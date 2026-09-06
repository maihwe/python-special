# Topic 20: Modules - Exercises

## Overview

These exercises teach you to create modules, organize packages, and structure professional Python projects.

---

## Exercise 1: Creating a Simple Module

**Create a file `calculator.py` that:**
- Defines functions: add(), subtract(), multiply(), divide()
- Each function takes two numbers and returns result
- Create `main.py` that imports from calculator
- Calls each function and prints results

**Example:**
```
from calculator import add, multiply
print(add(5, 3))       # 8
print(multiply(5, 3))  # 15
```

**Concepts:** Creating modules, importing functions

---

## Exercise 2: Module with Constants

**Create a file `config.py` that:**
- Defines constants: MAX_USERS, DATABASE_URL, DEBUG_MODE
- Create `app.py` that imports these constants
- Uses constants in logic
- Shows how module-level constants work

**Example:**
```
from config import MAX_USERS, DEBUG_MODE
print(f"Max users: {MAX_USERS}")
if DEBUG_MODE:
    print("Debug mode active")
```

**Concepts:** Module constants, configuration management

---

## Exercise 3: Package Structure

**Create package structure:**
```
utilities/
  __init__.py
  math_utils.py    (add, subtract functions)
  string_utils.py  (upper, reverse functions)
```

**In main.py:**
- Import from utilities.math_utils
- Import from utilities.string_utils
- Use functions from each module

**Example:**
```
from utilities.math_utils import add
from utilities.string_utils import reverse

print(add(5, 3))
print(reverse("hello"))
```

**Concepts:** Packages, sub-modules, organization

---

## Exercise 4: Understanding `__init__.py`

**Create package structure:**
```
mylib/
  __init__.py      (import and expose core items)
  core.py          (define functions)
```

**In `__init__.py`:**
- Import core functions
- Make them available at package level
- Use from main.py

**Example:**
```
# mylib/__init__.py
from mylib.core import helper_function

# main.py
from mylib import helper_function
```

**Concepts:** Package initialization, exposure

---

## Exercise 5: Standard Library Exploration

**Write program that:**
- Uses at least 5 different standard library modules
- Shows practical usage of each
- Demonstrates real-world applications
- Explains what each module does

**Example modules:** math, random, datetime, os, json

**Concepts:** Standard library, module usage

---

## Exercise 6: Avoiding Name Collisions

**Create two modules with same function names:**
```
math_ops.py  (has add(), multiply())
string_ops.py (has add(), multiply())
```

**In main.py:**
- Import both modules
- Call both versions of add() without collision
- Show how to avoid confusion

**Concepts:** Namespace isolation, aliasing

---

## Exercise 7: The `__name__` Guard

**Create file `demo.py` with:**
- Functions that perform calculations
- Code in `if __name__ == "__main__":` block
- Create `main.py` that imports functions
- Show `__name__` guard prevents unwanted execution

**Example:**
```
# demo.py
def calculate():
    return 42

if __name__ == "__main__":
    print(calculate())  # Only runs if demo.py is main

# main.py
from demo import calculate
# calculate() runs but not the guard code
```

**Concepts:** Entry points, main guards

---

## Exercise 8: Module with Class

**Create module `person_module.py`:**
- Defines Person class
- With __init__, methods, attributes
- Create main.py that imports class
- Creates and uses Person instances

**Example:**
```
# person_module.py
class Person:
    def __init__(self, name):
        self.name = name

# main.py
from person_module import Person
p = Person("Alice")
print(p.name)
```

**Concepts:** Classes in modules, importing classes

---

## Exercise 9: Module Aliasing

**Create multiple imports with aliases:**
- Import datetime as dt
- Import random as rand
- Import math as m
- Use each with their alias

**Example:**
```
import datetime as dt
import random as rand
from math import pi as PI

print(dt.datetime.now())
print(rand.randint(1, 10))
print(PI)
```

**Concepts:** Aliasing, import variety

---

## Exercise 10: Professional Project Structure

**Create project structure:**
```
my_project/
  my_package/
    __init__.py
    main.py
    utils.py
  tests/
    __init__.py
    test_utils.py
  main.py
  requirements.txt
  README.md
```

**Implement:**
- my_package with functions
- Tests that import from package
- Main entry point
- Documentation
- Requirements file

**Concepts:** Professional organization, project structure

---

## Challenge Exercises (Optional)

### Challenge 1: Create a Reusable Data Utilities Package
- Create package `data_utils` with multiple modules:
  - `validation.py` - validate emails, phone numbers, etc.
  - `formatting.py` - format dates, numbers, text
  - `conversion.py` - convert between data types
  - `__init__.py` - expose all utilities
- Write comprehensive tests
- Create README with usage examples
- Make it importable as: `from data_utils import validate_email`

### Challenge 2: Create a Game Package
- Structure as package:
  - `models/` - Player, Enemy, Item classes
  - `game.py` - game loop and logic
  - `config.py` - constants (MAX_HP, etc.)
  - `utils.py` - helper functions
- Implement proper imports
- Use config module throughout
- Test individual modules
- Create main.py that runs game

### Challenge 3: Create a Web Scraper Package
- Organize as package:
  - `scraper.py` - main scraping logic
  - `parser.py` - parse HTML
  - `storage.py` - save to file/database
  - `config.py` - URLs, settings
  - `utils.py` - utilities
- Use different modules for different concerns
- Implement proper error handling
- Use configuration module for settings

### Challenge 4: Analyze and Document Existing Module
- Choose a standard library module (json, csv, re, etc.)
- Write comprehensive guide:
  - What the module does
  - Key functions/classes
  - 10+ practical examples
  - Common use cases
  - Best practices
- Organize as document with examples.py

---

## Tips for Success

1. **Start small:** One module before multiple
2. **Name clearly:** Module names describe contents
3. **Use `__init__.py`:** Always include in packages
4. **Avoid circular imports:** Plan structure first
5. **Test each module:** Import and test separately
6. **Document code:** Add docstrings and comments
7. **Follow structure:** Professional structure matters

---

## Key Takeaways

After these exercises, you should:
- ✅ Create Python modules
- ✅ Organize modules into packages
- ✅ Use `__init__.py` properly
- ✅ Import efficiently
- ✅ Avoid name collisions
- ✅ Use standard library modules
- ✅ Understand entry points
- ✅ Structure professional projects
- ✅ Document and test modules
- ✅ Think in terms of reusable code

