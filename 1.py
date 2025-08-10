from typing import Annotated 
from langgraph.graph import START, END, StateGraph
from langgraph.graph.message import add_messages 
from langgraph.checkpoint.memory import InMemorySaver 
from langchain_ollama import ChatOllama
from colorama import Fore 
from langgraph.prebuilt import ToolNode 
from tool import simple_screener

# 2. Create LLM
llm = ChatOllama(model='qwen')

# 8. tool
tools = [simple_screener]
# 9. Bind LLM with tools
llm_with_tools = llm.bind_tools(tools)
# 10. Create Tool Node 
tool_node = ToolNode(tools)

# 3. Create state
class State(dict): 
    messages: Annotated[list, add_messages]
# 4. Build LLM node 
def chatbot(state:State): 
    print(state['messages'])
    last_message = state['messages'][-1].content.lower()
    
    # Check if user is asking for stock screening
    stock_keywords = ['stock', 'gainers', 'losers', 'active', 'tech', 'undervalued', 'small cap', 'large cap', 'london', 'tomorrow', 'session']
    if any(keyword in last_message for keyword in stock_keywords):
        # Manually call the screener based on keywords
        try:
            if 'gainer' in last_message or 'winner' in last_message:
                result = simple_screener.invoke({"screen_type": "day_gainers", "offset": 0})
            elif 'loser' in last_message or 'decliner' in last_message:
                result = simple_screener.invoke({"screen_type": "day_losers", "offset": 0})
            elif 'active' in last_message or 'volume' in last_message:
                result = simple_screener.invoke({"screen_type": "most_actives", "offset": 0})
            elif 'tech' in last_message or 'technology' in last_message:
                result = simple_screener.invoke({"screen_type": "growth_technology_stocks", "offset": 0})
            elif 'undervalued' in last_message and 'large' in last_message:
                result = simple_screener.invoke({"screen_type": "undervalued_large_caps", "offset": 0})
            elif 'small' in last_message:
                result = simple_screener.invoke({"screen_type": "small_cap_gainers", "offset": 0})
            elif 'london' in last_message or 'tomorrow' in last_message:
                # For London session, show most actives with London focus
                result = simple_screener.invoke({"screen_type": "most_actives", "offset": 0})
            else:
                # Default to most actives
                result = simple_screener.invoke({"screen_type": "most_actives", "offset": 0})
            
            return {"messages":[{"role": "assistant", "content": result}]}
        except Exception as e:
            print(f"Screener failed: {e}")
            # Fallback to regular LLM
            return {"messages":[llm.invoke(state['messages'])]}
    else:
        # Regular conversation - provide helpful guidance
        helpful_response = """I'm your Stock Screener Assistant! 📊

I can help you find stocks based on various criteria. Here are some things you can ask me:

🔍 **Stock Screeners:**
• "Show me day gainers" - Stocks with highest daily gains
• "Find day losers" - Stocks with biggest daily losses
• "Most active stocks" - Highest volume stocks
• "Technology growth stocks" - Tech companies with growth potential
• "Undervalued large caps" - Large cap value stocks
• "Small cap gainers" - Small cap growth stocks

💡 **Tips:**
• Be specific about what type of stocks you're looking for
• I can provide real-time data from Yahoo Finance
• Ask about market trends or specific sectors

What type of stocks would you like to screen today?"""
        
        return {"messages":[{"role": "assistant", "content": helpful_response}]}
# 11. Create Router Node
def router(state:State): 
    # Since we're not using tools, always go to END
    return END 

# 5. Assemble Graph 
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)
graph_builder.add_edge(START, "chatbot")
# 12. Update graph for Tools
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_conditional_edges("chatbot", router)
# 6. Add Memory and Compile Graph 
memory = InMemorySaver() 
graph = graph_builder.compile(checkpointer=memory)
# 7. Build call loop and run it
if __name__ == '__main__': 
    print("\n" + "="*80)
    print(Fore.CYAN + "🚀 Welcome to the Stock Screener Agent!" + Fore.RESET)
    print("="*80)
    print(Fore.LIGHTGREEN_EX + """
📊 Available Stock Screeners:
• Day Gainers - Stocks with highest daily gains
• Day Losers - Stocks with highest daily losses  
• Most Actives - Highest volume stocks
• Growth Technology Stocks - Tech growth companies
• Undervalued Large Caps - Large cap value stocks
• Small Cap Gainers - Small cap growth stocks

💡 Try asking: "Show me day gainers" or "Find tech stocks"
🔧 Type 'quit' or 'exit' to close the application
""" + Fore.RESET)
    print("="*80 + "\n")
    
    while True: 
        prompt = input(Fore.LIGHTBLUE_EX + "🤖 Ask about stocks: " + Fore.RESET)
        
        if prompt.lower() in ['quit', 'exit', 'q']:
            print(Fore.YELLOW + "👋 Thanks for using Stock Screener Agent!" + Fore.RESET)
            break
        try:
            result = graph.invoke({"messages":[{"role":"user", "content":prompt}]}, config={"configurable":{"thread_id":1234}})
            print("\n" + "="*80)
            print(Fore.LIGHTYELLOW_EX + result['messages'][-1].content + Fore.RESET)
            print("="*80 + "\n")
        except Exception as e:
            print(Fore.RED + f"❌ Error: {e}" + Fore.RESET)
            print(Fore.YELLOW + "🔄 Trying with fallback approach..." + Fore.RESET)
            # Fallback: direct LLM call without tools
            try:
                response = llm.invoke([{"role":"user", "content":prompt}])
                print("\n" + "="*80)
                print(Fore.LIGHTYELLOW_EX + response.content + Fore.RESET)
                print("="*80 + "\n")
            except Exception as fallback_error:
                print(Fore.RED + f"❌ Fallback also failed: {fallback_error}" + Fore.RESET) 


