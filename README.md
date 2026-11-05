# Python Practices

A personal collection of Python practice programs and notes, organized by topic. Most of the code was written while working through [CS50's Introduction to Programming with Python (CS50P)](https://cs50.harvard.edu/python/), with a few extra practice programs mixed in.

Each folder focuses on one concept, and many files include multiple alternative solutions in comments — they are kept as learning notes rather than polished production code.

## Repository Structure

```text
Python-Practices/
├── CS50-P/
│   ├── Conditionals/          # if / elif / else, match, parity, grading
│   ├── Et Cetara/             # extra OOP examples (classes, properties)
│   ├── Exceptions/            # try / except, input validation loops
│   ├── File IO/               # reading/writing text & CSV, GIF assembly
│   ├── Functions & Variables/ # defining functions, scope, type conversion
│   ├── Libraries/             # random, statistics, sys, requests, cowsay
│   ├── Loops/                 # for / while, range, lists, Mario patterns
│   ├── Oop/                   # classes, properties, inheritance, operators
│   ├── Others/                # Hello World, factorial
│   ├── Regular Expression/    # email and URL validation with re
│   └── Unit Test/             # pytest tests for a square() function
├── names.txt                  # sample data for File IO scripts
├── students.csv               # sample data for File IO scripts
├── students_home.csv          # sample data for File IO scripts
└── students_home_2.csv        # sample data for File IO scripts
```

## Topics Covered

| Folder | What it practices |
| --- | --- |
| `Conditionals` | Comparisons, `if`/`elif`/`else`, `match` statements, even/odd checks, grade calculation |
| `Et Cetara` | Class constants, properties, encapsulation (bank account), simple classes |
| `Exceptions` | `try`/`except`/`else`, `ValueError`, retry loops, safe integer input |
| `File IO` | `open()`, reading and writing text files, CSV files, combining images into a GIF with Pillow |
| `Functions & Variables` | `def`, parameters, return values, `main()`, `int()`/`float()`/`str()` conversion |
| `Libraries` | `random`, `statistics`, `sys.argv`, `requests`, `cowsay` |
| `Loops` | `for`/`while`, `range()`, iterating lists/dicts, nested loops, Mario-style patterns |
| `Oop` | Classes, `__init__`, `__str__`, properties and setters, class methods, inheritance, operator overloading |
| `Others` | Hello World and a recursive factorial |
| `Regular Expression` | Pattern matching and validation with the `re` module |
| `Unit Test` | Assertions and testing with `pytest` |

## Requirements

- **Python 3.10 or newer** — some examples use `match` statements.
- Most programs use only the Python standard library.
- A few examples need third-party packages:

  ```bash
  pip install cowsay requests pillow pytest
  ```

## Getting Started

```bash
git clone https://github.com/imbidyutpaul/Python-Practices.git
cd Python-Practices
```

Optionally create and activate a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

## Running the Programs

Run any script directly with Python:

```bash
python "CS50-P/Others/Hello.py"
python "CS50-P/Conditionals/grade.py"
```

The File IO examples open `names.txt` and `students.csv` using **relative paths**, so run them from the repository root:

```bash
python "CS50-P/File IO/read_names.py"
python "CS50-P/File IO/read_students.py"
```

`CS50-P/Oop/ex.py` imports sibling modules (`student_classmethod.py` and `hat.py`), so run it from inside the `Oop` folder:

```bash
cd "CS50-P/Oop"
python ex.py
```

`CS50-P/File IO/costume.py` builds an animated GIF from image paths passed on the command line:

```bash
cd "CS50-P/File IO"
python costume.py costume_1.gif costume_2.gif
```

> Note: many scripts are interactive and will prompt for input when run.

## Running the Tests

The unit tests use `pytest`:

```bash
python -m pytest "CS50-P/Unit Test"
```

They verify that `square()` works for positive numbers, negative numbers, and zero, and that it raises `TypeError` for a string.

## Notes

- The code is intentionally educational: several files contain commented-out alternatives showing different ways to solve the same problem.
- File and folder names are preserved as written during the course (for example, `Et Cetara`).
- This is a personal learning repository and is not affiliated with or endorsed by CS50.
