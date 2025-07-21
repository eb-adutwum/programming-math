# Internal Docs — Programming Math

Welcome to the **internal developer documentation** for the `programming-math` project. This guide is for contributors maintaining and extending the project. It outlines the code structure, development workflows, testing, and best practices.

---

## Project Overview

**Programming Math** is a modular Python library designed to support symbolic and numeric mathematics operations. It integrates DevOps practices like testing, CLI tooling, and coverage tracking — built to evolve alongside the author’s learning in mathematics with software engineering.

---

## Project Structure

```bash
programming-math/
│
├── src/
│   ├── algebra/               # Algebra module
│   │   ├── __init__.py
│   │   ├── algebra_utils.py   # Core algebra functions
│   │   └── __main__.py        # CLI entry point for algebra module
│   └── calculus/              # (Under development) Calculus module
│
├── tests/
│   ├── algebra/               # Unit and CLI tests for algebra
│   │   ├── test_algebra_utils.py
│   │   └── test_cli.py
│   └── calculus/              # (Pending)
│
├── .github/                   # (Optional) GitHub actions or PR templates
│
├── .gitignore
├── pyproject.toml            # Project metadata and dependencies
├── pytest.ini                # Pytest and coverage config
└── internal-docs.md          
```

---

## ️ Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/eb-adutwum/programming-math.git
cd programming-math
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .mathvenv
source .mathvenv/bin/activate  # Windows: .mathvenv\Scripts\activate
```

### 3. Install in Editable Mode

```bash
pip install -e .
```

---

##  Dependencies

* [`sympy`](https://www.sympy.org/) – symbolic math engine
* [`pytest`](https://docs.pytest.org/) – testing framework
* [`pytest-cov`](https://pytest-cov.readthedocs.io/) – code coverage
* [`black`](https://black.readthedocs.io/) – code formatter

> Add new dependencies via `pyproject.toml`.

---

## Testing

Run all tests and generate a coverage report:(You might not need to though because every flag is in the config file `pytest.ini`)

```bash
python -m pytest
```

Run a specific test file:

```bash
python -m pytest tests/algebra/test_cli.py
```

Check CLI integration (uses `subprocess`):

```bash
python -m pytest -k "test_factor_cli"
```

---

##  Coverage & Formatting

### Run Coverage

```bash
python -m pytest --cov=src
```

### Format Code

```bash
black src/ tests/
```

---

##  Branching & Commit Conventions

We follow a semantic branch and commit style:

### Branch Naming

* `feat/algebra`: New feature
* `fix/factor-bug`: Bug fix
* `chore/init`: Setup or minor config
* `docs/setup-guide`: Documentation

### Commit Format

```bash
<type>(<scope>): <description>
```

Examples:

* `feat(algebra): implement factor and expand`
* `test(algebra): add CLI integration test`
* `build(prog-math): add pyproject.toml`

---

## CLI Entry Point

Run CLI algebra module like this:

```bash
python -m algebra factor "x**2 - 1"
```

> Located at `src/algebra/__main__.py`

---

##  Sample Dev Flow

```bash
# Start new work
git switch -c feat/algebra-improve-solve

# Edit or add new feature in src/
# Write tests in tests/algebra/

# Run tests
python -m pytest

# Format code
black src/ tests/

# Stage and commit
git add .
git commit -m "feat(algebra): improve solve to handle complex roots"

# Push
git push origin feat/algebra-improve-solve

# Open PR into main or dev
```

---

##  Future Modules (Planned)

* `calculus/` – limits, derivatives, integrals
* `geometry/` – symbolic shapes, equations
* `statistics/` – mean, variance, distributions
* `numerical/` – approximation methods

---

##  Support

This project is led by [Elijah Boateng](mailto:eb.adutwum@gmail.com).
All issues, ideas, or suggestions are welcome via pull requests or GitHub discussions.
