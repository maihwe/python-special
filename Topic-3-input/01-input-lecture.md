# Topic 3: Input - Making Programs Interactive

## Goal

**Learn how to ask the user for information using `input()`. Understand that input() always returns text.**

---

## Why This Matters

Topics 1-2 had hardcoded data. Real programs ask users for information.

**Without input:**
```python
age = 25  # Only works for this age
```

**With input:**
```python
age = input("How old are you? ")  # Works for any user
```

Input makes programs interactive and useful.

---

## Mental Model 1: The Pause and Wait

When your program calls `input()`, here's what happens:

```
Your program runs
    ↓
Reaches: age = input("How old are you? ")
    ↓
Python PAUSES execution
    ↓
Displays prompt: "How old are you? "
    ↓
Waits for user to type
    ↓
User types: 25
    ↓
User presses Enter
    ↓
Python captures: "25"
    ↓
Python RESUMES execution
    ↓
age now contains "25"
    ↓
Program continues
```

**Key:** Program stops and waits. Nothing happens until user types and presses Enter.

---

## Mental Model 2: input() Always Returns Text

This is the most confusing part.

**No matter what the user types, input() gives you TEXT:**

```python
age = input("Age: ")  # User types: 25
print(age)           # Displays: 25
print(type(age))     # Displays: <class 'str'>
                     # It's TEXT, not a number!
```

Even though the user typed a number, `input()` gives you a string.

---

## Mental Model 3: Text Cannot Do Math

Think about it:

```
The number 5:        5
The text "5":        "5"
```

Numbers can do math:
```python
5 + 3  # 8
```

Text cannot:
```python
"5" + "3"  # "53" (joining, not math)
"5" + 3    # ERROR!
```

`input()` gives text. Text doesn't do arithmetic.

---

## Mental Model 4: Type Conversion - Converting Text to Numbers

To use input as a number, convert it:

```python
age = input("Age: ")      # age is "25" (text)
age = int(age)            # age is now 25 (number)
print(age + 5)            # Works! Displays: 30
```

Or in one line:

```python
age = int(input("Age: "))  # Convert immediately
print(age + 5)             # Works
```

Python provides conversion functions:
- `int()` - Convert to whole number
- `float()` - Convert to decimal
- `str()` - Convert to text

---

## Common Confusion Points

**"Why does input() give text when I typed a number?"**

`input()` captures exactly what was typed - as text. It doesn't interpret. You must convert with `int()` or `float()`.

**"What if the user types something that's not a number?"**

```python
age = int(input("Age: "))  # User types "abc"
# CRASH - ValueError
```

The program crashes. Topic 17 teaches error handling.

**"Do I always need to convert?"**

Only for numbers. For text input, no conversion:

```python
name = input("Name: ")  # Already text
print("Hello, " + name)  # Works fine
```

**"Can I convert to other types?"**

Yes:

```python
price = float(input("Price: "))  # Decimal number
```

---

## Summary

- `input()` pauses and waits for user
- It always returns text
- Convert to numbers with `int()` or `float()`
- This enables interactive programs

---

## What's Next

You can now get data from users. But what if the data is text you need to work with?

In Topic 4, you'll learn **Strings** - how to manipulate and transform text data.

