<div align="center">

# Python Practices

**A structured collection of Python exercises and notes, built while working through [CS50P](https://cs50.harvard.edu/python/) and beyond.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CS50P](https://img.shields.io/badge/CS50P-Practice-A51C30?style=for-the-badge)](https://cs50.harvard.edu/python/)
[![pytest](https://img.shields.io/badge/Tests-pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)

[Overview](#overview) · [Repository Layout](#repository-layout) · [Topics](#topics-covered) · [Quick Start](#quick-start) · [Usage](#running-the-programs) · [Tests](#running-the-tests) · [Notes](#notes)

</div>

---

## Overview

This repository is a personal, topic-by-topic record of learning Python. It started with [CS50's Introduction to Programming with Python (CS50P)](https://cs50.harvard.edu/python/) and grew to include additional practice programs and experiments.

Each folder focuses on a single concept. Many files contain multiple alternative solutions in comments, so they are kept as learning notes rather than polished production code.

> **At a glance:** 11 topic folders · 60 Python files · 4 sample data files · automated `pytest` suite.

### Highlights

- **Organized by concept** — one folder per topic, from conditionals and loops to OOP and regular expressions.
- **Learning-first** — solutions are short, readable, and often include commented alternatives.
- **Broad coverage** — core language features, file handling, third-party libraries, and testing.
- **Runnable examples** — every script can be executed directly, with sample data included.

## Repository Layout

```text
Python-Practices/
├── CS50-P/
│   ├── Conditionals/           # if / elif / else, match, parity, grading
│   ├── Et Cetara/              # class constants, properties, encapsulation
│   ├── Exceptions/             # try / except, validation loops
│   ├── File IO/                # text & CSV handling, GIF assembly
│   ├── Functions & Variables/  # functions, scope, type conversion
│   ├── Libraries/              # random, statistics, sys, requests, cowsay
│   ├── Loops/                  # for / while, range, lists, Mario patterns
│   ├── Oop/                    # classes, inheritance, operator overloading
│   ├── Others/                 # Hello World, factorial
│   ├── Regular Expression/     # email and URL validation
│   └── Unit Test/              # pytest tests for square()
├── names.txt                   # sample input for File IO
├── students.csv                # sample input for File IO
├── students_home.csv           # sample input for File IO
└── students_home_2.csv         # sample input for File IO
```

## Topics Covered

| Folder | What it practices | Example files |
| :--- | :--- | :--- |
| `Conditionals` | Comparisons, `if`/`elif`/`else`, `match` statements, even/odd checks, grade calculation | `compare.py`, `grade.py`, `house.py` |
| `Et Cetara` | Class constants, properties, encapsulation (bank account), sets | `bank.py`, `meows.py`, `houses.py` |
| `Exceptions` | `try`/`except`/`else`, `ValueError`, retry loops, safe integer input | `number.py`, `number_2.py`, `number_3.py` |
| `File IO` | Reading and writing text files, CSV files, combining images into a GIF with Pillow | `read_names.py`, `write_students.py`, `costume.py` |
| `Functions & Variables` | `def`, parameters, return values, `main()`, `int()`/`float()`/`str()` conversion | `def_function_2.py`, `int_function.py`, `str_function.py` |
| `Libraries` | `random`, `statistics`, `sys.argv`, `requests`, `cowsay` | `average.py`, `itunes.py`, `say.py` |
| `Loops` | `for`/`while`, `range()`, iterating lists and dicts, nested loops, Mario-style patterns | `cat_for.py`, `hogwarts.py`, `mario.py` |
| `Oop` | Classes, `__init__`, `__str__`, properties and setters, class methods, inheritance, operator overloading | `student_properties.py`, `wizard.py`, `vault.py` |
| `Others` | Hello World and a recursive factorial | `Hello.py`, `factorial.py` |
| `Regular Expression` | Pattern matching and validation with the `re` module | `email_validate.py`, `URL_validate.py` |
| `Unit Test` | Assertions and testing with `pytest` | `calculator.py`, `test_calculator.py` |

## Requirements

| Requirement | Details |
| :--- | :--- |
| **Python** | 3.10 or newer — some examples use `match` statements. |
| **Standard library** | Used by most programs; no installation needed. |
| **Third-party packages** | Required only for a few examples (see below). |

Install the optional dependencies with:

```bash
pip install cowsay requests pillow pytest
```

| Package | Used for | Example |
| :--- | :--- | :--- |
| `cowsay` | ASCII-art speech bubbles | `CS50-P/Libraries/say.py` |
| `requests` | HTTP requests to the iTunes Search API | `CS50-P/Libraries/itunes.py` |
| `Pillow` | Assembling images into an animated GIF | `CS50-P/File IO/costume.py` |
| `pytest` | Running the unit test suite | `CS50-P/Unit Test/` |

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/imbidyutpaul/Python-Practices.git
cd Python-Practices
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it with the command for your platform:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install cowsay requests pillow pytest
```

## Running the Programs

Most scripts are standalone and can be run directly from the repository root:

```bash
python "CS50-P/Others/Hello.py"
python "CS50-P/Conditionals/grade.py"
```

> Many programs are interactive and will prompt for input when run.

### File I/O examples

These scripts use **relative paths**, so run them from the repository root:

```bash
python "CS50-P/File IO/read_names.py"
python "CS50-P/File IO/read_students.py"
```

They read from `names.txt`, `students.csv`, and the related sample files at the repository root.

### Module imports (OOP example)

`CS50-P/Oop/ex.py` imports sibling modules (`student_classmethod.py` and `hat.py`), so run it from inside the `Oop` folder:

```bash
cd "CS50-P/Oop"
python ex.py
```

### GIF assembly

`costume.py` combines the supplied images into `costume.gif`:

```bash
cd "CS50-P/File IO"
python costume.py costume_1.gif costume_2.gif
```

## Running the Tests

Run the `pytest` suite from the repository root:

```bash
python -m pytest "CS50-P/Unit Test" -v
```

| Test | What it verifies |
| :--- | :--- |
| `test_positive` | `square()` handles positive integers |
| `test_negative` | `square()` handles negative integers |
| `test_zero` | `square(0)` returns `0` |
| `test_str` | `square("cat")` raises `TypeError` |

## Notes

- **Educational intent.** The code is intentionally learning-focused; clarity is preferred over production-level structure.
- **Alternative solutions.** Several files contain commented-out approaches showing different ways to solve the same problem.
- **Preserved names.** File and folder names are kept as written during the course (for example, `Et Cetara`).
- **No affiliation.** This is a personal learning repository and is not affiliated with or endorsed by CS50.

---

<div align="center">

**Created and maintained by [Bidyut Paul](https://github.com/imbidyutpaul)**

</div>
