# Topic 2: Variables - Storing and Naming Data

## Goal

**Learn how to store data in variables. Understand that variables are labeled boxes holding values in memory.**

---

## Why This Matters

Topic 1 let you display static text. Real programs work with changing data.

**Without variables:**
```python
print(85 + 92 + 88) / 3)  # What does this mean? Forgotten.
```

**With variables:**
```python
midterm = 85
final = 92
project = 88
average = (midterm + final + project) / 3
print("Average:", average)  # Clear meaning
```

Variables let you:
- Store user input
- Store calculation results
- Reuse values multiple times
- Make code understandable

---

## Mental Model 1: The Filing Cabinet

Imagine your computer's memory as a filing cabinet:

```
┌─────────────────┐
│ FILE CABINET    │
├─────────────────┤
│ [Drawer A]      │  ← label: midterm
│ Midterm         │  ← content: 85
├─────────────────┤
│ [Drawer B]      │  ← label: final
│ Final           │  ← content: 92
├─────────────────┤
│ [Drawer C]      │  ← label: project
│ Project         │  ← content: 88
└─────────────────┘
```

When you write:
```python
midterm = 85
```

Python:
1. Creates a drawer
2. Labels it "midterm"
3. Puts 85 inside

When you use it:
```python
print(midterm)
```

Python:
1. Finds the drawer labeled "midterm"
2. Gets the value inside (85)
3. Uses it

---

## Mental Model 2: Memory - Where Variables Actually Live

Your computer has RAM with numbered locations:

```
Location 1000: [empty]
Location 1001: [empty]
Location 1002: 85        ← midterm
Location 1003: 92        ← final
Location 1004: 88        ← project
Location 1005: [empty]
```

When you create a variable:
```python
midterm = 85
```

Python:
1. Finds empty location (1002)
2. Stores 85 there
3. Records: "midterm" → 1002

When you use it:
```python
print(midterm)
```

Python:
1. Looks up: where is midterm? (1002)
2. Gets value there (85)
3. Uses it

---

## Mental Model 3: Variable Names Are Labels

The name is NOT the data. It's just a label.

```python
score = 85
points = 85
value = 85
```

All three store 85. The names are different, but data is identical.

**Good names make code readable:**
```python
midterm = 85  # Clear what this is
final = 92    # Clear what this is
```

**Bad names are confusing:**
```python
a = 85  # What is 'a'? Unknown
b = 92  # What is 'b'? Unknown
```

Variable names are for humans. The computer only cares about the value.

---

## Mental Model 4: Data Types

Variables store different kinds of data:

```python
score = 85           # Integer
gpa = 3.85          # Float
name = "Alice"      # String
is_passed = True    # Boolean
```

Python tracks both:
- The value (85)
- The type (integer)

Types behave differently:
```python
print(5 + 3)      # 8 (math)
print("5" + "3")  # "53" (text joining)
```

---

## Common Confusion Points

**"Why can't I use spaces in names?"**

```python
midterm score = 85  # WRONG
midterm_score = 85  # RIGHT
```

Use underscores instead of spaces.

**"Can variables change?"**

```python
age = 25
age = 26  # Yes, overwrites old value
```

Yes. That's why they're called "variables" (they vary).

**"What if I use a name twice?"**

```python
score = 85
score = 92  # Overwrites the old value
print(score)  # 92
```

The new value replaces the old one. The old value is lost.

**"Can I do math with variables?"**

```python
x = 5
y = 3
print(x + y)  # 8
```

Yes. Variables hold values, so they work in calculations.

---

## Summary

- Variables are labeled containers for data
- They live in your computer's memory
- Variable names are just labels for humans
- Values can change (that's why they're "variable")
- Different data types exist (numbers, text, true/false)

---

## What's Next

Now you can store data. But where does the data come from?

In Topic 3, you'll learn **input()** - how to ask users for data. Then your programs can work with any user's information, not just hardcoded values.

