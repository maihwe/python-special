# Topic 4: Data Types - Understanding Python's Type System

## Goal

**Learn what data types are and why they exist. Understand Python's basic types: integers, floats, strings, booleans, and None. Master the concept that different data requires different representation and operations. Recognize how to choose the right type for the right job.**

---

## Why This Matters - The Real Problem

You've worked with numbers and text, but never formally asked: **Why are they different?**

The answer is fundamental to programming:
- **Different data needs different treatment**
- **Different types enable different operations**
- **Choosing the right type prevents bugs**
- **Understanding types makes you a better programmer**

Without understanding types, you'll:
- Make mistakes like trying to add text and numbers
- Choose wrong types for problems
- Misunderstand error messages
- Write inefficient code
- Create bugs that are hard to trace

Understanding types is like understanding ingredients in cooking:
- Flour, salt, sugar, water are all different
- Each has properties and uses
- You can't substitute randomly
- The right ingredients make good results

Python types are the same way.

---

## Mental Model 1: What Is a Data Type? (The Classification Model)

A data type is a **classification of data**.

Every value in Python has a type that defines:
1. **How it's stored** (internal representation)
2. **What operations are allowed** (what you can do with it)
3. **How much memory it uses**
4. **What values it can hold**

```python
42          # Type: int (integer)
3.14        # Type: float (floating-point)
"hello"     # Type: str (string)
True        # Type: bool (boolean)
None        # Type: NoneType (nothing)
```

Each type has:
- **A name** (int, float, str, bool, NoneType)
- **Allowed operations** (math, text, comparison, etc.)
- **A range of values** (int can be very large, bool only True/False)
- **Internal storage** (how Python represents it in memory)

**Why types exist:**

Without types, Python wouldn't know:
```python
5 + 3       # Is this math (8) or text concatenation ("53")?
"5" + "3"   # Is this math or text ("53")?
```

Types make it explicit.

---

## Mental Model 2: The Basic Types Landscape (Type Overview)

Python has several basic types. Here are the most important:

```
┌─────────────────────────────────────────┐
│         PYTHON DATA TYPES               │
├─────────────────────────────────────────┤
│                                         │
│  NUMERIC TYPES                          │
│  ├─ int        42, -5, 0               │
│  └─ float      3.14, -2.5, 0.0        │
│                                         │
│  TEXT TYPE                              │
│  └─ str        "hello", 'world'        │
│                                         │
│  BOOLEAN TYPE                           │
│  └─ bool       True, False              │
│                                         │
│  SPECIAL TYPE                           │
│  └─ NoneType   None                     │
│                                         │
│  SEQUENCE TYPES (covered later)         │
│  ├─ list       [1, 2, 3]               │
│  ├─ tuple      (1, 2, 3)               │
│  └─ str        (also sequence)          │
│                                         │
│  MAPPING TYPE (covered later)           │
│  └─ dict       {"key": "value"}        │
│                                         │
└─────────────────────────────────────────┘
```

For now, focus on the basic types: **int, float, str, bool, None**.

---

## Mental Model 3: Integers - Whole Numbers (Int Type)

**Integer** (int) represents **whole numbers** with no decimal point.

```python
42          # positive integer
-5          # negative integer
0           # zero
1_000_000   # large number (underscores for readability)
```

**Properties of integers:**
- No decimal point
- Can be positive, negative, or zero
- Can be very large (Python has no limit)
- Operations: +, -, *, //, %, **
- Exact representation (no rounding errors)

**What you can do with integers:**

```python
# Math
5 + 3         # 8
10 - 4        # 6
3 * 4         # 12
10 // 3       # 3 (integer division)
10 % 3        # 1 (remainder)
2 ** 3        # 8 (exponent)

# Comparison
5 > 3         # True
5 == 5        # True
```

**When to use integers:**
- Ages (people are whole numbers old)
- Counts (items, votes, people)
- IDs (user IDs, product IDs)
- Years
- Scores
- Anything that's a whole number

**Memory representation:**
```
Integer 42 in memory:
Binary: 00101010 (8 bits shown, actually more)
Storage: Typically 28-32 bytes in Python
```

---

## Mental Model 4: Floats - Decimal Numbers (Float Type)

**Float** (floating-point) represents **numbers with decimals**.

```python
3.14        # pi
-2.5        # negative decimal
0.0         # zero with decimal
1.0         # whole number as float
1e-5        # scientific notation (0.00001)
```

**Properties of floats:**
- Has decimal point
- Can represent very large and very small numbers
- Uses scientific notation for extremes
- **Approximate** (rounding errors possible)
- Operations: +, -, *, /, //, %, **

**What you can do with floats:**

```python
# Math
3.14 + 2.5    # 5.64
10.0 - 3.5    # 6.5
2.5 * 4.0     # 10.0
10.5 / 3.0    # 3.5

# Comparison
3.14 > 3.0    # True
```

**When to use floats:**
- Prices (dollars and cents)
- Measurements (height, weight, distance)
- Temperatures
- Percentages
- Any calculation with decimals
- Scientific data

**Important: Precision Issues**

```python
0.1 + 0.2           # 0.30000000000000004 (not exactly 0.3!)
# This is a known issue in computer science, not Python's fault
```

---

## Mental Model 5: Strings - Text Data (Str Type)

**String** (str) represents **text** - any sequence of characters.

```python
"hello"           # text in double quotes
'world'           # text in single quotes
"123"             # text that looks like numbers
""                # empty string
"hello world"     # text with spaces
```

**Properties of strings:**
- Enclosed in quotes (' or " or ''')
- Immutable (can't change in place)
- Sequence (has positions, can index)
- Can contain any character

**What you can do with strings:**

```python
# Concatenation (joining)
"hello" + " " + "world"   # "hello world"

# Repetition
"ha" * 3                   # "hahaha"

# Indexing (access character)
"hello"[0]                 # "h"
"hello"[4]                 # "o"

# Slicing (extract portion)
"hello"[1:4]              # "ell"

# Methods (operations)
"hello".upper()           # "HELLO"
"hello".replace("l", "L") # "heLLo"

# Comparison
"apple" < "banana"        # True (alphabetical)
"hello" == "hello"        # True
```

**When to use strings:**
- Names
- Addresses
- Messages
- Usernames
- File paths
- URLs
- Anything textual

---

## Mental Model 6: Booleans - True/False (Bool Type)

**Boolean** (bool) represents **true or false** - yes or no.

```python
True        # boolean true
False       # boolean false
```

**Properties of booleans:**
- Only two possible values: True or False
- Result of comparisons
- Used in conditions
- Result of logical operations

**What you can do with booleans:**

```python
# Comparisons produce booleans
5 > 3           # True
5 == 3          # False
"apple" in "apple pie"  # True

# Logical operations on booleans
True and False  # False
True or False   # True
not True        # False

# Use in conditions
if True:
    print("yes")
```

**When to use booleans:**
- Flags (is_active, is_logged_in, is_student)
- Results of tests (is it valid? is it found?)
- Conditions in if/else
- Decision making

---

## Mental Model 7: None - The Absence of Value (NoneType)

**None** is a special type representing **"nothing"** or **"absence of value"**.

```python
None        # represents nothing
```

**Properties of None:**
- Only one value: None
- Represents "no value"
- Default return value of functions that don't return anything
- Used for initialization (hasn't been set yet)

**What you use None for:**

```python
# Function with no return
def greet():
    print("hello")
result = greet()  # None (function doesn't return anything)

# Initialization (will be set later)
user_name = None
if condition:
    user_name = "Alice"

# Checking for no value
if value is None:
    print("No value set")
```

**When to use None:**
- Initial placeholder (hasn't been set yet)
- Function return when there's nothing to return
- Representing missing data
- Indicating absence

---

## Mental Model 8: Type Relationships (The Type System)

Types have relationships and can be converted between them.

```
Number Types:
┌──────────────────────┐
│     int              │
│    (whole)           │
│      ↔               │  ← Can convert
│   float              │
│  (decimal)           │
└──────────────────────┘
        ↕ Can convert to/from
       str (text)
        ↕ Can convert to/from
      bool (yes/no)
```

**Conversion rules:**

```python
int("42")           # ✓ "42" → 42
int("3.14")         # ✗ Error (has decimal)
float("3.14")       # ✓ "3.14" → 3.14
str(42)             # ✓ 42 → "42"
bool(0)             # ✓ 0 → False
bool(1)             # ✓ 1 → True
int(3.9)            # ✓ 3.9 → 3 (truncates)
float(42)           # ✓ 42 → 42.0
```

---

## Mental Model 9: Type Hierarchy and Relationships

Some operations work across multiple types:

**Numeric operations (int and float):**
```python
5 + 3         # 8 (int)
5.0 + 3       # 8.0 (float - promotes int to float)
5 + 3.0       # 8.0 (float)
```

**String operations (only strings):**
```python
"hello" + " world"    # "hello world"
"hello" + 5           # ERROR (can't mix)
```

**Comparisons (most types):**
```python
5 > 3          # True
3.14 > 3       # True
"apple" < "banana"  # True
5 == "5"       # False (different types)
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Why Can't I Add a String and a Number?"

**The question:** Why does "5" + 3 fail?

**The answer:** They're different types with different meanings.

```python
"5" + 3      # ERROR
# What does this mean?
# Is it: "53" (text concatenation)?
# Or: 8 (math)?
# Python can't know, so it requires explicit conversion
```

Solution:
```python
int("5") + 3       # 8 (math)
"5" + str(3)       # "53" (text)
```

### Confusion 2: "What's the Difference Between int(3.9) and 3.9?"

**The question:** If int(3.9) gives 3, why not use floats for everything?

**The answer:** Different types have different purposes and efficiency.

```python
int(3.9)    # 3 (loses decimal information)
3.9         # 3.9 (keeps precision)
```

Use:
- **int** for counts, indices, discrete values
- **float** for measurements, calculations with decimals

### Confusion 3: "Why Is True = 1 and False = 0?"

**The question:** Why do booleans have numeric values?

**The answer:** Historical reason from computer architecture.

```python
bool(0)     # False (zero = nothing)
bool(1)     # True (one = something)
```

But more importantly:
```python
True + True     # 2 (can do math with booleans)
True * 5        # 5
False + 5       # 5
```

This is rarely used; treat booleans as True/False, not 1/0.

### Confusion 4: "What Happens When I Mix Types?"

**The question:** If I do 5 + 3.0, what's the type?

**The answer:** Python **promotes** to the more general type (float).

```python
5 + 3         # 8 (int + int = int)
5 + 3.0       # 8.0 (int + float = float)
5.0 + 3.0     # 8.0 (float + float = float)
```

This is called **type promotion** - Python automatically converts to accommodate.

### Confusion 5: "Why Do Some Operations Give Different Results?"

**The question:** Why does 10 / 3 give 3.333... but 10 // 3 gives 3?

**The answer:** Different operators for different types of division.

```python
10 / 3        # 3.3333... (true division - always float)
10 // 3       # 3 (integer division - rounds down)
10 % 3        # 1 (modulo - remainder)
```

Choose based on what you need:
- Want decimal result? Use `/`
- Want whole number? Use `//`
- Want remainder? Use `%`

---

## Type System Design Philosophy

Why does Python have this type system?

1. **Clarity** - Different types clarify intent
2. **Safety** - Prevents certain mistakes
3. **Performance** - Each type optimized for its use
4. **Flexibility** - Can convert when needed
5. **Predictability** - Behavior is consistent

---

## Summary - The Big Picture

**What you learned:**
1. Data types classify data (int, float, str, bool, None)
2. Each type has specific operations and capabilities
3. Different types store data differently
4. Type choice affects what you can do
5. Types can be converted between each other
6. Python provides tools to work with types
7. Type errors come from using wrong operations

**Why this matters:**
- Understanding types prevents bugs
- Choosing right types makes code clearer
- Type conversion is essential skill
- Type mismatches are common errors
- Professional code respects types

**What's next:**
Now you understand the type landscape.

Topic 5 teaches **Strings** - deep dive into how to work with text data.

Topic 6 teaches **Type Conversion** - how to transform between types.

Topic 7 teaches **Arithmetic** - mathematical operations on numbers.

---

## What You Should Be Able To Do Now

✅ Name Python's basic data types
✅ Identify the type of a value
✅ Understand what operations each type supports
✅ Explain why different types exist
✅ Know when to use each type
✅ Convert between types (conceptually)
✅ Predict type results of operations
✅ Understand type promotion
✅ Recognize type errors
✅ Explain types to others

