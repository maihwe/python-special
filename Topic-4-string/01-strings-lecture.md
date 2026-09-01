# Topic 4: Strings - Working With Text

## Goal

**Learn how to work with text data. Understand string indexing, slicing, methods, and formatting.**

---

## Why This Matters

Most programs work with text:
- User names, messages, labels
- File names, file contents
- Log messages, reports
- Anything humans read

You need to understand text manipulation.

---

## Mental Model 1: Strings as Sequences

A string is a sequence of characters arranged in order.

```python
text = "Python"
```

Each character has a position:

```
Position: 0  1  2  3  4  5
Char:     P  y  t  h  o  n
```

You can access each character by position (called "indexing").

---

## Mental Model 2: Indexing - Accessing Characters

Access individual characters by position:

```python
word = "Python"
print(word[0])  # P (first character)
print(word[1])  # y (second character)
print(word[5])  # n (last character)
```

**Important:** Counting starts at 0, not 1.

Negative indexing works backward:

```python
print(word[-1])  # n (last character)
print(word[-2])  # o (second to last)
```

---

## Mental Model 3: Slicing - Getting Substrings

Get a portion of a string:

```python
text = "Python"
print(text[0:3])   # "Pyt" (positions 0, 1, 2)
print(text[2:5])   # "tho" (positions 2, 3, 4)
print(text[:3])    # "Pyt" (from start to 3)
print(text[3:])    # "hon" (from 3 to end)
```

Slicing creates a new string. Original unchanged.

---

## Mental Model 4: String Methods

Strings have built-in methods:

```python
text = "hello"
text.upper()       # "HELLO"
text.capitalize()  # "Hello"
text.replace("l", "L")  # "heLLo"
```

Methods don't change the original string. They return a new string.

---

## Mental Model 5: String Operations

**Concatenation - joining strings:**
```python
first = "Hello"
second = "World"
result = first + " " + second  # "Hello World"
```

**Repetition - repeating strings:**
```python
dash = "-"
line = dash * 10  # "----------"
```

**Membership - checking if substring exists:**
```python
text = "Python"
"y" in text   # True
"x" in text   # False
```

---

## Common Confusion Points

**"Can I change a string character?"**

```python
text = "hello"
text[0] = "H"  # ERROR - strings are immutable
```

Strings cannot be changed. Create a new string instead.

**"How do I find text in a string?"**

```python
text = "Python"
position = text.find("tho")  # 2
```

**"How do I join many strings?"**

```python
words = ["Hello", "World", "Python"]
result = " ".join(words)  # "Hello World Python"
```

---

## Summary

- Strings are sequences of characters
- Access characters by index (position)
- Get substrings with slicing
- Use methods to transform
- Strings are immutable (can't change)

---

## What's Next

Strings are often text that came from `input()`. But what if the user typed a number and you need to do math?

Topic 5 covers **Type Conversion** - converting between text, numbers, and other types.

