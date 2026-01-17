# Contributing to KaggleRun

First off, thanks for taking the time to contribute!

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, error messages)
- **Describe the behavior you observed vs expected**
- **Include your environment** (Python version, OS, kagglerun version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List any alternatives you've considered**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes: `pytest tests/ -v`
4. Make sure your code follows the existing style
5. Issue that pull request!

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/kagglerun.git
cd kagglerun

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run linting
ruff check src/
black --check src/
```

## Code Style

- We use [Black](https://black.readthedocs.io/) for code formatting
- We use [Ruff](https://github.com/astral-sh/ruff) for linting
- Type hints are encouraged
- Docstrings for all public functions/classes

## Testing

- Write tests for new features
- Tests should be runnable without actual Kaggle API access (use mocking)
- Aim for high coverage on critical paths

## Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Keep the first line under 72 characters
- Reference issues and pull requests liberally after the first line

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue with your question!
