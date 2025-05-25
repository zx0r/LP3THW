# Learn Python the Hard Way: Build Like a Senior

A comprehensive collection of exercises and projects based on "Learn Python the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code" by Zed Shaw—reimagined with senior-level engineering principles and best practices.

## Overview

This repository contains all exercises from the book, enhanced with modern Python tooling, code quality checks, and scalable project organization. Each solution emphasizes code readability, maintainability, and robustness, helping you not only learn Python, but also adopt the habits of professional software engineers.

## Features

- **Clear, modular code** for each exercise
- **Automated testing** with `pytest`
- **Static analysis** via `flake8` and `mypy`
- **Consistent formatting** using `black`
- **Sample data and skeleton projects** for advanced topics
- **Jupyter notebooks** for exploration and self-guided learning
- **Real-world directory structure** mirroring production-grade Python projects

## Repository Structure

```
.
├── ex1-50_jupyter_notebook.ipynb  # All exercises in interactive form
├── ex1.py ... ex50.py             # Individual exercises
├── ex47/ ... ex49/                # Skeleton project templates
├── ex15_sample.txt, etc.          # Sample data files
├── tests/                         # Pytest-based unit tests
├── .gitignore
├── requirements.txt
├── README.md
```

## Best Practices Applied

- **DRY Principle**: Code is written to maximize reuse and minimize repetition.
- **Testing**: Each exercise has corresponding unit tests in `/tests/`.
- **Static Typing**: Type annotations and `mypy` ensure early error detection.
- **Linting and Formatting**: Enforced with `flake8` and `black` for code consistency.
- **Documentation**: Every module and function includes docstrings for clarity.
- **Version Control**: `.gitignore` and clear commit messages for maintainability.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/zx0r/learn-python-the-hard-way-senior.git
   cd learn-python-the-hard-way-senior
   ```

2. **Set up a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Explore and edit exercises**
   - Start with `ex1.py` or the Jupyter notebook.
   - Modify, refactor, and add tests as you learn.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

**The best way to learn is to build like a senior—one exercise at a time.**
