# Topic 1: Hello World - Understanding Program Execution

## Goal

**Learn how to make a computer display output. Understand the execution flow: code → Python interpreter → output.**

---

## Why This Matters

You want to tell the computer to do something and see the result. The simplest result is displaying text.

This quest confirms:
- Python is installed
- Your setup works  
- Basic syntax is understood
- Programs execute line by line

---

## Mental Model 1: What Is a Program?

A program is a sequence of instructions the computer follows, one by one, in order.

```
Instruction 1: Display "Hello, World!"
Instruction 2: Stop
```

**Execution flow:**
1. Python reads line 1
2. Python understands it
3. Python executes it
4. Screen shows result
5. Python moves to line 2
6. Program ends

**Key insight:** Programs run top to bottom. One line at a time. No magic.

---

## Mental Model 2: The Execution Flow - What Actually Happens

When you run `python hello.py`:

```
Your file exists
    ↓
You type: python hello.py
    ↓
Python interpreter starts
    ↓
Python reads: print("Hello, World!")
    ↓
Python interprets: This is a print command
    ↓
Python executes: Send "Hello, World!" to output
    ↓
Operating system receives the command
    ↓
Your monitor displays: Hello, World!
    ↓
Python finishes
    ↓
Program ends
```

All of this happens in milliseconds. But conceptually, that's the flow.

---

## Mental Model 3: Strings - Text vs Code

The quotes are critical.

```python
print(Hello, World!)  # WRONG - Python looks for commands called Hello and World
print("Hello, World!")  # RIGHT - Python knows this is text
```

**The rule:** Text must be in quotes. Quotes tell Python: "This is literal text, not code."

Think of it as two languages:
- **Code:** `print`, `variable`, `+`
- **Text:** `"Hello, World!"` - everything inside quotes

Quotes are the boundary between code and text.

---

## Mental Model 4: Why `print()` Has Parentheses

`print()` is a **function**. Functions in Python use parentheses.

```python
print("Hello")      # Correct - has parentheses
print "Hello"       # Wrong - missing parentheses
```

This is syntax - the exact rule Python requires. Functions must have `()`.

You'll see this pattern everywhere:
```python
len("hello")
int("42")
input("Name: ")
```

All functions use parentheses.

---

## Mental Model 5: Output - How Programs Tell You Results

Without output, the computer does work but you never know:
- Did it work?
- What was the result?
- Was there an error?

`print()` solves this. It's how programs tell you what happened.

Every real program uses output:
- Games display score
- Calculators display result
- Weather app displays temperature
- Banking app displays balance

This quest teaches the most fundamental skill: making the computer talk to you.

---

## Common Confusion Points

**"Why do I need quotes?"**

Without quotes, Python thinks you're writing code:
```python
print(Hello)  # Python looks for a variable called Hello
```

With quotes, Python knows it's text:
```python
print("Hello")  # Python displays the text
```

**"Can I use single quotes?"**

```python
print('Hello')   # Works
print("Hello")   # Also works
```

Both are correct. Pick one style and stick with it.

**"What if the text has quotes?"**

```python
print('She said "Hello"')  # Double quotes inside single quotes
print("It's nice")        # Single quote inside double quotes
```

Or escape the quotes:
```python
print("She said \"Hello\"")  # Escaped double quotes
```

**"What if I want a new line?"**

```python
print("Line 1")
print("Line 2")  # Each print creates a new line

# Or use \n
print("Line 1\nLine 2")
```

---

## Summary

- Programs execute line by line
- `print()` displays output
- Strings must be in quotes
- Quotes tell Python: "This is text"
- This is the foundation for all programs

---

## What's Next

You can now display text. But real programs work with **data**.

In Topic 2, you'll learn **variables** - how to store information so your program can work with it. Then you can calculate things and display results.

