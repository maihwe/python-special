# Topic 20: Modules - Organizing and Sharing Python Code

## Goal

**Learn to organize Python code into modules and packages. Understand imports, namespacing, and how to structure professional Python projects. Master the practices for writing reusable, shareable code.**

---

## Why This Matters - The Real Problem

Without modules, all code lives in one file:

**Without modules (one gigantic file):**
```python
# game.py - 5000 lines!

# Player code (500 lines)
class Player:
    pass

def player_attack():
    pass

def player_heal():
    pass

# Enemy code (500 lines)
class Enemy:
    pass

def enemy_attack():
    pass

# Game logic (500 lines)
def start_game():
    pass

def run_game_loop():
    pass

# Database code (500 lines)
def save_game():
    pass

def load_game():
    pass

# This is impossible to maintain!
```

**With modules (organized):**
```
game/
  __init__.py
  player.py      # Player class and functions
  enemy.py       # Enemy class and functions
  game.py        # Game loop logic
  database.py    # Save/load functions
  main.py        # Entry point

# In main.py:
from game.player import Player
from game.enemy import Enemy
from game import run_game
```

**Modules enable:**
- Organize large projects
- Reuse code across projects
- Share code with others
- Separate concerns
- Collaborate with teams
- Publish to Python Package Index
- Professional software structure

---

## Mental Model 1: What Is a Module? (The File Model)

A **module** is a Python file.

```
player.py  → module named "player"
  ↓
Can be imported:  from player import Player
```

**Module contains:**
```python
# player.py

class Player:
    pass

def attack():
    pass

MAX_HEALTH = 100
```

**Importing the module:**
```python
# main.py
import player

# Access module contents via dot notation
player.Player
player.attack()
player.MAX_HEALTH
```

**Module = one file:**
```
my_project/
  │
  ├── main.py         (module: main)
  ├── player.py       (module: player)
  ├── enemy.py        (module: enemy)
  └── database.py     (module: database)
```

---

## Mental Model 2: Importing (The Namespace Model)

**Import** loads code from a module into your namespace.

```python
# player.py
class Player:
    pass

# main.py
import player              # Load entire module
player.Player()            # Access via module.name

from player import Player  # Load specific item
Player()                   # Use directly

from player import *       # Load everything (avoid!)
```

**Namespace isolation:**

```python
# file1.py
def process():
    return "file1"

# file2.py
def process():
    return "file2"

# main.py
from file1 import process
print(process())  # "file1"

from file2 import process
print(process())  # "file2" (overwrites!)
```

**Better approach:**

```python
import file1
import file2

print(file1.process())  # "file1"
print(file2.process())  # "file2"
# No collision!
```

---

## Mental Model 3: The Import System (The Mechanism Model)

**When Python sees an import:**

```python
import player
```

**Python does:**
1. Look for file named player.py
2. Execute entire file
3. Create module object
4. Add module object to namespace

**Search path (in order):**
```
1. Current directory
2. PYTHONPATH directories
3. Standard library
4. Site-packages (installed libraries)
```

**Execution only once:**

```python
# player.py
print("Loading player module!")

class Player:
    pass

# main.py
import player  # Output: Loading player module!
import player  # No output (already loaded)
```

---

## Mental Model 4: Packages (The Hierarchy Model)

A **package** is a directory containing `__init__.py`.

```
game/                    (package)
  __init__.py
  player.py
  enemy.py
  combat/                (sub-package)
    __init__.py
    attacks.py
    spells.py
```

**Importing from packages:**

```python
from game.player import Player
from game.combat.spells import Fireball

# Hierarchy represents directory structure
```

**`__init__.py` makes it a package:**

```
game/
  __init__.py  ← Required for package
  player.py

Without __init__.py, Python doesn't recognize it as package
```

**What goes in `__init__.py`:**

```python
# game/__init__.py

# Initialize package
print("Loading game package")

# Expose useful items
from game.player import Player
from game.enemy import Enemy

# Define package-level variables
__version__ = "1.0.0"
__author__ = "Me"
```

---

## Mental Model 5: Standard Library (The Ecosystem Model)

Python ships with **standard library** - hundreds of built-in modules.

```python
import os              # Operating system
import sys             # System utilities
import math            # Math functions
import random          # Random numbers
import json            # JSON parsing
import datetime        # Date and time
import collections     # Data structures
import itertools       # Iteration tools
import functools       # Functional tools
import re              # Regular expressions
```

**Categories:**

```
Data:      json, csv, pickle, sqlite3
Strings:   re (regex), textwrap, string
Math:      math, random, statistics, decimal
Date/Time: datetime, time, calendar
Files:     os, shutil, pathlib, glob
Internet:  http, urllib, socket, email
```

---

## Mental Model 6: Avoiding Name Collisions (The Aliasing Model)

**Problem: Two modules with same name:**

```python
from player import Player    # Which player?
from database import Player  # Both have Player!
```

**Solution 1: Use full import:**

```python
import player
import database

player.Player()
database.Player()
```

**Solution 2: Use aliases:**

```python
from player import Player as PlayerClass
from database import Player as PlayerObject

PlayerClass()
PlayerObject()
```

**Solution 3: Import module with alias:**

```python
import player as p
import database as db

p.Player()
db.Player()
```

---

## Mental Model 7: Module Initialization (The Entry Point Model)

**`if __name__ == "__main__":`** runs only when executed directly.

```python
# calculator.py

def add(a, b):
    return a + b

# This runs when file is executed directly
if __name__ == "__main__":
    print(add(5, 3))

# This does NOT run when imported
```

**When executed directly:**

```bash
$ python calculator.py
8
```

**When imported:**

```python
from calculator import add
add(5, 3)  # No print output
```

**Why this matters:**

```python
# utils.py
def setup_database():
    print("Setting up database...")

if __name__ == "__main__":
    setup_database()  # Only runs if directly executed

# main.py
from utils import setup_database
# Database setup doesn't run automatically
setup_database()  # Must call explicitly
```

---

## Mental Model 8: Module Organization (The Structure Model)

**Professional Python project:**

```
my_project/
  ├── my_package/           # Main package
  │   ├── __init__.py
  │   ├── core.py
  │   ├── utils.py
  │   └── models/           # Sub-package
  │       ├── __init__.py
  │       ├── player.py
  │       └── enemy.py
  │
  ├── tests/                # Test code
  │   ├── __init__.py
  │   ├── test_core.py
  │   └── test_models.py
  │
  ├── main.py               # Entry point
  ├── setup.py              # Installation script
  ├── requirements.txt      # Dependencies
  ├── README.md             # Documentation
  └── LICENSE               # Legal
```

**Import structure:**

```python
# main.py
from my_package.models.player import Player
from my_package.core import run_game

# Imports follow directory hierarchy
```

---

## Mental Model 9: Distributing Code (The Publishing Model)

**From local file to reusable package:**

```
Local:     my_module.py in my project
  ↓
Package:   Structured as package with __init__.py
  ↓
Published: Upload to PyPI (Python Package Index)
  ↓
Installed: pip install my_module
  ↓
Imported:  import my_module (works anywhere!)
```

**Making code shareable:**

```
1. Organize into package
2. Write setup.py
3. Create README
4. Tag version
5. Upload to PyPI
6. Others: pip install your_package
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Import vs From Import"

**The question:** When do I use `import` vs `from ... import`?

**The answer:**
```python
# Use import when:
import os
os.path.exists("file.txt")  # Clear what module function is from

# Use from when:
from os.path import exists
exists("file.txt")  # Shorter, but less clear source

# Prefer import for clarity:
import datetime
datetime.datetime.now()  # Clear it's from datetime

# But from is OK for frequently used items:
from datetime import datetime
datetime.now()  # Still clear, less typing
```

### Confusion 2: "Why Is `__init__.py` Needed?"

**The question:** What does `__init__.py` do?

**The answer:**
```python
# Marks directory as package
game/
  __init__.py  ← Makes game a package

# Without it:
from game.player import Player  # Fails!

# With it:
from game.player import Player  # Works!

# Python 3.3+ can skip it (namespace packages)
# But best practice: always include it
```

### Confusion 3: "Circular Imports"

**The question:** Why does this fail?

**The answer:**
```python
# player.py
from enemy import Enemy  # Try to import enemy

class Player:
    pass

# enemy.py
from player import Player  # Try to import player

class Enemy:
    pass

# player imports enemy while enemy imports player
# CIRCULAR! Causes error
```

**Solution:**

```python
# player.py
class Player:
    pass

# enemy.py
class Enemy:
    pass

# main.py
from player import Player
from enemy import Enemy
# No circular dependency
```

### Confusion 4: "Relative vs Absolute Imports"

**The question:** What's the difference?

**The answer:**
```python
# Absolute import (preferred)
from game.player import Player
from game.enemy import Enemy

# Relative import (within package)
from . import player  # Current package
from ..models import Player  # Parent package

# Use absolute imports normally
# Use relative imports only within packages
```

### Confusion 5: "Module Not Found Error"

**The question:** Why can't Python find my module?

**The answer:**
```python
# module.py is in /home/user/project/
# But you're running from different directory

# Add to path before import:
import sys
sys.path.append("/home/user/project")
import module  # Now works

# Better: Run from correct directory
# Or use proper package structure
```

---

## How Imports Work Internally (Execution Model)

**When Python imports a module:**

```python
import player
```

**Step by step:**

```
1. Check if already in sys.modules
   └─ If yes: Use cached version

2. Search for player.py
   └─ Check current directory
   └─ Check PYTHONPATH
   └─ Check standard library
   └─ Check site-packages

3. Execute entire player.py file
   └─ Creates module object
   └─ Executes all top-level code
   └─ Populates module namespace

4. Return module object
   └─ Add to current namespace
   └─ Now "player" refers to module
```

---

## Real-World Module Organization (Practical Applications)

**Flask web application:**

```
my_app/
  app/
    __init__.py
    main.py          # Routes
    models.py        # Database models
    forms.py         # Form validation
  tests/
    __init__.py
    test_main.py
  run.py
  config.py
```

**Data science project:**

```
analysis/
  src/
    __init__.py
    data.py          # Loading data
    processing.py    # Cleaning data
    models.py        # ML models
    visualization.py # Plots
  notebooks/
    exploration.ipynb
  tests/
  main.py
```

---

## Summary - The Big Picture

**What you learned:**
1. Modules are Python files
2. Imports load code into namespace
3. Packages organize modules
4. Standard library provides built-ins
5. `__init__.py` marks packages
6. Name aliasing avoids collisions
7. `if __name__ == "__main__"` gates entry point
8. Project structure matters
9. Modules can be distributed

**Why this matters:**
- Organize large systems
- Share code professionally
- Use others' code
- Collaborate with teams
- Scale to production

**What's next:**
You've completed the entire Python curriculum!

---

## What You Should Be Able To Do Now

✅ Create and import modules
✅ Organize code into packages
✅ Use the standard library
✅ Avoid name collisions
✅ Structure professional projects
✅ Understand import mechanisms
✅ Use `if __name__ == "__main__"`
✅ Distribute Python packages
✅ Read and use others' modules
✅ Build scalable applications

