# Contributing to AI Stock Screener Agent

🎉 Thank you for your interest in contributing to the AI Stock Screener Agent! We welcome contributions from developers of all skill levels.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## 🤝 Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct. By participating, you agree to uphold this code.

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- Ollama installed
- Qwen model pulled (`ollama pull qwen`)

### Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/yourusername/ai-stock-screener-agent.git
cd ai-stock-screener-agent

# Add upstream remote
git remote add upstream https://github.com/originalowner/ai-stock-screener-agent.git
```

## 💻 Development Setup

### 1. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install all dependencies
pip install -r requirements.txt

# Or minimal dependencies
pip install -r requirements-minimal.txt

# Install development dependencies
pip install pytest black flake8 mypy
```

### 3. Verify Installation

```bash
python 1.py
# Should start the interactive agent
```

## 📝 Contributing Guidelines

### Types of Contributions

We welcome several types of contributions:

1. **🐛 Bug Reports**: Found a bug? Let us know!
2. **✨ Feature Requests**: Have an idea? We'd love to hear it!
3. **🔧 Code Contributions**: Fix bugs or implement features
4. **📚 Documentation**: Improve docs, README, or code comments
5. **🧪 Tests**: Add or improve test coverage
6. **🎨 UI/UX**: Improve the terminal interface

### Areas Needing Help

- 🔍 **Additional Screeners**: Implement new screening algorithms
- 🌐 **Internationalization**: Add support for more languages/markets
- 📈 **Charting**: ASCII chart generation for price movements
- 🔔 **Alerts**: Price movement notification system
- 🤖 **Model Support**: Integration with more LLM providers
- 📱 **Mobile**: Terminal app optimization for mobile devices

## 🔄 Pull Request Process

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/bug-description
# or
git checkout -b docs/documentation-improvement
```

### 2. Make Changes

- Write clean, readable code
- Follow existing code style
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run the application
python 1.py

# Run tests (if available)
python -m pytest

# Check code style
black --check .
flake8 .
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "Add detailed description of your changes"
```

Use conventional commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding tests

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title and description
- Reference any related issues
- Screenshots (if UI changes)
- Testing instructions

## 🐛 Issue Guidelines

### Bug Reports

When reporting bugs, please include:

```markdown
**Bug Description**
A clear description of the bug.

**Steps to Reproduce**
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment**
- OS: [e.g. Windows 10, macOS 12, Ubuntu 20.04]
- Python Version: [e.g. 3.9.7]
- Ollama Version: [e.g. 0.1.25]
- Model: [e.g. qwen:latest]

**Additional Context**
Add any other context about the problem here.
```

### Feature Requests

When requesting features, please include:

```markdown
**Feature Description**
A clear description of the feature you'd like to see.

**Use Case**
Why would this feature be useful? Who would benefit?

**Proposed Solution**
How do you envision this working?

**Alternatives Considered**
Any alternative solutions you've considered.

**Additional Context**
Any other context or screenshots about the feature request.
```

## 📏 Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) conventions
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [flake8](https://flake8.pycqa.org/) for linting
- Use type hints where appropriate

### Code Organization

```python
# File structure example
"""
Module docstring explaining the purpose.
"""

# Standard library imports
import json
from typing import Dict, List

# Third-party imports
from langchain.tools import tool
import yfinance as yf

# Local imports
from .utils import helper_function

# Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Classes and functions...
```

### Naming Conventions

- **Variables**: `snake_case`
- **Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private methods**: `_leading_underscore`

### Documentation

- Use docstrings for all functions and classes
- Include type hints
- Add inline comments for complex logic

```python
def format_stock_results(stocks_data: List[Dict], screen_type: str) -> str:
    """
    Format stock data into a structured, readable output.
    
    Args:
        stocks_data: List of dictionaries containing stock information
        screen_type: Type of screening performed (e.g., 'day_gainers')
        
    Returns:
        Formatted ASCII table string with stock data
        
    Raises:
        ValueError: If stocks_data is empty or invalid
    """
    # Implementation here...
```

## 🧪 Testing

### Writing Tests

```python
import pytest
from unittest.mock import Mock, patch
from tool import simple_screener

def test_simple_screener_success():
    """Test successful stock screening."""
    # Arrange
    mock_data = {...}
    
    # Act
    with patch('yfinance.screen') as mock_screen:
        mock_screen.return_value = mock_data
        result = simple_screener("day_gainers", 0)
    
    # Assert
    assert "STOCK SCREENER RESULTS" in result
    assert len(result) > 100  # Ensure formatted output
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=.

# Run specific test file
python -m pytest tests/test_tool.py

# Run with verbose output
python -m pytest -v
```

## 📚 Documentation

### Code Documentation

- Write clear docstrings
- Include examples in docstrings
- Document complex algorithms
- Keep README.md updated

### API Documentation

When adding new functions, document them in the README:

```markdown
#### `new_function(param1: str, param2: int) -> bool`
Brief description of what the function does.

**Parameters:**
- `param1`: Description of parameter
- `param2`: Description of parameter

**Returns:**
- Description of return value

**Example:**
```python
result = new_function("example", 42)
```
```

## 🏷️ Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Test all functionality
- [ ] Update documentation
- [ ] Create release notes
- [ ] Tag release

## 🎯 Good First Issues

Looking for good first contributions? Check issues labeled:
- `good first issue`
- `help wanted`
- `documentation`
- `bug`

## 💬 Getting Help

- **GitHub Discussions**: For questions and general discussion
- **GitHub Issues**: For bug reports and feature requests
- **Code Review**: We provide constructive feedback on all PRs

## 🏆 Recognition

Contributors will be:
- Listed in the README.md
- Mentioned in release notes
- Given credit in commit history

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to AI Stock Screener Agent! 🚀
