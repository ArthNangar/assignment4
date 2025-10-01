# Python Command-Line Calculator  

A modular, test-driven calculator built in Python that highlights **clean architecture**, **factory design pattern**, and **100% unit test coverage**.  

This project was developed as part of an academic assignment to practice professional-grade software development practices, including testing, CI/CD, and documentation.  

---

##  Features  
- Interactive **REPL interface** (Read–Eval–Print–Loop)  
- Arithmetic operations:  
  - Addition 
  - Subtraction 
  - Multiplication
  - Division (with zero-division handling)  
  - Power
  - Modulo 
- `help`, `history`, and `exit` commands for smooth user interaction  
- **Error handling** using both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission) paradigms  
- Fully modular code with **factory pattern** for extensibility  
- **100% test coverage** with `pytest` and `pytest-cov`  
- Automated CI/CD pipeline with **GitHub Actions**  

---

## 📂 Project Structure  

```plaintext
calculator-repl/
├── app/
│   ├── calculator/          # REPL interface
│   ├── calculation/         # Calculation classes & factory
│   └── operation/           # Arithmetic operations
├── tests/                   # Unit and integration tests
│   ├── test_calculator.py
│   ├── test_calculation.py
│   └── test_operations.py
├── requirements.txt         # Dependencies
├── .coveragerc              # Coverage configuration
├── pytest.ini               # Pytest configuration
└── .github/workflows/       # CI/CD with GitHub Actions

```
## Installation
Clone the repository and set up your environment:
```

git clone https://github.com/<your-username>/calculator-repl.git
cd calculator-repl
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the calculator in interactive mode:
```
python -m app.calculator.repl
```
## Examples:
```
Welcome to Calculator! Type 'help' for commands.
>>> add 10 5
add 10.0 5.0 = 15.0
>>> pow 2 4
pow 2.0 4.0 = 16.0
>>> mod 17 5
mod 17.0 5.0 = 2.0
>>> history
add 10.0 5.0 = 15.0
pow 2.0 4.0 = 16.0
mod 17.0 5.0 = 2.0
>>> exit
Goodbye!
```
 
## Testing
Run all tests:
``` 
pytest

PYTHONPATH=. pytest --cov=app --cov-report=term-missing tests/
```
## CI/CD with GitHub Actions

Every push and pull request to main triggers GitHub Actions to:

Install dependencies

Run all tests with pytest

Enforce 100% coverage (build fails if coverage < 100%)

## Design Principles

Factory Pattern:
Operations are dynamically mapped to calculation objects, making it easy to add new ones.

Error Handling:
Manages invalid input, invalid commands, and division by zero.

## 📜 License

MIT License – see LICENSE
 for details.

## 👤 Author

Arth Nangar

Date: 09/30/2025
