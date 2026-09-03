# Topic 12: For Loops - Iterating Over Sequences

## Goal

**Learn to iterate over sequences using for loops. Understand how for loops differ from while loops, when to use each, the range() function, looping over strings and lists, loop variables, and nested for loops. Master sequence iteration.**

---

## Why This Matters - The Real Problem

Many programs need to process collections:

- **Process all items:** Analyze each number in a list
- **Transform data:** Apply operation to every element
- **Search:** Find specific item in collection
- **Aggregate:** Sum all values, find max, count items
- **Display:** Show each item formatted nicely
- **Build:** Create new data from existing data

Without for loops, you'd track indices manually:

**Without for loops (tedious):**
```python
numbers = [10, 20, 30, 40, 50]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

**With for loops (elegant):**
```python
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)
```

**For loops let you iterate elegantly over sequences.**

---

## Mental Model 1: What Is a For Loop? (The Sequence Model)

A **for loop** repeats for each item in a sequence.

```python
for variable in sequence:
    # Execute this for each item in sequence
    # variable holds current item
```

**Visual representation:**

```
        Start
          ↓
    Get next item from sequence
      /         \
  Item exists   No more items
     ↓               ↓
Execute           Exit loop
 code with        Continue
  item           program
     ↑               ↓
     └─ Loop back to get next
```

**Real example:**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

**Key difference from while:**

```python
# While: repeat WHILE condition is true
while count < 3:
    print(count)
    count += 1

# For: repeat FOR each item in sequence
for item in sequence:
    print(item)
```

---

## Mental Model 2: Range - Creating Sequences (The Range Model)

**range()** creates a sequence of numbers.

```python
range(stop)           # 0 to stop-1
range(start, stop)    # start to stop-1
range(start, stop, step)  # start to stop-1, by step
```

**Examples:**

```python
range(5)           # 0, 1, 2, 3, 4
range(2, 5)        # 2, 3, 4
range(0, 10, 2)    # 0, 2, 4, 6, 8
range(10, 0, -1)   # 10, 9, 8, 7, ..., 1
```

**Using range in for loops:**

```python
for i in range(3):
    print(i)
# Output: 0, 1, 2

for i in range(1, 4):
    print(i)
# Output: 1, 2, 3

for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
```

**Common patterns:**

```python
# Count up from 0
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Count from 1
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# Count down
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1

# Every other number
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

---

## Mental Model 3: Looping Over Strings (Character Iteration)

Strings are sequences of characters. For loops iterate over each character.

```python
for char in "hello":
    print(char)

# Output:
# h
# e
# l
# l
# o
```

**Real-world uses:**

```python
# Count character
text = "programming"
count = 0
for char in text:
    if char == "g":
        count += 1
print(f"'g' appears {count} times")

# Check if palindrome
word = "racecar"
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-(i+1)]:
        is_palindrome = False

# Build pattern
result = ""
for char in "abc":
    result += char * 2
print(result)  # "aabbcc"
```

---

## Mental Model 4: Looping Over Lists (Collection Iteration)

Lists are sequences of items. For loops iterate over each item.

```python
numbers = [10, 20, 30]
for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30
```

**Real-world uses:**

```python
# Sum all items
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print(total)  # 15

# Find maximum
max_val = None
for num in [45, 23, 89, 12]:
    if max_val is None or num > max_val:
        max_val = num
print(max_val)  # 89

# Process each item
for name in ["Alice", "Bob", "Charlie"]:
    print(f"Hello, {name}!")
```

---

## Mental Model 5: Index-Based Loops (When You Need Indices)

Sometimes you need the index AND the item. Use **enumerate()**.

```python
for index, item in enumerate(sequence):
    # index is 0, 1, 2, ...
    # item is the current element
```

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

**Alternative: Manual indexing**

```python
for i in range(len(fruits)):
    fruit = fruits[i]
    print(f"{i}: {fruit}")
```

**When to use each:**

```python
# Simple iteration (prefer this)
for item in list:
    process(item)

# Need index
for i, item in enumerate(list):
    process(item, i)

# Complex index logic (less common)
for i in range(len(list)):
    if some_condition(i):
        process(list[i])
```

---

## Mental Model 6: Nested For Loops (Loops Within Loops)

For loops can be nested for multi-dimensional processing.

```python
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
```

**Output:**
```
(0, 0)
(0, 1)
(1, 0)
(1, 1)
(2, 0)
(2, 1)
```

**Real-world uses:**

```python
# Grid/board processing
for row in range(3):
    for col in range(3):
        print("□", end=" ")
    print()  # New line

# Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
```

---

## Mental Model 7: Break and Continue in For Loops (Loop Control)

**break:** Exit for loop immediately.

```python
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        break
    print(num)

# Output: 1, 2
```

**continue:** Skip rest of iteration, go to next.

```python
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        continue
    print(num)

# Output: 1, 2, 4, 5
```

**Real-world uses:**

```python
# Find item and exit
target = "Charlie"
for name in ["Alice", "Bob", "Charlie", "Diana"]:
    if name == target:
        print("Found!")
        break

# Skip invalid items
for item in items:
    if not is_valid(item):
        continue
    process(item)
```

---

## Mental Model 8: List Comprehensions (Compact Iteration)

**List comprehensions** create new lists by processing existing ones.

```python
# Traditional for loop
result = []
for num in [1, 2, 3, 4]:
    result.append(num * 2)
# result: [2, 4, 6, 8]

# List comprehension (same result)
result = [num * 2 for num in [1, 2, 3, 4]]
# result: [2, 4, 6, 8]
```

**Syntax:**

```python
[expression for item in sequence]
[expression for item in sequence if condition]
```

**Examples:**

```python
# Square all numbers
[x**2 for x in [1, 2, 3, 4]]  # [1, 4, 9, 16]

# Filter even numbers
[x for x in [1, 2, 3, 4, 5] if x % 2 == 0]  # [2, 4]

# Convert to uppercase
[word.upper() for word in ["hello", "world"]]  # ["HELLO", "WORLD"]
```

---

## Mental Model 9: For vs While Loops (Choosing the Right One)

**Use for loops when:**
- Iterating over a sequence (list, string, range)
- You know how many iterations (range)
- Processing each item exactly once

**Use while loops when:**
- Repeating until a condition changes
- You don't know how many iterations
- Complex loop conditions

**Examples:**

```python
# For: Process known collection
for item in list:
    process(item)

# While: Repeat until condition
while user_input != "quit":
    user_input = input()

# For: Iterate known times
for i in range(10):
    do_something()

# While: Unknown iterations
while random_value > threshold:
    random_value = random.random()
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Off-by-one Errors with Range"

**The question:** Why doesn't `range(5)` include 5?

**The answer:** Range is like indexing - it goes from 0 to stop-1.

```python
range(5)  # 0, 1, 2, 3, 4 (not 5!)

# To include 5:
range(6)  # 0, 1, 2, 3, 4, 5
```

This matches list indexing: list[0] to list[4] for 5-item list.

### Confusion 2: "When Do I Use Enumerate vs Range?"

**The question:** Should I use `for i in range(len(list))` or `for item in list`?

**The answer:** Depends on what you need.

```python
# Just the item (preferred)
for item in list:
    print(item)

# Need index too
for i, item in enumerate(list):
    print(f"{i}: {item}")

# Complex index logic (rare)
for i in range(len(list)):
    if condition_on_index(i):
        process(list[i])
```

### Confusion 3: "Breaking a Nested Loop"

**The question:** Break only exits inner loop. How to exit both?

**The answer:** Use a flag or break after inner loop.

```python
# Wrong: break only exits inner
for i in range(3):
    for j in range(3):
        if condition:
            break  # Only exits inner loop

# Better: use flag
found = False
for i in range(3):
    for j in range(3):
        if condition:
            found = True
            break
    if found:
        break
```

### Confusion 4: "List Comprehension Syntax"

**The question:** What's the order of comprehension syntax?

**The answer:** `[expression for variable in sequence if condition]`

```python
# Right
[x * 2 for x in range(5)]

# Wrong (syntax reversed)
[for x in range(5) x * 2]  # Error!

# With condition
[x for x in range(5) if x > 2]
```

### Confusion 5: "Modifying List While Iterating"

**The question:** Can I modify a list while looping over it?

**The answer:** Risky - modifying changes what you're iterating over.

```python
# Dangerous
items = [1, 2, 3, 4, 5]
for item in items:
    if item == 3:
        items.remove(item)  # Skips items!

# Better: loop over copy or create new
items = [1, 2, 3, 4, 5]
for item in items[:]:  # Loop over copy
    if item == 3:
        items.remove(item)
```

---

## How For Loops Work Internally (Execution Model)

```
Step 1: GET sequence
Step 2: GET first item from sequence
Step 3: ASSIGN to loop variable
Step 4: EXECUTE loop body
Step 5: GET next item
Step 6: Go back to Step 3
Step 7: When no more items, EXIT loop
```

**Example execution:**

```python
for num in [10, 20, 30]:
    print(num)

# Step 1: Get sequence [10, 20, 30]
# Step 2-4: Get 10, assign to num, print 10
# Step 5-6: Get 20, assign to num, print 20
# Step 5-6: Get 30, assign to num, print 30
# Step 7: No more items, exit
```

---

## Real-World For Loops (Practical Applications)

**Data processing:**

```python
# Calculate average
grades = [85, 92, 78, 95, 88]
total = 0
for grade in grades:
    total += grade
average = total / len(grades)
```

**Search and transform:**

```python
# Find all names starting with 'A'
names = ["Alice", "Bob", "Andrew", "Diana"]
a_names = []
for name in names:
    if name.startswith("A"):
        a_names.append(name)

# Or with comprehension
a_names = [name for name in names if name.startswith("A")]
```

**Building UI:**

```python
# Create menu
options = ["Play", "Settings", "Quit"]
for i, option in enumerate(options, 1):
    print(f"{i}. {option}")
```

---

## Summary - The Big Picture

**What you learned:**
1. For loops iterate over sequences
2. range() creates numeric sequences
3. Looping over strings and lists
4. Enumerate for index + item
5. Nested for loops
6. Break and continue
7. List comprehensions
8. Choosing for vs while
9. Common patterns

**Why this matters:**
- Most programs process collections
- For loops are cleaner than while for sequences
- Patterns like list comprehension are powerful
- Understanding both loops enables any algorithm

**What's next:**
Now you can iterate over sequences.

Topic 13 teaches **Lists** - the most common sequence type, with more operations.

---

## What You Should Be Able To Do Now

✅ Write for loops that iterate over sequences
✅ Use range() to create numeric sequences
✅ Loop over strings and lists
✅ Use enumerate() when you need indices
✅ Nest for loops correctly
✅ Use break and continue in for loops
✅ Use list comprehensions
✅ Choose between for and while loops
✅ Solve real-world iteration problems
✅ Debug loop logic

