# CI/CD Basics – A Super Simple Demo

This repository is a **beginner-friendly** project that demonstrates the **basic structure of a CI/CD pipeline** using **GitHub Actions**. It includes a simple Python script, tests with `pytest`, and an automated workflow to run tests on every push.

---

## 🚀 What Is This?
This project helps you **understand how CI/CD works** by automating the process of testing a Python script when changes are made to the repository.

- **CI (Continuous Integration)**: Automatically tests code when pushed to GitHub.
- **CD (Continuous Deployment)**: Deploys changes automatically (not covered in this demo).

---

## 📂 Project Structure
```
/CICD-basics
├── calculator.py            # Simple math functions
├── test.py                  # Tests using pytest
├── requirements.txt         # Lists dependencies (pytest)
└── .github/
    └── workflows/
        └── python-ci.yml    # GitHub Actions CI/CD config
```

---

## 📜 File Descriptions
### `calculator.py`
Contains simple math functions to be tested.
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```

### `test.py`
Contains tests using `pytest`.
```python
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 0) == "Cannot divide by zero"

if __name__ == "__main__":
    pytest.main()
```

### `requirements.txt`
Lists dependencies needed for the project.
```
pytest
```

### `.github/workflows/python-ci.yml`
Defines the **GitHub Actions workflow** that runs tests automatically on every push.
```yaml
name: Python CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install --upgrade pip
        pip install -r requirements.txt  

    - name: Run tests
      run: pytest test.py
```

---

## 🔧 How to Use This Project

### 1️⃣ Install Dependencies
If you want to run tests locally, install dependencies first:
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Tests Locally
Execute tests with:
```bash
pytest test.py
```

### 3️⃣ Push Code to GitHub
```bash
git add .
git commit -m "Added basic CI/CD pipeline"
git push origin main
```

### 4️⃣ See CI/CD in Action 🚀
After pushing, go to the **GitHub Actions tab** in your repo, and you’ll see the tests running automatically!

---

## 📖 Definitions & Key Concepts

- **CI/CD Pipeline**: A process that automates testing and deployment.
- **`assert`**: A Python keyword that checks if a condition is `True`. If not, the program stops.
  ```python
  assert 2 + 2 == 4  # ✅ Passes
  assert 2 + 2 == 5  # ❌ Fails
  ```
- **GitHub Actions**: A built-in automation tool in GitHub that runs workflows like tests.
- **`pytest`**: A Python testing framework that runs test functions and checks assertions.
- **`requirements.txt`**: A file listing dependencies needed for the project.

---

## 🎯 Why This Matters
- 🏗️ **Learn CI/CD by doing** – This is a **hands-on** demo.
- ⚡ **Automate testing** – Never merge broken code.
- 🎯 **Super simple** – Focuses only on CI/CD basics.

Now go ahead, **modify something**, push to GitHub, and watch the magic happen! 🚀

