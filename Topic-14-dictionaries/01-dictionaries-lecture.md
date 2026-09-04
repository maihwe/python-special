# Topic 14: Dictionaries - Working with Key-Value Collections

## Goal

**Learn to create and use dictionaries - collections that map keys to values. Understand dictionary operations, methods, nested dictionaries, and when dictionaries are better than lists. Master lookup and storage patterns.**

---

## Why This Matters - The Real Problem

Many real-world problems need fast lookup by name, not position:

- **Student records:** Find grade by student name
- **Phone book:** Look up number by name
- **Settings:** Store config by setting name
- **Inventory:** Check stock by product name
- **Scores:** Track points by player name
- **Translation:** Look up word in dictionary

With lists, you'd search:

**Without dictionaries (slow):**
```python
# Search through entire list
students = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]

name = "Bob"
for i in range(len(students)):
    if students[i] == name:
        print(grades[i])
```

**With dictionaries (instant):**
```python
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(grades["Bob"])  # Instant lookup
```

**Dictionaries are the foundation of data lookup and storage.**

---

## Mental Model 1: What Is a Dictionary? (The Mapping Model)

A **dictionary** maps **keys** to **values**.

```python
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
    keys: Alice, Bob, Charlie
    values: 85, 92, 78
```

**Key properties:**

1. **Key-value pairs:** Each key maps to exactly one value
2. **Unordered:** Items don't have positions (Python 3.7+: insertion order preserved)
3. **Mutable:** Can add/remove/change entries
4. **Keys must be unique:** No duplicate keys
5. **Values can repeat:** Different keys can have same value
6. **Fast lookup:** O(1) to find value by key

**Visual representation:**

```
Dictionary: {"Alice": 85, "Bob": 92, "Charlie": 78}

Lookup: grades["Bob"] → 92 (instant!)

Not positional like lists:
  - Can't access by position
  - Must access by key
```

**Difference from lists:**

```python
# List: access by position
grades_list = [85, 92, 78]
grades_list[1]  # 92 (what student?)

# Dictionary: access by key
grades_dict = {"Alice": 85, "Bob": 92, "Charlie": 78}
grades_dict["Bob"]  # 92 (directly find Bob)
```

---

## Mental Model 2: Creating Dictionaries (The Syntax Model)

**Create dictionaries multiple ways:**

```python
# Literal syntax (most common)
person = {"name": "Alice", "age": 30, "city": "New York"}

# Empty dictionary
empty = {}

# Using dict() constructor
person = dict(name="Alice", age=30, city="New York")

# From pairs
person = dict([("name", "Alice"), ("age", 30)])
```

**Key types:**

```python
# Keys can be strings
person = {"name": "Alice", "age": 30}

# Keys can be numbers
scores = {1: "first", 2: "second", 3: "third"}

# Keys can be mixed (but avoid)
mixed = {"name": "Alice", 1: "one", (1, 2): "tuple"}

# Keys must be immutable
valid = {1: "a", "b": "c", (1, 2): "d"}
invalid = {[1, 2]: "list"}  # ERROR! Lists aren't hashable
```

**Value types:**

```python
# Values can be anything
varied = {
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "list": [1, 2, 3],
    "dict": {"nested": "value"},
    "none": None
}
```

---

## Mental Model 3: Accessing and Modifying (The Access Model)

**Get values by key:**

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

name = person["name"]      # "Alice"
age = person["age"]        # 30
person["job"]  # ERROR! Key doesn't exist

# Safe access with get()
job = person.get("job")    # None (no error)
job = person.get("job", "unknown")  # "unknown" (default)
```

**Modify values:**

```python
person = {"name": "Alice", "age": 30}

# Change existing
person["age"] = 31

# Add new
person["city"] = "Boston"

# person is now {"name": "Alice", "age": 31, "city": "Boston"}
```

**Remove entries:**

```python
person = {"name": "Alice", "age": 30, "city": "Boston"}

# Remove by key
del person["age"]  # Removes age

# Remove with pop (returns value)
city = person.pop("city")  # city = "Boston", removed from dict

# Clear all
person.clear()  # {}
```

---

## Mental Model 4: Dictionary Methods (The Method Model)

**Core methods:**

```python
person = {"name": "Alice", "age": 30, "city": "Boston"}

# Get value (safe)
person.get("name")      # "Alice"
person.get("job", "none")  # "none" (default)

# Keys, values, items
person.keys()      # dict_keys(['name', 'age', 'city'])
person.values()    # dict_values(['Alice', 30, 'Boston'])
person.items()     # key-value pairs

# Check membership
"name" in person   # True
"job" in person    # False

# Remove
del person["age"]  # Remove by key
person.pop("city")  # Remove and return value
person.clear()      # Remove all
```

**Update entries:**

```python
person = {"name": "Alice", "age": 30}

# Update single
person["city"] = "Boston"

# Update multiple
person.update({"age": 31, "city": "Boston"})

# After: {"name": "Alice", "age": 31, "city": "Boston"}
```

---

## Mental Model 5: Iterating Over Dictionaries (The Iteration Model)

**Loop over keys:**

```python
person = {"name": "Alice", "age": 30, "city": "Boston"}

for key in person:
    print(key)
# Output: name, age, city

for key in person.keys():
    print(key)  # Same as above
```

**Loop over values:**

```python
for value in person.values():
    print(value)
# Output: Alice, 30, Boston
```

**Loop over key-value pairs:**

```python
for key, value in person.items():
    print(f"{key}: {value}")
# Output: name: Alice, age: 30, city: Boston
```

**Real-world pattern:**

```python
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Print all grades
for name, grade in grades.items():
    print(f"{name} scored {grade}")

# Find average
total = sum(grades.values())
average = total / len(grades)
```

---

## Mental Model 6: Nested Dictionaries (The Structure Model)

Dictionaries can contain dictionaries.

```python
students = {
    "Alice": {"grade": 9, "gpa": 3.9, "city": "Boston"},
    "Bob": {"grade": 10, "gpa": 3.7, "city": "NYC"},
    "Charlie": {"grade": 9, "gpa": 3.5, "city": "LA"}
}

# Access nested values
students["Alice"]["gpa"]  # 3.9
students["Bob"]["city"]  # "NYC"
```

**Real-world example:**

```python
# Product inventory
inventory = {
    "apple": {"price": 1.50, "quantity": 100, "category": "fruit"},
    "milk": {"price": 3.00, "quantity": 50, "category": "dairy"},
    "bread": {"price": 2.50, "quantity": 75, "category": "bakery"}
}

# Access product info
apple_price = inventory["apple"]["price"]  # 1.50

# Update inventory
inventory["apple"]["quantity"] -= 10
```

---

## Mental Model 7: Dictionary Comprehensions (The Compact Model)

Create dictionaries concisely.

```python
# Traditional
result = {}
for x in range(1, 4):
    result[x] = x ** 2

# Comprehension
result = {x: x**2 for x in range(1, 4)}
# {1: 1, 2: 4, 3: 9}
```

**With conditions:**

```python
# Only even keys
{x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Transform existing dictionary
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v*2 for k, v in original.items()}
# {"a": 2, "b": 4, "c": 6}
```

---

## Mental Model 8: When to Use Dict vs List (The Choice Model)

**Use lists when:**
- Items are ordered
- Access by position
- Similar items
- Examples: scores in order, student roster

```python
scores = [85, 92, 78, 95]
scores[0]  # Get first score
```

**Use dictionaries when:**
- Need name/label lookup
- Keys are meaningful
- Fast lookup important
- Examples: find grade by name, product by ID

```python
grades = {"Alice": 85, "Bob": 92}
grades["Alice"]  # Get Alice's grade (by name!)
```

**Real decision matrix:**

```
Access by position?
  Yes → List
  No → Dictionary

Access by name/key?
  Yes → Dictionary
  No → List

Need ordered results?
  Yes → List
  No → Dictionary (order not guaranteed)
```

---

## Mental Model 9: Common Patterns and Idioms (The Pattern Model)

**Pattern 1: Counting occurrences**

```python
text = "hello"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
# {"h": 1, "e": 1, "l": 2, "o": 1}
```

**Pattern 2: Group by category**

```python
students = [
    {"name": "Alice", "grade": 9},
    {"name": "Bob", "grade": 10},
    {"name": "Charlie", "grade": 9}
]

by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])
# {9: ["Alice", "Charlie"], 10: ["Bob"]}
```

**Pattern 3: Transform list to lookup**

```python
names = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]

lookup = {}
for name, grade in zip(names, grades):
    lookup[name] = grade
# {"Alice": 85, "Bob": 92, "Charlie": 78}
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "KeyError vs None"

**The question:** Why do I get KeyError when accessing missing key?

**The answer:** Dictionaries require key to exist. Use `.get()` for safe access.

```python
d = {"a": 1}
d["b"]  # KeyError: 'b'
d.get("b")  # None (safe)
d.get("b", 0)  # 0 (default)
```

### Confusion 2: "Keys Must Be Unique"

**The question:** What happens if I use same key twice?

**The answer:** Later value overwrites earlier.

```python
d = {"a": 1, "a": 2}
d  # {"a": 2} - second value wins
```

### Confusion 3: "Mutable Keys Won't Work"

**The question:** Can I use a list as key?

**The answer:** No - keys must be immutable (hashable).

```python
d = {[1, 2]: "value"}  # ERROR! Lists aren't hashable

# Use tuple instead
d = {(1, 2): "value"}  # OK
```

### Confusion 4: "Accessing Non-Existent Key"

**The question:** How do I safely check and access?

**The answer:** Use `in` operator or `.get()`.

```python
# Check first
if "key" in d:
    value = d["key"]

# Or use get()
value = d.get("key", default)
```

### Confusion 5: "Dictionary Order"

**The question:** What's the order of items?

**The answer:** Python 3.7+ preserves insertion order, but don't rely on order.

```python
d = {"b": 2, "a": 1, "c": 3}
list(d.keys())  # ["b", "a", "c"] (insertion order in 3.7+)
```

---

## How Dictionaries Work Internally (Implementation Model)

Dictionaries use **hash tables:**

```
Key lookup process:
1. Hash the key (convert to number)
2. Use hash to find bucket
3. Search bucket for key
4. Return value

Result: O(1) average lookup time
```

**Why immutable keys:**

```python
# Immutable: hash is stable
key = (1, 2)
hash(key)  # Same every time

# Mutable: hash would change
key = [1, 2]
hash(key)  # ERROR! Can't hash mutable
```

---

## Real-World Dictionaries (Practical Applications)

**User profiles:**

```python
user = {
    "id": 12345,
    "username": "alice_wonder",
    "email": "alice@example.com",
    "age": 28,
    "registered": "2023-01-15"
}
```

**Configuration:**

```python
config = {
    "debug": True,
    "host": "localhost",
    "port": 8000,
    "database": "myapp.db"
}
```

**Inventory lookup:**

```python
products = {
    "APPLE": {"price": 1.50, "stock": 100},
    "MILK": {"price": 3.00, "stock": 50},
    "BREAD": {"price": 2.50, "stock": 75}
}
```

---

## Summary - The Big Picture

**What you learned:**
1. Dictionaries map keys to values
2. Creating dictionaries
3. Accessing and modifying entries
4. Dictionary methods
5. Iterating with keys, values, items
6. Nested dictionaries
7. Dictionary comprehensions
8. When to use dict vs list
9. Common patterns

**Why this matters:**
- Most real-world data has labels/names
- Dictionaries enable fast lookup
- Fundamental data structure in programming
- Build complex data structures from dicts

**What's next:**
Now you have ordered (lists) and unordered (dicts) collections.

Topic 15 teaches **Tuples & Sets** - specialized collections for specific problems.

---

## What You Should Be Able To Do Now

✅ Create dictionaries with key-value pairs
✅ Access values by key safely
✅ Add, modify, and remove entries
✅ Use dictionary methods
✅ Iterate over keys, values, or items
✅ Work with nested dictionaries
✅ Use dictionary comprehensions
✅ Choose between lists and dictionaries
✅ Solve lookup and counting problems
✅ Build complex data structures

