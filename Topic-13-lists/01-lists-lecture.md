# Topic 13: Lists - Working with Ordered Collections

## Goal

**Learn to create and manipulate lists - the most fundamental Python collection. Understand list operations, methods, indexing, slicing, mutability, and how to solve real-world problems with lists. Master the data structure behind most programs.**

---

## Why This Matters - The Real Problem

Almost every program deals with multiple items:

- **Student records:** Store many student objects
- **Shopping cart:** Multiple items with quantities
- **Game boards:** Grid of cells
- **Sensor data:** Stream of measurements
- **Inventory:** Multiple products with stock
- **Results:** Collection of search results

Without lists, you'd need separate variables:

**Without lists (terrible):**
```python
student1 = "Alice"
student2 = "Bob"
student3 = "Charlie"
student4 = "Diana"
# Calculate average grade
grade1 = 85
grade2 = 92
grade3 = 78
grade4 = 95
avg = (grade1 + grade2 + grade3 + grade4) / 4
```

**With lists (elegant):**
```python
students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [85, 92, 78, 95]
avg = sum(grades) / len(grades)
```

**Lists are the foundation of data processing.**

---

## Mental Model 1: What Is a List? (The Container Model)

A **list** is an ordered collection of items.

```python
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
empty = []
```

**Key properties:**

1. **Ordered:** Items have positions (0, 1, 2, ...)
2. **Mutable:** Can change items after creation
3. **Indexed:** Access by position
4. **Heterogeneous:** Can mix types
5. **Dynamic:** Can grow/shrink

**Visual representation:**

```
List: [10, 20, 30, 40, 50]
Index: 0   1   2   3   4
```

**Difference from strings:**

```python
# Strings are immutable (can't change)
text = "hello"
text[0] = "H"  # ERROR!

# Lists are mutable (can change)
items = [1, 2, 3]
items[0] = 99  # OK! items = [99, 2, 3]
```

---

## Mental Model 2: Indexing and Access (The Position Model)

Access items by their **index** (position).

```python
list = [10, 20, 30, 40, 50]
list[0]   # 10 (first item)
list[1]   # 20 (second item)
list[4]   # 50 (fifth item)
list[-1]  # 50 (last item)
list[-2]  # 40 (second to last)
```

**Index diagram:**

```
        Forward indexing
[10,  20,  30,  40,  50]
  0    1    2    3    4

        Backward indexing
[10,  20,  30,  40,  50]
 -5   -4   -3   -2   -1
```

**Common operations:**

```python
items = ["apple", "banana", "cherry"]

# Get first
first = items[0]  # "apple"

# Get last
last = items[-1]  # "cherry"

# Change item
items[1] = "blueberry"  # ["apple", "blueberry", "cherry"]

# Get length
count = len(items)  # 3
```

---

## Mental Model 3: Slicing - Getting Subsequences (The Range Model)

**Slicing** gets a portion of a list.

```python
list[start:stop:step]
list[start:stop]      # Step defaults to 1
list[:stop]           # Start defaults to 0
list[start:]          # Stop defaults to end
list[:]               # Copy entire list
```

**Examples:**

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]     # [2, 3, 4]        (items 2-4, not including 5)
nums[:3]      # [0, 1, 2]        (first 3 items)
nums[7:]      # [7, 8, 9]        (from 7 to end)
nums[::2]     # [0, 2, 4, 6, 8]  (every other)
nums[::-1]    # [9, 8, 7, ..., 1, 0]  (reversed!)
nums[1:8:2]   # [1, 3, 5, 7]     (from 1-7, every other)
```

**Real-world uses:**

```python
# Get first 3
top_3 = scores[:3]

# Get last 3
bottom_3 = scores[-3:]

# Get middle
middle = scores[1:-1]

# Reverse list
reversed_list = scores[::-1]

# Every other
alternating = scores[::2]
```

---

## Mental Model 4: List Methods - Modifying Lists (The Mutation Model)

Lists have **methods** to modify themselves.

**Adding items:**

```python
items = [1, 2, 3]

# append: Add to end
items.append(4)  # [1, 2, 3, 4]

# extend: Add multiple items
items.extend([5, 6])  # [1, 2, 3, 4, 5, 6]

# insert: Add at position
items.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]
```

**Removing items:**

```python
items = [1, 2, 3, 4, 5]

# remove: Remove by value
items.remove(3)  # [1, 2, 4, 5]

# pop: Remove by index (returns item)
last = items.pop()  # last = 5, items = [1, 2, 4]
first = items.pop(0)  # first = 1, items = [2, 4]

# clear: Remove all
items.clear()  # []
```

**Reordering:**

```python
items = [3, 1, 4, 1, 5]

# sort: Alphabetical/numerical
items.sort()  # [1, 1, 3, 4, 5]

# reverse: Flip order
items.reverse()  # [5, 4, 3, 1, 1]
```

**Searching:**

```python
items = [1, 2, 3, 4, 5]

# count: How many?
count = items.count(3)  # 1

# index: What position?
pos = items.index(3)  # 2
```

---

## Mental Model 5: List Mutability and References (The Identity Model)

**Mutability:** Lists change in place, affecting all references.

```python
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)  # [1, 2, 3, 4] - CHANGED!
```

**Why it matters:**

```python
list1 = [1, 2, 3]
list2 = list1     # Both point to same list
list2[0] = 99
print(list1)      # [99, 2, 3] - affected!

# To make independent copy:
list2 = list1[:]  # Slice copy
list2 = list1.copy()  # copy() method
list2 = list(list1)   # Convert to list
```

**Reference vs copy:**

```python
original = [1, 2, 3]

# Reference (same object)
ref = original
ref[0] = 99  # Changes original

# Copy (new object)
copy = original.copy()
copy[0] = 99  # original unchanged
```

---

## Mental Model 6: Common Patterns and Idioms (The Pattern Model)

**Pattern 1: Building a list**

```python
result = []
for item in items:
    if condition(item):
        result.append(item)
```

**Pattern 2: Transform elements**

```python
result = []
for item in items:
    result.append(transform(item))
```

**Pattern 3: Find item**

```python
for item in items:
    if item == target:
        print("Found!")
        break
```

**Pattern 4: Safe pop**

```python
if items:
    item = items.pop()
else:
    print("Empty list")
```

**Pattern 5: Swap elements**

```python
list[i], list[j] = list[j], list[i]
```

---

## Mental Model 7: List Comprehensions Revisited (The Compact Model)

**List comprehensions** create new lists concisely.

```python
# Traditional
result = []
for x in items:
    if condition(x):
        result.append(transform(x))

# Comprehension
result = [transform(x) for x in items if condition(x)]
```

**Examples:**

```python
# Squares
[x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filter even
[x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Uppercase strings
[word.upper() for word in ["hello", "world"]]
# ["HELLO", "WORLD"]
```

---

## Mental Model 8: Nested Lists (The 2D Model)

Lists can contain lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0]      # [1, 2, 3]
matrix[0][1]   # 2
matrix[2][-1]  # 9
```

**Real-world use:**

```python
# Game board
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]

# Access cell
board[1][2]  # "O"

# Modify cell
board[0][0] = "O"
```

---

## Mental Model 9: List Methods Reference (The Method Model)

**Modifying:**
- `append(item)` - Add to end
- `extend(items)` - Add multiple
- `insert(i, item)` - Add at position
- `remove(item)` - Remove by value
- `pop()` - Remove from end
- `pop(i)` - Remove from position
- `clear()` - Remove all
- `sort()` - Sort in place
- `reverse()` - Reverse in place

**Searching:**
- `count(item)` - How many?
- `index(item)` - What position?

**Copying:**
- `copy()` - Shallow copy

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Index Out of Range"

**The question:** Why do I get "index out of range" error?

**The answer:** Trying to access index that doesn't exist.

```python
items = [1, 2, 3]
items[5]  # ERROR: index out of range (only 0-2 exist)

# Safe access:
if 0 <= index < len(items):
    value = items[index]
```

### Confusion 2: "Modifying List in Loop"

**The question:** Why does my list change unexpectedly when I modify during iteration?

**The answer:** Modifying while iterating causes skipped/duplicate items.

```python
# Dangerous
items = [1, 2, 3, 4, 5]
for item in items:
    if item == 3:
        items.remove(item)  # Skips next item!

# Better: Loop over copy
for item in items[:]:
    if item == 3:
        items.remove(item)
```

### Confusion 3: "append vs extend"

**The question:** What's the difference?

**The answer:**
- `append()` adds item as single element
- `extend()` adds each item from iterable

```python
items = [1, 2, 3]
items.append([4, 5])  # [1, 2, 3, [4, 5]]
items.extend([4, 5])  # [1, 2, 3, 4, 5]
```

### Confusion 4: "Slice Notation is Backwards"

**The question:** Why is `list[2:5]` not including 5?

**The answer:** Convention - start is inclusive, stop is exclusive.

```python
[0, 1, 2, 3, 4][2:5]  # [2, 3, 4] (not 5!)

# This makes slices consistent:
list[:n] + list[n:] == list  # Always true!
```

### Confusion 5: "List vs String"

**The question:** What's the difference?

**The answer:**
- Lists are mutable (changeable)
- Strings are immutable (fixed)

```python
items = [1, 2, 3]
items[0] = 99  # OK

text = "hello"
text[0] = "H"  # ERROR!
```

---

## How Lists Work Internally (Implementation Model)

Lists are **dynamic arrays:**

```
Internal structure:
[item0, item1, item2, item3, _, _, _]
                                ^
                            Extra capacity

When full:
list.append(item)
# Allocates larger array
# Copies all items
# Adds new item
```

**Time complexity:**
- Access `list[i]`: O(1) - instant
- Append: O(1) amortized
- Insert at middle: O(n) - shifts items
- Remove: O(n) - shifts items

---

## Real-World Lists (Practical Applications)

**Shopping cart:**

```python
cart = []
cart.append({"item": "Apple", "price": 1.50})
cart.append({"item": "Milk", "price": 3.00})
total = sum(item["price"] for item in cart)
```

**High scores:**

```python
scores = [100, 85, 92, 88]
scores.sort(reverse=True)  # Highest first
top_score = scores[0]
```

**Data analysis:**

```python
data = [23, 45, 12, 89, 34, 56]
average = sum(data) / len(data)
max_val = max(data)
min_val = min(data)
```

---

## Summary - The Big Picture

**What you learned:**
1. Lists are ordered, mutable collections
2. Indexing with positive and negative indices
3. Slicing to get subsequences
4. List methods (append, remove, sort, etc.)
5. Mutability and references
6. Common patterns and idioms
7. List comprehensions
8. Nested lists
9. Method reference

**Why this matters:**
- Lists are the most common data structure
- Almost every program uses lists
- Understanding lists enables data processing
- Proper use prevents subtle bugs

**What's next:**
Now you understand ordered collections.

Topic 14 teaches **Dictionaries** - key-value collections for lookup.

---

## What You Should Be Able To Do Now

✅ Create lists and access items by index
✅ Slice lists to get subsequences
✅ Add items with append/extend
✅ Remove items with remove/pop
✅ Sort and reverse lists
✅ Search for items
✅ Copy lists safely
✅ Understand mutability and references
✅ Use list comprehensions
✅ Work with nested lists

