# Topic 17: File I/O - Reading and Writing Files

## Goal

**Learn to read from and write to files - enabling programs to persist data across runs. Understand file modes, file operations, text vs binary, CSV/JSON handling, and best practices for robust file handling.**

---

## Why This Matters - The Real Problem

Without file I/O, programs lose all data when they stop:

**Without files (data is lost):**
```python
scores = []
scores.append(95)
scores.append(87)
# Program ends
# scores is gone forever!
```

**With files (data persists):**
```python
# Save scores
with open("scores.txt", "w") as f:
    for score in scores:
        f.write(f"{score}\n")

# Later, load scores back
scores = []
with open("scores.txt", "r") as f:
    for line in f:
        scores.append(int(line.strip()))
```

**File I/O enables:**
- Save game state
- Store configuration
- Log application events
- Process data files
- Build databases
- Exchange data with other programs

---

## Mental Model 1: Files as Sequences (The Stream Model)

A **file** is a sequence of data on disk that can be read or written.

```
File on disk: "hello\nworld\npython"
                ↓
            Read as stream
                ↓
        ["hello", "world", "python"]
```

**File operations:**

```python
# 1. Open file
f = open("data.txt", "r")  # Open for reading

# 2. Read/write data
content = f.read()  # Read all content

# 3. Close file
f.close()  # Save and close
```

**File pointer/cursor:**

```
File: "hello world"
      ↑
  Cursor at start

read(5) → "hello"
      ↑
  Cursor after "hello"

read(6) → " world"
      ↑
  Cursor at end
```

---

## Mental Model 2: File Modes (The Mode Model)

**File mode** determines what operations are allowed.

```python
"r"   # Read only (file must exist)
"w"   # Write only (creates or overwrites)
"a"   # Append (creates or appends)
"r+"  # Read and write
"w+"  # Read and write (creates or overwrites)
```

**Mode selection:**

```python
# Read existing file
with open("data.txt", "r") as f:
    content = f.read()

# Create/overwrite file
with open("data.txt", "w") as f:
    f.write("new data")

# Append to existing
with open("data.txt", "a") as f:
    f.write("more data")
```

**Text vs binary:**

```python
"r"   # Text read (strings)
"rb"  # Binary read (bytes)
"w"   # Text write (strings)
"wb"  # Binary write (bytes)
```

---

## Mental Model 3: Reading Files (The Read Model)

**Three ways to read:**

```python
# 1. Read all at once
f = open("data.txt", "r")
content = f.read()  # Entire file as string
f.close()

# 2. Read line by line
f = open("data.txt", "r")
lines = f.readlines()  # List of lines (with \n)
f.close()

# 3. Read one line
f = open("data.txt", "r")
line = f.readline()  # One line as string
f.close()
```

**Reading examples:**

```python
# File content:
# alice 85
# bob 92
# charlie 78

# Read all
with open("grades.txt", "r") as f:
    content = f.read()
# content = "alice 85\nbob 92\ncharlie 78"

# Read lines
with open("grades.txt", "r") as f:
    lines = f.readlines()
# lines = ["alice 85\n", "bob 92\n", "charlie 78"]

# Loop through lines
with open("grades.txt", "r") as f:
    for line in f:
        print(line.strip())
# Prints: alice 85, bob 92, charlie 78
```

---

## Mental Model 4: Writing and Appending (The Write Model)

**Write** creates new file or overwrites existing.

```python
with open("output.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
# File: "Line 1\nLine 2\n"
```

**Append** adds to end of existing file.

```python
# File exists: "Line 1\n"
with open("output.txt", "a") as f:
    f.write("Line 2\n")
# File: "Line 1\nLine 2\n"
```

**Write multiple items:**

```python
data = ["alice", "bob", "charlie"]
with open("names.txt", "w") as f:
    for name in data:
        f.write(f"{name}\n")
```

**Writelines (adds no newlines automatically):**

```python
lines = ["alice\n", "bob\n", "charlie\n"]
with open("names.txt", "w") as f:
    f.writelines(lines)
```

---

## Mental Model 5: Context Managers (The Safety Model)

**With statement** automatically closes files.

```python
# Safe: with statement
with open("data.txt", "r") as f:
    content = f.read()
# File automatically closed

# Risky: manual close
f = open("data.txt", "r")
content = f.read()
f.close()  # Easy to forget!
```

**Exception safety:**

```python
# If exception occurs, file still closes
with open("data.txt", "r") as f:
    content = f.read()
    # If error here, file still closes!

# Without with, file might stay open
f = open("data.txt", "r")
content = f.read()
if error:
    raise Exception()  # File not closed!
f.close()
```

---

## Mental Model 6: Processing Structured Data (The Structure Model)

**CSV (Comma-Separated Values):**

```python
# File content:
# name,age,city
# Alice,30,Boston
# Bob,25,NYC

import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['name', 'age', 'city'], ['Alice', '30', 'Boston'], ...
```

**JSON (JavaScript Object Notation):**

```python
# File content:
# {"name": "Alice", "age": 30, "city": "Boston"}

import json

with open("data.json", "r") as f:
    data = json.load(f)  # Converts to Python dict
    print(data["name"])  # Alice

# Write JSON
data = {"name": "Alice", "age": 30}
with open("output.json", "w") as f:
    json.dump(data, f)
```

---

## Mental Model 7: File Paths (The Location Model)

**Absolute vs relative paths:**

```python
# Absolute: full path from root
open("/home/user/data.txt", "r")
open("C:\\Users\\user\\data.txt", "r")  # Windows

# Relative: relative to current directory
open("data.txt", "r")          # Current directory
open("data/file.txt", "r")     # Subdirectory
open("../file.txt", "r")       # Parent directory
```

**Path operations:**

```python
import os

# Current directory
cwd = os.getcwd()

# Change directory
os.chdir("/path/to/dir")

# List files
files = os.listdir(".")

# Check if file exists
exists = os.path.exists("data.txt")

# Path joining
path = os.path.join("data", "file.txt")
```

---

## Mental Model 8: Reading and Parsing (The Parsing Model)

**Parse delimited data:**

```python
# File: "alice 85 90 95"
with open("grades.txt", "r") as f:
    line = f.readline()
    parts = line.split()
    name = parts[0]
    scores = [int(x) for x in parts[1:]]
```

**Parse structured text:**

```python
# File:
# [User]
# name: Alice
# age: 30

data = {}
with open("config.txt", "r") as f:
    for line in f:
        if ":" in line:
            key, value = line.split(":")
            data[key.strip()] = value.strip()
```

---

## Mental Model 9: Best Practices (The Quality Model)

**Always use with statement:**

```python
# Good
with open("file.txt", "r") as f:
    content = f.read()

# Bad - file might not close
f = open("file.txt", "r")
content = f.read()
f.close()
```

**Handle errors:**

```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except IOError as e:
    print(f"Error reading file: {e}")
```

**Check before overwriting:**

```python
import os

if os.path.exists("data.txt"):
    print("File exists, backing up...")
    os.rename("data.txt", "data.txt.bak")

with open("data.txt", "w") as f:
    f.write("new content")
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "r vs w vs a"

**The question:** When do I use each mode?

**The answer:**
- `r`: Read existing file
- `w`: Create new or overwrite completely
- `a`: Add to end without losing existing

```python
# Starts empty
with open("file.txt", "w") as f:
    f.write("Line 1\n")

# File has: "Line 1\n"

# Overwrites!
with open("file.txt", "w") as f:
    f.write("New\n")

# File has: "New\n" (old content gone!)

# Appends
with open("file.txt", "a") as f:
    f.write("Line 2\n")

# File has: "New\nLine 2\n"
```

### Confusion 2: "Forgetting to strip() newlines"

**The question:** Why do lines have \n at the end?

**The answer:** readline/readlines include newlines from file.

```python
with open("names.txt", "r") as f:
    for line in f:
        print(line)  # Prints with \n (extra blank line)
        # Output:
        # alice
        # 
        # bob
        #
        # charlie

# Better: strip newlines
with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())  # Removes \n
        # Output:
        # alice
        # bob
        # charlie
```

### Confusion 3: "Binary vs Text Mode"

**The question:** What's the difference?

**The answer:** Text mode auto-converts line endings, binary doesn't.

```python
# Text mode (usually what you want)
with open("file.txt", "r") as f:
    content = f.read()  # Returns string

# Binary mode (for images, executables, etc.)
with open("file.bin", "rb") as f:
    content = f.read()  # Returns bytes
```

### Confusion 4: "JSON vs CSV vs Text"

**The question:** Which format should I use?

**The answer:** Depends on data structure:
- Text: Simple line-based data
- CSV: Tabular data (spreadsheets)
- JSON: Hierarchical/nested data

```python
# Text file (simple)
# alice 85
# bob 92

# CSV file (tabular)
# name,grade
# alice,85
# bob,92

# JSON file (hierarchical)
# {
#   "students": [
#     {"name": "alice", "grade": 85},
#     {"name": "bob", "grade": 92}
#   ]
# }
```

### Confusion 5: "File Position/Cursor"

**The question:** Why can't I read again after reading?

**The answer:** File pointer moves as you read. Seek back to start.

```python
with open("data.txt", "r") as f:
    content = f.read()  # Pointer at end
    content = f.read()  # Returns empty string!

# Better: seek to start
with open("data.txt", "r") as f:
    content = f.read()
    f.seek(0)  # Go back to start
    content = f.read()  # Works now
```

---

## How File I/O Works Internally (Implementation Model)

**File operations flow:**

```
1. Open file
   ↓
   OS opens file descriptor
   Creates file object in Python
   Sets cursor to beginning

2. Read/write operations
   ↓
   Each operation moves cursor

3. Close file
   ↓
   Flushes buffers
   Closes OS file descriptor
```

---

## Real-World File I/O (Practical Applications)

**Save game state:**

```python
import json

game_state = {
    "level": 5,
    "score": 1000,
    "inventory": ["sword", "shield"]
}

with open("save.json", "w") as f:
    json.dump(game_state, f)
```

**Log events:**

```python
from datetime import datetime

with open("app.log", "a") as f:
    f.write(f"{datetime.now()}: User logged in\n")
    f.write(f"{datetime.now()}: User clicked button\n")
```

**Process data file:**

```python
import csv

with open("sales.csv", "r") as f:
    reader = csv.reader(f)
    total = 0
    for row in reader:
        total += float(row[2])  # Sum third column
```

---

## Summary - The Big Picture

**What you learned:**
1. File operations (open, read, write, close)
2. File modes (r, w, a, +)
3. Reading methods (read, readline, readlines)
4. Writing and appending
5. Context managers (with statement)
6. CSV and JSON handling
7. File paths and navigation
8. Parsing and processing
9. Best practices and safety

**Why this matters:**
- Programs can persist data
- Can work with real data files
- Foundation for databases
- Enable data processing pipelines
- Required for most real applications

**What's next:**
Now you can save/load data.

Topic 18 teaches **Error Handling** - how to handle failures gracefully.

---

## What You Should Be Able To Do Now

✅ Open files in different modes
✅ Read entire files or line by line
✅ Write and append to files
✅ Use with statement for safety
✅ Process CSV files
✅ Work with JSON data
✅ Navigate file system
✅ Handle file errors
✅ Parse and process file data
✅ Build data persistence into programs

