# Topic 8: Comparisons - Testing Relationships Between Values

## Goal

**Learn how to compare values in Python. Master comparison operators that test equality, inequality, and ordering. Understand boolean results and how comparisons enable decision-making in programs.**

---

## Why This Matters - The Real Problem

Every meaningful program makes decisions based on conditions:

- **Login systems:** Is password correct? (comparison)
- **E-commerce:** Is item in stock? (comparison)
- **Games:** Is player health zero? (comparison)
- **Banking:** Is balance sufficient? (comparison)
- **Scientific computation:** Is result within tolerance? (comparison)
- **Data validation:** Is input valid? (comparison)

Without comparisons, programs can't respond to circumstances. They're just static.

**Comparisons are the gatekeepers of decision-making.**

They answer yes/no questions:
- Is this greater than that?
- Are these equal?
- Is this less than that?
- Is this not equal to that?

The answers drive everything that comes next.

---

## Mental Model 1: What Are Comparisons? (The Question Model)

A **comparison** is a question about two values that has a yes/no answer.

```python
5 > 3           # Question: Is 5 greater than 3?
                # Answer: Yes (True)

"apple" == "apple"  # Question: Are these equal?
                    # Answer: Yes (True)

10 < 5          # Question: Is 10 less than 5?
                # Answer: No (False)
```

Every comparison returns a **boolean** (True or False).

```python
result = 5 > 3
print(result)   # True
print(type(result))  # <class 'bool'>
```

Comparisons are **binary operations** - they need two values.

```python
5 > 3       # Two values (5 and 3), one operator (>)
x == y      # Two values (x and y), one operator (==)
```

---

## Mental Model 2: Comparison Operators (The Tool Model)

Python provides operators to test different relationships:

```python
>           # Greater than
<           # Less than
>=          # Greater than or equal
<=          # Less than or equal
==          # Equal to
!=          # Not equal to
is          # Identity (same object)
is not      # Not same object
in          # Membership (contains)
not in      # Not contains
```

**Each operator tests a specific relationship.**

---

## Mental Model 3: Equality Operators (Testing Same/Different)

**Equality (==):** Tests if two values are the same.

```python
5 == 5              # True (same value)
5 == 3              # False (different values)
"hello" == "hello"  # True
"hello" == "HELLO"  # False (case matters)
```

**Inequality (!=):** Tests if two values are different.

```python
5 != 3              # True (they're different)
5 != 5              # False (they're same)
"hello" != "world"  # True
```

**Critical: Use == to compare, not =**

```python
x = 5           # Assignment (stores 5 in x)
x == 5          # Comparison (tests if x equals 5)
```

Common mistake:
```python
if x = 5:           # ERROR: This is assignment
if x == 5:          # Correct: This is comparison
```

---

## Mental Model 4: Relational Operators (Testing Order)

**Greater than (>):** Left is larger than right.

```python
10 > 5          # True
5 > 10          # False
5 > 5           # False (not greater, equal)
```

**Less than (<):** Left is smaller than right.

```python
5 < 10          # True
10 < 5          # False
5 < 5           # False (not less, equal)
```

**Greater than or equal (>=):** Left is larger or equal.

```python
10 >= 5         # True
5 >= 5          # True (equal counts)
5 >= 10         # False
```

**Less than or equal (<=):** Left is smaller or equal.

```python
5 <= 10         # True
5 <= 5          # True (equal counts)
10 <= 5         # False
```

**Real-world use:**

```python
age = 16
is_adult = age >= 18        # False (not yet)

score = 90
is_passing = score >= 70    # True (passes)

temperature = 0
is_freezing = temperature <= 32  # True (in Fahrenheit)
```

---

## Mental Model 5: Comparing Different Types (Type Matters)

Comparisons work differently with different types.

**Comparing numbers:**

```python
5 == 5.0            # True (Python considers equal)
5 < 10              # True
3.14 > 3            # True
```

**Comparing strings:**

```python
"apple" == "apple"  # True (exact match)
"apple" == "Apple"  # False (case matters)
"apple" < "banana"  # True (alphabetical order)
```

**Comparing booleans:**

```python
True == True        # True
True == 1           # True (Python special case)
False == 0          # True (Python special case)
```

**Type mismatch in comparisons:**

```python
5 == "5"            # False (int ≠ str)
5 < "10"            # TypeError (can't compare)
```

**Important:** Most operators work across numeric types (int and float).

```python
5 == 5.0            # True (numeric equality)
5 >= 4.5            # True (numeric comparison)
```

---

## Mental Model 6: String Comparisons (Alphabetical Order)

Strings compare alphabetically (lexicographically).

```python
"apple" < "banana"      # True (a comes before b)
"zebra" > "apple"       # True (z comes after a)
"apple" < "application" # True (shorter comes first)
```

**Character-by-character comparison:**

```python
"cat" < "dog"    # True (c < d)
"cat" < "car"    # False (car < cat, r < t at position 2)
```

**Case matters:**

```python
"Apple" < "apple"   # True (uppercase < lowercase in ASCII)
```

**Real-world use:**

```python
name1 = "Alice"
name2 = "Bob"
is_sorted = name1 < name2  # True

password = "password123"
is_strong = len(password) >= 8  # True
```

---

## Mental Model 7: Identity vs Equality (is vs ==)

**Equality (==):** Tests if values are the same.

**Identity (is):** Tests if they're the same object in memory.

```python
x = [1, 2, 3]
y = [1, 2, 3]

x == y      # True (same contents)
x is y      # False (different objects)
x is x      # True (same object)
```

**Special case: Small integers and None**

```python
a = 5
b = 5
a is b      # Usually True (Python optimizes small integers)

a = 256
b = 256
a is b      # True (small integer caching)

a = 257
b = 257
a is b      # Usually False (Python doesn't cache large integers)
```

**When to use each:**

- **==**: Compare values (99% of the time)
- **is**: Compare identity (usually only for None)

```python
value = None
if value is None:       # Correct way
    print("No value")

if value == None:       # Works but not preferred
    print("No value")
```

---

## Mental Model 8: Membership Testing (in/not in)

**in:** Tests if value exists in a collection.

```python
3 in [1, 2, 3, 4]       # True
5 in [1, 2, 3, 4]       # False
"a" in "hello"          # True
"x" in "hello"          # False
```

**not in:** Tests if value doesn't exist.

```python
5 not in [1, 2, 3, 4]   # True
3 not in [1, 2, 3, 4]   # False
```

**Real-world use:**

```python
valid_responses = ["yes", "no", "maybe"]
response = "yes"
if response in valid_responses:
    print("Valid")

forbidden = ["admin", "root", "system"]
username = "john"
if username not in forbidden:
    print("Available")
```

---

## Mental Model 9: Comparison Chains (Multiple Comparisons)

Chain comparisons to test ranges.

```python
# Test if value is between 1 and 10
x = 5
if 1 < x < 10:  # Reads naturally: 1 < x AND x < 10
    print("In range")

# Same as:
if 1 < x and x < 10:  # More verbose
    print("In range")
```

**More examples:**

```python
# Age requirements
age = 25
if 18 <= age < 65:      # Working age
    print("Working age")

# Grade ranges
score = 85
if 80 <= score < 90:    # B grade
    print("B grade")

# Multiple conditions chained
if a < b <= c > d:      # a < b AND b <= c AND c > d
    print("All true")
```

**Avoid mixing incompatible types in chains:**

```python
if "apple" < x < 10:    # TypeError (can't compare str and int)
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Why Is == Different From =?"

**The question:** Can't I use = to compare?

**The answer:** = is assignment (stores a value). == is comparison (tests equality).

```python
x = 5       # Assignment: store 5 in x
x == 5      # Comparison: is x equal to 5?
```

Mixing them is a common error:

```python
if x = 5:           # ERROR: This assigns 5 to x
if x == 5:          # Correct: This tests equality
```

### Confusion 2: "Why Does 5 == 5.0 Return True?"

**The question:** Aren't int and float different types?

**The answer:** Python compares numeric values, not types.

```python
5 == 5.0            # True (same value)
type(5) == type(5.0)  # False (different types)
```

This is usually what you want:

```python
price = 19.99
if price == 20.0:   # Works, compares values
```

But if you need type equality:

```python
if type(price) == float:  # Tests the type specifically
```

### Confusion 3: "String Comparison Seems Random"

**The question:** Why is "Apple" < "apple"?

**The answer:** Strings compare by character codes (ASCII). Uppercase letters come before lowercase.

```python
ord("A")  # 65 (ASCII code for uppercase A)
ord("a")  # 97 (ASCII code for lowercase a)

"A" < "a"    # True (65 < 97)
"Apple" < "apple"  # True
```

For case-insensitive comparison:

```python
if "Apple".lower() == "apple":  # True
```

### Confusion 4: "Why Can't I Compare 5 < 'hello'?"

**The question:** Why does this error out?

**The answer:** Python doesn't know how to order numbers and strings together.

```python
5 < "hello"         # TypeError: can't compare int and str
5 == "5"            # False (different types, not error)
```

The == and != allow mixed types (returns False). But <, >, <=, >= need comparable types.

Solution: Convert to same type:

```python
str(5) < "hello"    # True (both strings)
int("5") < 10       # True (both integers)
```

### Confusion 5: "What's the Difference Between 'is None' and '== None'?"

**The question:** Do I need to use `is None` or can I use `== None`?

**The answer:** Both work, but `is None` is preferred.

```python
value = None
if value is None:   # Preferred
if value == None:   # Works but not preferred
```

Use `is` because:
- None is a singleton (only one None exists)
- `is` checks identity (more efficient)
- It's the Python convention

```python
if value is None:       # Pythonic
if value == None:       # Works but style issue
if not value:           # Too general (also matches 0, "", [], etc)
```

---

## How Comparisons Work Internally (Execution Model)

When Python evaluates `5 > 3`:

```
Step 1: PARSE
  Recognize: 5 > 3
  Identify: operator (>), left value (5), right value (3)

Step 2: EVALUATE LEFT
  Get value: 5

Step 3: EVALUATE RIGHT
  Get value: 3

Step 4: APPLY OPERATOR
  Is 5 > 3? Yes

Step 5: RETURN RESULT
  Return: True (a boolean)
```

With variables:

```python
x = 10
y = 7
result = x > y

Step 1: Look up x → 10
Step 2: Look up y → 7
Step 3: Apply > → 10 > 7 is true
Step 4: Return True
```

---

## Real-World Comparisons (Practical Applications)

**Login system:**

```python
username = "alice"
password = "secret"
stored_password = "secret"

if username == "alice" and password == stored_password:
    print("Login successful")
```

**Age verification:**

```python
age = 21
if age >= 21:
    print("You can vote")
```

**Temperature monitoring:**

```python
temperature = 45
if temperature > 100:
    print("Shutdown: overheating")
elif temperature > 80:
    print("Warning: running hot")
else:
    print("Normal")
```

**Range validation:**

```python
score = 85
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
```

**Inventory check:**

```python
stock = 5
min_threshold = 10
if stock < min_threshold:
    print("Reorder needed")
```

---

## Summary - The Big Picture

**What you learned:**
1. Comparisons test relationships between values
2. Comparison operators: ==, !=, <, >, <=, >=
3. Comparisons return boolean (True/False)
4. Type affects comparison behavior
5. String comparison is alphabetical
6. Identity (is) vs equality (==)
7. Membership testing (in/not in)
8. Comparison chains for ranges
9. Common pitfalls and solutions

**Why this matters:**
- Comparisons enable decision-making
- Almost every program makes choices
- Wrong comparisons cause subtle bugs
- Understanding types is essential
- Clarity prevents errors

**What's next:**
Now you can ask yes/no questions about data.

Topic 9 teaches **If/Else** - how to make decisions based on comparisons.

---

## What You Should Be Able To Do Now

✅ Use all comparison operators correctly
✅ Understand the difference between = and ==
✅ Compare numbers, strings, and other types
✅ Use identity comparison (is) appropriately
✅ Test membership (in/not in)
✅ Chain comparisons for ranges
✅ Predict boolean results of comparisons
✅ Handle type mismatches
✅ Write clear comparison expressions
✅ Debug comparison errors

