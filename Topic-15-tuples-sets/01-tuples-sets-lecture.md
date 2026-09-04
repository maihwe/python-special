# Topic 15: Tuples and Sets - Specialized Collections

## Goal

**Learn to use tuples for immutable sequences and sets for unique unordered collections. Understand when each is appropriate, their operations, and how they solve specific problems that lists and dictionaries cannot.**

---

## Why This Matters - The Real Problem

Sometimes you need more specialized collections:

**Tuples solve:**
- **Immutable data:** Prevent accidental changes (function returns, dictionary keys)
- **Lightweight:** More memory efficient than lists
- **Hashable:** Can be dictionary keys or set members
- **Function returns:** Return multiple values naturally

**Sets solve:**
- **Unique items:** Automatically remove duplicates
- **Fast membership:** Check "is this item in collection?"
- **Set operations:** Find common items, differences
- **Deduplication:** Remove duplicates from lists

Without tuples:

```python
# Lists are mutable (risky for fixed data)
coordinates = [10, 20]
coordinates[0] = 999  # Oops, changed by accident!

# Can't use lists as dict keys
locations = {[10, 20]: "home"}  # ERROR! Lists aren't hashable
```

Without sets:

```python
# Lists allow duplicates (inefficient)
tags = ["python", "coding", "python", "programming", "python"]
# Duplicates wasted space

# Membership checking is slow on large lists
if "python" in tags:  # Searches entire list
```

**Tuples and sets solve these problems elegantly.**

---

## Mental Model 1: What Is a Tuple? (The Immutable Sequence Model)

A **tuple** is an immutable sequence - like a list that can't be changed.

```python
coordinates = (10, 20)
rgb = (255, 128, 0)
empty = ()
single = (42,)  # Note comma - required for single element
```

**Key properties:**

1. **Immutable:** Can't change after creation
2. **Ordered:** Items have positions
3. **Hashable:** Can be dictionary keys or set members
4. **Lightweight:** More efficient than lists
5. **Sequence:** Like lists, can index and slice

**Visual comparison:**

```
List:  [1, 2, 3]
       - Mutable
       - Can change
       - Can't hash

Tuple: (1, 2, 3)
       - Immutable
       - Fixed
       - Can hash
```

**Why immutability matters:**

```python
# List: mutable (risky)
data = [1, 2, 3]
data[0] = 999  # Changed!

# Tuple: immutable (safe)
data = (1, 2, 3)
data[0] = 999  # ERROR! Can't modify

# Use tuple for data you shouldn't change
COLOR = (255, 128, 0)  # Constant color
DIRECTIONS = ("north", "south", "east", "west")  # Fixed list
```

---

## Mental Model 2: Creating and Using Tuples (The Syntax Model)

**Create tuples:**

```python
# Literal syntax
coordinates = (10, 20)
colors = (255, 128, 0)
mixed = (1, "hello", 3.14, True)

# Empty tuple
empty = ()

# Single element (comma required!)
single = (42,)

# Without parentheses (implicit tuple)
point = 10, 20
point = 10, 20, 30

# Using tuple() constructor
t = tuple([1, 2, 3])  # (1, 2, 3)
t = tuple("abc")      # ('a', 'b', 'c')
```

**Access tuples (like lists):**

```python
t = (10, 20, 30, 40, 50)

t[0]      # 10 (first)
t[-1]     # 50 (last)
t[1:3]    # (20, 30)
len(t)    # 5
```

**Immutability:**

```python
t = (1, 2, 3)
t[0] = 99  # ERROR! Can't assign to tuple
t.append(4)  # ERROR! Tuples have no append
```

---

## Mental Model 3: Tuple Unpacking (The Decomposition Model)

**Unpacking** assigns tuple elements to variables.

```python
# Unpack tuple
x, y = (10, 20)
# x = 10, y = 20

# Unpack in loop
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"({x}, {y})")

# Multiple unpacking
a, b, c = (1, 2, 3)
# a = 1, b = 2, c = 3

# Swap with unpacking
a, b = b, a  # Swap without temp variable!
```

**Real-world uses:**

```python
# Function returns multiple values
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

# Dictionary items
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# Extract from list of tuples
students = [("Alice", 85), ("Bob", 92)]
for name, grade in students:
    print(f"{name}: {grade}")
```

---

## Mental Model 4: What Is a Set? (The Unique Collection Model)

A **set** is an unordered collection of unique items.

```python
colors = {"red", "green", "blue"}
numbers = {1, 2, 3, 4, 5}
empty = set()  # Note: {} creates dict, need set()
```

**Key properties:**

1. **Unique:** No duplicate items
2. **Unordered:** No positions
3. **Mutable:** Can add/remove items
4. **Hashable members:** Items must be hashable
5. **Fast membership:** Check if item exists in O(1)

**Visual representation:**

```
Set: {1, 2, 3}
- No duplicates
- No positions
- Super fast lookup

List: [1, 2, 3, 2, 1]
- Has duplicates
- Has positions
- Slower lookup
```

**Why sets matter:**

```python
# Removing duplicates
items = [1, 2, 2, 3, 3, 3, 4]
unique = set(items)  # {1, 2, 3, 4}

# Fast membership check
if "python" in large_set:  # O(1)
if "python" in large_list:  # O(n)
```

---

## Mental Model 5: Set Operations (The Math Model)

Sets support mathematical operations.

```python
a = {1, 2, 3}
b = {2, 3, 4}

# Union: all items from both
a | b  # {1, 2, 3, 4}
a.union(b)

# Intersection: common items
a & b  # {2, 3}
a.intersection(b)

# Difference: in a but not b
a - b  # {1}
a.difference(b)

# Symmetric difference: in a or b but not both
a ^ b  # {1, 4}
a.symmetric_difference(b)
```

**Real-world uses:**

```python
# Find common skills
alice_skills = {"Python", "Java", "SQL"}
bob_skills = {"Python", "JavaScript", "SQL"}
common = alice_skills & bob_skills
# {"Python", "SQL"}

# Find new skills to learn
all_skills = {"Python", "Java", "SQL", "JavaScript"}
alice_has = {"Python", "Java"}
alice_needs = all_skills - alice_has
# {"SQL", "JavaScript"}
```

---

## Mental Model 6: Set Methods (The Modification Model)

**Add and remove:**

```python
s = {1, 2, 3}

# Add single item
s.add(4)  # {1, 2, 3, 4}

# Add multiple
s.update([5, 6])  # {1, 2, 3, 4, 5, 6}

# Remove (error if not present)
s.remove(1)  # {2, 3, 4, 5, 6}

# Remove safely
s.discard(99)  # No error if not present

# Remove and return item
item = s.pop()  # Removes arbitrary item

# Clear all
s.clear()  # set()
```

**Check membership:**

```python
s = {1, 2, 3}

1 in s   # True
5 in s   # False
```

**Other operations:**

```python
s = {1, 2, 3}

len(s)  # 3
list(s)  # Convert to list
set([1, 1, 2, 2, 3])  # Remove duplicates
```

---

## Mental Model 7: Tuples as Dictionary Keys (The Hashability Model)

Only **immutable** objects can be dictionary keys.

```python
# Lists can't be keys (mutable)
d = {[1, 2]: "point"}  # ERROR!

# Tuples can be keys (immutable)
d = {(1, 2): "point"}  # OK
d[(1, 2)]  # "point"

# Real example: game board positions
board = {
    (0, 0): "empty",
    (0, 1): "pawn",
    (1, 0): "knight",
}

# Access by coordinate
board[(0, 1)]  # "pawn"
```

**Why:**

```python
# If keys were mutable, hash could change
key = [1, 2]
d = {key: "value"}
key[0] = 999  # Changed key!
# Now can't find "value" - broken!

# Tuples prevent this
key = (1, 2)
# Can't change, so hash stays same
```

---

## Mental Model 8: When to Use Each Collection (The Choice Model)

**Use lists when:**
- Need ordered sequence
- Will modify contents
- Index access important
- Allow duplicates

```python
scores = [85, 92, 78, 95]
scores[0]  # Access by position
scores.append(88)  # Modify
```

**Use tuples when:**
- Need immutable sequence
- Use as dictionary key
- Return multiple values
- Prevent accidental changes

```python
# Constant data
RGB = (255, 128, 0)

# Dictionary key
locations = {(0, 0): "home", (1, 1): "work"}

# Return multiple values
def get_coordinates():
    return (10, 20)

# Prevent changes
def process(data):  # User can't modify tuple
    pass
```

**Use dictionaries when:**
- Need key-value lookup
- Keys are meaningful
- Access by name/label

```python
person = {"name": "Alice", "age": 30}
person["name"]  # Access by key
```

**Use sets when:**
- Need unique items
- Fast membership check
- Set operations (union, intersection)
- Remove duplicates

```python
tags = {"python", "coding", "javascript"}
"python" in tags  # Fast check!

unique_items = set(items)  # Remove duplicates
```

---

## Mental Model 9: Common Patterns (The Pattern Model)

**Pattern 1: Remove duplicates**

```python
items = [1, 2, 2, 3, 3, 3]
unique = list(set(items))  # [1, 2, 3]
```

**Pattern 2: Find common elements**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
common = a & b  # {3, 4}
```

**Pattern 3: Multiple return values**

```python
def get_user():
    return ("Alice", 30, "Boston")

name, age, city = get_user()
```

**Pattern 4: Immutable constant**

```python
DIRECTIONS = ("N", "S", "E", "W")
COLORS = ("red", "green", "blue")
```

**Pattern 5: Board/grid positions**

```python
board = {
    (0, 0): "X",
    (0, 1): "O",
    (1, 0): "X",
}
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Single Element Tuple"

**The question:** Why does (42) not create a tuple?

**The answer:** Parentheses alone don't create tuples - need comma.

```python
(42)      # Just 42, not a tuple
(42,)     # Tuple with one element
(42, 43)  # Tuple with two elements
```

### Confusion 2: "Empty Set"

**The question:** Why can't I create set with {}?

**The answer:** {} creates dictionary, not set. Use set().

```python
{}           # Dict (empty)
set()        # Set (empty)
{1, 2, 3}    # Set (with items)
```

### Confusion 3: "Set Ordering"

**The question:** Why can't I access set items by position?

**The answer:** Sets are unordered - no positions.

```python
s = {1, 2, 3}
s[0]  # ERROR! Sets don't have positions
list(s)[0]  # Convert to list first
```

### Confusion 4: "Tuple Unpacking Wrong Count"

**The question:** What if tuple has different number of items?

**The answer:** Must match number of variables.

```python
x, y = (1, 2)  # OK
x, y = (1, 2, 3)  # ERROR! Too many values

# Can use * to catch extras
x, *rest = (1, 2, 3)
# x = 1, rest = [2, 3]
```

### Confusion 5: "Nested Tuples"

**The question:** How do tuples work when nested?

**The answer:** Tuples can contain anything, including other tuples.

```python
nested = ((1, 2), (3, 4), (5, 6))
nested[0]  # (1, 2)
nested[0][1]  # 2
```

---

## How Tuples and Sets Work Internally (Implementation Model)

**Tuples:**

```
Internal structure (immutable):
(1, 2, 3)
[1][2][3]  - Fixed positions

Immutability = No resize, no modify
Hashability = Can compute hash once
```

**Sets:**

```
Internal structure (hash table):
{1, 2, 3}

Fast lookup:
1. Hash item
2. Check bucket
3. O(1) result

Uniqueness enforced by hash table
```

---

## Real-World Tuples and Sets (Practical Applications)

**Tuples - GPS coordinates:**

```python
locations = [
    ("Boston", 42.36, -71.06),
    ("NYC", 40.71, -74.01),
    ("LA", 34.07, -118.24)
]

for city, lat, lon in locations:
    print(f"{city}: {lat}, {lon}")
```

**Sets - Unique users:**

```python
session_users = {"alice", "bob", "charlie"}
online_users = {"bob", "charlie", "diana"}

common = session_users & online_users
# {"bob", "charlie"}
```

**Tuples as keys - Game board:**

```python
board_state = {
    (0, 0): "pawn",
    (0, 1): "knight",
    (0, 2): "bishop",
}
```

---

## Summary - The Big Picture

**What you learned:**
1. Tuples are immutable sequences
2. Creating tuples and accessing items
3. Tuple unpacking
4. Sets are unique unordered collections
5. Set operations (union, intersection, difference)
6. Set methods (add, remove, pop)
7. Tuples as dictionary keys
8. When to use each collection
9. Common patterns

**Why this matters:**
- Tuples prevent accidental changes
- Sets remove duplicates and enable fast lookup
- Different collections solve different problems
- Together with lists/dicts, solve most data problems

**What's next:**
Now you know all four collection types.

Topic 16 teaches **Functions** - how to write reusable code.

---

## What You Should Be Able To Do Now

✅ Create tuples and access elements
✅ Unpack tuples into variables
✅ Use tuples as dictionary keys
✅ Create sets and add/remove items
✅ Use set operations (union, intersection, difference)
✅ Remove duplicates with sets
✅ Check membership efficiently
✅ Choose the right collection type
✅ Understand immutability and hashability
✅ Solve real-world collection problems

