# Topic 20: Modules - Elaborate Examples
# Comprehensive examples of modules, packages, imports, and code organization

# ============================================================================
# EXAMPLE 1: Simple Module Import
# ============================================================================
# Import an entire module

print("Example 1: Module Import")
print("-" * 50)

import math

print(f"π = {math.pi}")
print(f"sqrt(16) = {math.sqrt(16)}")
print(f"sin(0) = {math.sin(0)}")
print()

# ============================================================================
# EXAMPLE 2: From Import
# ============================================================================
# Import specific items from module

print("Example 2: From Import")
print("-" * 50)

from math import pi, sqrt, sin

print(f"π = {pi}")
print(f"sqrt(16) = {sqrt(16)}")
print(f"sin(0) = {sin(0)}")
print()

# ============================================================================
# EXAMPLE 3: Import with Alias
# ============================================================================
# Rename imported items

print("Example 3: Aliasing")
print("-" * 50)

import math as m

print(f"π = {m.pi}")
print(f"sqrt(16) = {m.sqrt(16)}")

from math import pi as PI, sqrt as square_root

print(f"PI = {PI}")
print(f"square_root(25) = {square_root(25)}")
print()

# ============================================================================
# EXAMPLE 4: Standard Library - OS Module
# ============================================================================
# Working with operating system

print("Example 4: OS Module")
print("-" * 50)

import os

print(f"Current directory: {os.getcwd()}")
print(f"OS name: {os.name}")
print(f"Path separator: {os.sep}")

# Create a demo file path
demo_path = os.path.join("demo", "file.txt")
print(f"Path: {demo_path}")
print()

# ============================================================================
# EXAMPLE 5: Standard Library - Random Module
# ============================================================================
# Generate random values

print("Example 5: Random Module")
print("-" * 50)

import random

print(f"Random int (1-10): {random.randint(1, 10)}")
print(f"Random float (0-1): {random.random():.2f}")

items = ["apple", "banana", "cherry"]
print(f"Random choice: {random.choice(items)}")

random.shuffle(items)
print(f"Shuffled: {items}")
print()

# ============================================================================
# EXAMPLE 6: Standard Library - Datetime Module
# ============================================================================
# Date and time operations

print("Example 6: Datetime Module")
print("-" * 50)

import datetime

now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")

tomorrow = now + datetime.timedelta(days=1)
print(f"Tomorrow: {tomorrow}")
print()

# ============================================================================
# EXAMPLE 7: Standard Library - JSON Module
# ============================================================================
# Parse and create JSON

print("Example 7: JSON Module")
print("-" * 50)

import json

# Dictionary to JSON
data = {"name": "Alice", "age": 30, "city": "NYC"}
json_str = json.dumps(data)
print(f"JSON: {json_str}")

# JSON to dictionary
parsed = json.loads(json_str)
print(f"Parsed: {parsed}")
print(f"Name: {parsed['name']}")
print()

# ============================================================================
# EXAMPLE 8: Standard Library - Collections Module
# ============================================================================
# Specialized data structures

print("Example 8: Collections Module")
print("-" * 50)

from collections import Counter, defaultdict

# Counter counts occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(f"Word counts: {count}")
print(f"Most common: {count.most_common(1)}")

# defaultdict provides default values
dd = defaultdict(int)
for word in words:
    dd[word] += 1
print(f"defaultdict: {dict(dd)}")
print()

# ============================================================================
# EXAMPLE 9: Creating a Custom Module - Part 1
# ============================================================================
# Define functions in a module structure

print("Example 9: Custom Module (Part 1 - Define)")
print("-" * 50)

# We'll simulate a module by defining functions here
# In practice, this would be in a separate file

class MathModule:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def power(a, b):
        return a ** b

# This is like having a module with these functions
print("Module simulated with class")
print()

# ============================================================================
# EXAMPLE 10: Using Custom Module - Part 2
# ============================================================================
# Import and use the custom module

print("Example 10: Custom Module (Part 2 - Use)")
print("-" * 50)

# Simulate importing the module
math_module = MathModule()

print(f"add(5, 3) = {math_module.add(5, 3)}")
print(f"multiply(5, 3) = {math_module.multiply(5, 3)}")
print(f"power(2, 8) = {math_module.power(2, 8)}")
print()

# ============================================================================
# EXAMPLE 11: __name__ == "__main__"
# ============================================================================
# Running code only when executed directly

print("Example 11: Main Guard")
print("-" * 50)

# This demonstrates the pattern
def demo_function():
    return "Demo running"

# This block runs only if script executed directly
if __name__ == "__main__":
    print(f"Running as main: {demo_function()}")
else:
    print("Imported as module (this won't print)")

print()

# ============================================================================
# EXAMPLE 12: sys Module - System Access
# ============================================================================
# System-specific parameters

print("Example 12: sys Module")
print("-" * 50)

import sys

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Python executable: {sys.executable}")
print(f"Number of args: {len(sys.argv)}")
print()

# ============================================================================
# EXAMPLE 13: Standard Library - Statistics Module
# ============================================================================
# Statistical calculations

print("Example 13: Statistics Module")
print("-" * 50)

import statistics

scores = [85, 90, 78, 92, 88, 95, 82]

print(f"Scores: {scores}")
print(f"Mean: {statistics.mean(scores):.1f}")
print(f"Median: {statistics.median(scores):.1f}")
print(f"Mode: {statistics.mode(scores)}")
print(f"Stdev: {statistics.stdev(scores):.1f}")
print()

# ============================================================================
# EXAMPLE 14: Standard Library - String Module
# ============================================================================
# String utilities

print("Example 14: String Module")
print("-" * 50)

import string

print(f"ASCII digits: {string.digits}")
print(f"ASCII letters: {string.ascii_letters[:10]}...")
print(f"Punctuation: {string.punctuation}")
print()

# ============================================================================
# EXAMPLE 15: Standard Library - Itertools Module
# ============================================================================
# Advanced iteration

print("Example 15: Itertools Module")
print("-" * 50)

import itertools

# Combinations
items = ['a', 'b', 'c']
combos = list(itertools.combinations(items, 2))
print(f"Combinations of {items}: {combos}")

# Permutations
perms = list(itertools.permutations(['a', 'b'], 2))
print(f"Permutations: {perms}")

# Count
counter = itertools.count(start=10, step=2)
first_five = [next(counter) for _ in range(5)]
print(f"Count(10, 2): {first_five}")
print()

# ============================================================================
# EXAMPLE 16: Module Documentation - Docstrings
# ============================================================================
# Document modules and functions

print("Example 16: Docstrings")
print("-" * 50)

def documented_function(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b

print(f"Function: {documented_function.__name__}")
print(f"Docstring: {documented_function.__doc__[:40]}...")
print(f"Result: {documented_function(5, 3)}")
print()

# ============================================================================
# EXAMPLE 17: Module Directory Structure Understanding
# ============================================================================
# Understanding package structure

print("Example 17: Package Structure")
print("-" * 50)

# Simulate package structure
package_structure = """
my_app/
  __init__.py
  core.py
  utils.py
  models/
    __init__.py
    user.py
    product.py
  views/
    __init__.py
    dashboard.py
    settings.py
"""

print(package_structure)
print("This is a professional Python package")
print()

# ============================================================================
# EXAMPLE 18: Multiple Imports
# ============================================================================
# Import multiple items at once

print("Example 18: Multiple Imports")
print("-" * 50)

from math import pi, e, sqrt
from datetime import datetime, timedelta

print(f"π = {pi:.5f}")
print(f"e = {e:.5f}")
print(f"sqrt(100) = {sqrt(100)}")

now = datetime.now()
tomorrow = now + timedelta(days=1)
print(f"Now: {now.strftime('%Y-%m-%d')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print()

# ============================================================================
# EXAMPLE 19: Module Reloading
# ============================================================================
# Reload a module (for development)

print("Example 19: Module Reloading")
print("-" * 50)

import importlib
import math

# Get module info
print(f"Math module file: {math.__file__}")

# Reload (rarely needed)
importlib.reload(math)
print(f"Math module reloaded")
print()

# ============================================================================
# EXAMPLE 20: Inspect Module - Introspection
# ============================================================================
# Examine module contents

print("Example 20: Inspect Module")
print("-" * 50)

import inspect

# Get all functions in math module
math_functions = [name for name, obj in inspect.getmembers(math) 
                  if inspect.isbuiltin(obj)]
print(f"Math functions (first 5): {math_functions[:5]}")

# Get function signature
sqrt_sig = inspect.signature(math.sqrt)
print(f"sqrt signature: {sqrt_sig}")
print()

# ============================================================================
# EXAMPLE 21: Global Variables in Modules
# ============================================================================
# Module-level constants and variables

print("Example 21: Module-level Variables")
print("-" * 50)

# Simulate module constants
class SimulatedModule:
    VERSION = "1.0.0"
    AUTHOR = "Alice"
    DESCRIPTION = "A sample module"
    
    @staticmethod
    def get_info():
        return f"{SimulatedModule.DESCRIPTION} v{SimulatedModule.VERSION}"

module = SimulatedModule()
print(f"Version: {module.VERSION}")
print(f"Author: {module.AUTHOR}")
print(f"Info: {module.get_info()}")
print()

# ============================================================================
# EXAMPLE 22: Namespace Isolation
# ============================================================================
# Avoid name collisions with modules

print("Example 22: Namespace Isolation")
print("-" * 50)

# Import different modules with same function names
from datetime import datetime as dt1
import json

# Both have methods, but namespaced
print(f"datetime.now(): {dt1.now()}")
print(f"json module: {json.__name__}")

# No collision because they're in different namespaces
print("No name collision!")
print()

# ============================================================================
# EXAMPLE 23: Built-in Modules Available
# ============================================================================
# Some important built-in modules

print("Example 23: Built-in Modules Overview")
print("-" * 50)

modules = {
    "math": "Mathematical functions",
    "random": "Random number generation",
    "datetime": "Date and time",
    "json": "JSON parsing",
    "os": "Operating system",
    "sys": "System utilities",
    "re": "Regular expressions",
    "collections": "Specialized data structures",
    "itertools": "Advanced iteration",
    "functools": "Functional programming",
}

for name, desc in list(modules.items())[:5]:
    print(f"{name:15} - {desc}")

print(f"... and {len(modules) - 5} more")
print()

# ============================================================================
# EXAMPLE 24: Understanding Import Paths
# ============================================================================
# How Python searches for modules

print("Example 24: Import Search Path")
print("-" * 50)

import sys

print("Python search path for modules:")
for i, path in enumerate(sys.path[:3], 1):
    print(f"{i}. {path}")

print(f"... and {len(sys.path) - 3} more directories")
print()

# ============================================================================
# EXAMPLE 25: Professional Code Organization
# ============================================================================
# Best practices for organizing Python code

print("Example 25: Professional Organization")
print("-" * 50)

organization = """
PROFESSIONAL PYTHON PROJECT STRUCTURE:

project/
  ├── my_package/           ← Main code
  │   ├── __init__.py
  │   ├── core.py
  │   ├── utils.py
  │   └── models/
  │       ├── __init__.py
  │       └── user.py
  │
  ├── tests/                ← Test code
  │   ├── __init__.py
  │   └── test_core.py
  │
  ├── main.py               ← Entry point
  ├── setup.py              ← Installation config
  ├── requirements.txt      ← Dependencies
  ├── README.md             ← Documentation
  └── LICENSE               ← License

KEY PRACTICES:
✓ Use packages for organization
✓ Keep __init__.py files
✓ Separate code into logical modules
✓ Write setup.py for distribution
✓ Include requirements.txt
✓ Document with README.md
✓ Use tests/ directory for tests
✓ Include LICENSE file
"""

print(organization)

