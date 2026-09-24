# Topic 8: Comparisons - Lecture Content

## Lecture 1: What Are Comparisons? (The Foundation)

### Opening Question
**Why can't we build real programs without comparisons?**

Think about any meaningful program you use:
- When you log in, the system asks: "Is the password correct?"
- When you make a purchase, the system asks: "Is there sufficient inventory?"
- When you play a game, the system asks: "Is the player's health zero?"

Without the ability to ask these yes/no questions, programs are just static text displays.

### The Core Concept

A **comparison** is a question about data that has exactly two possible answers: yes or no.

In Python:
- Yes = `True`
- No = `False`

```python
5 > 3           # Question: Is 5 greater than 3?
                # Answer: True (yes)

"apple" == "banana"  # Question: Are these equal?
                     # Answer: False (no)
```

### What Comparisons Return

Every comparison produces a **boolean** - a value that's either True or False.

```python
result = 5 > 3
print(result)           # True
print(type(result))     # <class 'bool'>
```

Boolean is a data type, just like int, float, and str.

```python
# Different data types
x = 5               # int
y = 5.5             # float
name = "Alice"      # str
is_adult = True     # bool ← This is what comparisons produce
```

### Structure of a Comparison

Every comparison has three parts:

```
[Left Value]  [Operator]  [Right Value]

5             >           3
```

- **Left Value:** The thing being compared
- **Operator:** The relationship being tested
- **Right Value:** What it's being compared to

```python
age >= 18
│    ││  │
│    ││  └─ Right: reference value (18)
│    │└──── Operator: greater than or equal
│    └───── Left: the thing being tested (age)
```

### Why This Matters

Comparisons enable decision-making:

```python
# Without comparison, you can't do this:
if age >= 18:
    print("You can vote")

# Without comparison, you can't do this:
if password == stored_password:
    print("Login successful")

# Without comparison, you can't do this:
while score < 100:
    print("Keep playing")
```

Comparisons are the gatekeepers of every decision your program makes.

---

## Lecture 2: Comparison Operators (The Tools)

### The Three Categories of Operators

Python provides operators for three different kinds of questions:

#### 1. Equality Questions: "Are they the same?"

```python
==      "Are they equal?"
!=      "Are they different?"
```

#### 2. Ordering Questions: "Which is bigger?"

```python
>       "Is left greater than right?"
<       "Is left less than right?"
>=      "Is left greater or equal?"
<=      "Is left less or equal?"
```

#### 3. Advanced Questions

```python
is      "Are they the same object?"
in      "Is this inside that?"
```

### Equality: Testing Sameness and Difference

#### The == Operator

```python
5 == 5              # True (same value)
5 == 3              # False (different values)
"hello" == "hello"  # True (exact match)
"hello" == "HELLO"  # False (case matters)
```

**Important:** == is comparison, not assignment.

The most common mistake in programming:

```python
x = 5       # Assignment (stores 5 in x)
x == 5      # Comparison (asks: is x equal to 5?)

if x = 5:           # ERROR: This assigns, not compares
if x == 5:          # CORRECT: This compares
```

#### The != Operator

```python
5 != 3              # True (they're different)
5 != 5              # False (they're the same)
"hello" != "world"  # True (different strings)
```

### Ordering: Testing Size Relationships

#### The > and < Operators (Strict)

These do NOT include equality.

```python
10 > 5      # True (10 is greater)
5 > 10      # False (5 is not greater)
5 > 5       # False (not greater - they're equal)
```

Think of them as strict inequalities.

```python
score = 80
if score > 80:
    print("Perfect!")  # Does NOT print (score equals 80, not greater)
```

#### The >= and <= Operators (Inclusive)

These DO include equality.

```python
10 >= 5     # True (10 is greater)
5 >= 5      # True (they're equal) ← Notice: this includes equality
5 >= 10     # False (5 is not ≥ 10)
```

This is the critical difference:

```python
score = 80

if score > 80:      # False (must be 81 or higher)
if score >= 80:     # True (80 or higher)
```

### Real-World Example: Age Thresholds

```python
age = 16

age > 18        # False - younger, not older
age < 18        # True - definitely younger
age >= 18       # False - not yet at threshold
age <= 18       # True - at or under threshold
```

Notice how >= and <= include the boundary, while > and < do not.

### Common Mistake: Confusing > and >=

```python
# For "at least 18"
if age > 18:        # WRONG: accepts 19, 20, 21... but NOT 18
if age >= 18:       # CORRECT: accepts 18, 19, 20...
```

**Memory aid:** The equals sign is inside the inequality.

```
>=  (the = is part of it)
<=  (the = is part of it)
```

---

## Lecture 3: Equality vs Identity (The Subtle Difference)

### Two Different Questions

**Equality (==):** "Do these values contain the same thing?"

**Identity (is):** "Are these the same object in memory?"

### Example: Two Dollar Bills

Imagine two $20 bills:

```
Bill A: $20
Bill B: $20

Same value? YES (==)
Same physical bill? NO (is)
```

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

list1 == list2      # True (same contents)
list1 is list2      # False (different objects)
```

### Example: Pointing to the Same Object

Now imagine one bill in two wallets:

```
Wallet A: points to Bill
Wallet B: points to Bill

Same value? YES (==)
Same physical bill? YES (is)
```

```python
list1 = [1, 2, 3]
list2 = list1       # list2 now points to the same list

list1 == list2      # True (same contents)
list1 is list2      # True (same object)

# Proof: change one, the other changes too
list1.append(4)
print(list2)        # [1, 2, 3, 4] - it changed!
```

### When to Use Each

**Use == (equality):** Almost always (99% of the time)

```python
# Comparing values
if password == stored_password:
    print("Correct")

# Checking numbers
if score == 100:
    print("Perfect")

# Comparing lists
if list1 == list2:
    print("Same contents")
```

**Use is (identity):** Only for special cases

The most important use is checking for None:

```python
value = None
if value is None:       # STANDARD way
    print("No value")

if value == None:       # Works but not Pythonic
    print("No value")
```

Why? Because None is a singleton (only one None exists in Python).

### The "is" Pitfall: Small Integer Caching

Python caches small integers for efficiency:

```python
a = 5
b = 5
a is b      # Usually True (same cached object)

a = 257
b = 257
a is b      # Usually False (large integers not cached)
```

This is why you shouldn't use `is` to compare integers. It's unreliable.

---

## Lecture 4: Comparison Chains (Elegant Range Testing)

### The Problem: Testing Ranges

You want to check if a value is between 1 and 10.

```python
# Traditional way
x = 5
if x > 1 and x < 10:
    print("In range")
```

This works but reads awkwardly. We repeat `x` twice.

### The Pythonic Solution: Comparison Chains

```python
if 1 < x < 10:
    print("In range")
```

This reads naturally, like mathematical notation.

### How Chains Work

When Python evaluates a chain, it checks each comparison:

```python
1 < x < 10

Step 1: Is 1 < x? (left to right)
Step 2: If yes, is x < 10?
Step 3: Combine with AND
```

Examples:

```python
x = 5
1 < 5 < 10      # True (1 < 5 is True AND 5 < 10 is True)

x = 15
1 < 15 < 10     # False (1 < 15 is True BUT 15 < 10 is False)

x = 0
1 < 0 < 10      # False (1 < 0 is False, so stop)
```

### Real-World: Grade Boundaries

```python
score = 85

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")      # Prints
elif 70 <= score < 80:
    print("C")
```

Notice:
- First range: 90 <= 100 (includes 90 and 100)
- Second range: 80 <= < 90 (includes 80, excludes 90)
- No overlap because the first uses <=, the second uses <

### Real-World: Age Groups

```python
age = 25

if 0 <= age < 13:
    print("Child")
elif 13 <= age < 18:
    print("Teen")
elif 18 <= age < 65:
    print("Adult")      # Prints
elif age >= 65:
    print("Senior")
```

### Why Chains Are Better

```python
# Without chains (verbose)
if 13 <= age and age < 18:
    print("Teen")

# With chains (Pythonic)
if 13 <= age < 18:
    print("Teen")
```

The chain version:
- Reads like mathematics
- Repeats the variable only once
- Makes intent clearer
- Is the standard in Python

---

## Lecture 5: Type Matters in Comparisons

### Comparing Numbers

Python treats integers and floats as comparable:

```python
5 == 5.0            # True (same numeric value)
5 < 10.5            # True (numeric comparison)
```

Even though they're different types:

```python
type(5)             # <class 'int'>
type(5.0)           # <class 'float'>
5 == 5.0            # True (values equal, types don't matter)
```

This is usually what you want:

```python
price = 19.99
if price == 20:     # Comparing float to int - works fine
    print("Free")
```

### Comparing Strings

Strings compare alphabetically (character by character):

```python
"apple" < "banana"      # True (a comes before b)
"apple" == "apple"      # True (exact match)
"apple" == "Apple"      # False (case matters)
```

### Case-Insensitive Comparison

When you need to ignore case:

```python
password1 = "MyPassword"
password2 = "mypassword"

password1 == password2              # False (case differs)
password1.lower() == password2.lower()  # True (ignoring case)
```

### Ordering Comparisons Require Compatible Types

Some comparisons fail:

```python
5 < "hello"         # TypeError: can't compare int and str
```

Why? Python doesn't know how to order numbers relative to strings.

Solution: Convert to the same type:

```python
str(5) < "hello"    # True ("5" < "h" alphabetically)
int("5") < 10       # True (5 < 10 numerically)
```

Note: Equality works across types:

```python
5 == "5"            # False (different types)
5 != "5"            # True (they're different)
```

---

## Lecture 6: String Comparisons Deep Dive

### Character-by-Character Comparison

Strings compare letter by letter, from left to right:

```python
"apple" < "banana"

Position 0: 'a' vs 'b'
'a' comes before 'b' alphabetically
Result: True (stop here)
```

### When Strings Are Prefixes

```python
"cat" < "catalog"

Position 0: 'c' == 'c' (same, continue)
Position 1: 'a' == 'a' (same, continue)
Position 2: 't' == 't' (same, continue)
Position 3: end vs 'a'

The shorter string comes first.
Result: True
```

### Case Matters: ASCII Order

Computers have a standard character ordering (ASCII):

```python
ord('A')  # 65
ord('a')  # 97

'A' < 'a'        # True (65 < 97)
"Apple" < "apple"  # True
```

All uppercase letters come before all lowercase letters.

```python
names = ["alice", "Bob", "charlie"]
names.sort()
# Result: ['Bob', 'alice', 'charlie']
# (Uppercase B comes first!)
```

For case-insensitive sorting:

```python
names.sort(key=str.lower)
# Result: ['alice', 'Bob', 'charlie']
```

---

## Lecture 7: Membership Testing with 'in' and 'not in'

### The Problem: Checking Collections

You have a list of valid options and need to check if something is in it:

```python
valid_responses = ["yes", "no", "maybe"]
user_response = "yes"

# Awkward way (don't do this)
if user_response == "yes" or user_response == "no" or user_response == "maybe":
    print("Valid")

# Elegant way (do this)
if user_response in valid_responses:
    print("Valid")
```

### The 'in' Operator

```python
value in collection
```

Tests if `value` exists in `collection`.

```python
# Lists
3 in [1, 2, 3, 4]               # True
5 in [1, 2, 3, 4]               # False

# Strings (substring search)
"a" in "hello"                  # True
"x" in "hello"                  # False

# Tuples
"apple" in ("apple", "banana")  # True
```

### The 'not in' Operator

```python
value not in collection
```

Tests if `value` does NOT exist.

```python
5 not in [1, 2, 3, 4]   # True
3 not in [1, 2, 3, 4]   # False
```

### Real-World: Validation

```python
# Check if username is forbidden
forbidden = ["admin", "root", "system"]
username = "john"

if username not in forbidden:
    print("Username available")  # Prints
```

### Real-World: Feature Flags

```python
# Check if feature is enabled
enabled_features = ["dark_mode", "beta_api"]
feature = "new_ui"

if feature in enabled_features:
    activate_feature()  # Does NOT execute
else:
    show_coming_soon()  # Executes
```

### Performance: Sets vs Lists

For large collections, use sets for membership testing:

```python
# List (slow for large data)
valid_ids = [1, 2, 3, ..., 1000000]
if user_id in valid_ids:        # Checks each item
    print("Valid")

# Set (fast for large data)
valid_ids = {1, 2, 3, ..., 1000000}
if user_id in valid_ids:        # Uses hash lookup
    print("Valid")
```

Sets are much faster for membership testing.

---

## Lecture 8: Common Mistakes and How to Avoid Them

### Mistake 1: Using = Instead of ==

```python
if x = 5:           # ERROR: This assigns
if x == 5:          # CORRECT: This compares
```

The equals sign appears twice in comparison: ==

### Mistake 2: Forgetting Equality in Range Checks

```python
score = 80

if score > 80:      # WRONG for "at least 80"
if score >= 80:     # CORRECT for "at least 80"
```

When you want to include the boundary, use >= or <=.

### Mistake 3: Comparing Incompatible Types

```python
5 < "hello"         # TypeError
```

Convert to same type first:

```python
str(5) < "hello"    # "5" < "hello"
```

### Mistake 4: Expecting Case-Sensitive Strings to Match

```python
"Hello" == "hello"  # False

# Solution:
"Hello".lower() == "hello".lower()  # True
```

### Mistake 5: Using 'is' for Value Comparison

```python
a = 5
b = 5
a is b              # Unreliable (depends on Python optimization)

# Use ==
a == b              # Reliable (True)
```

Use `is` only for None:

```python
if value is None:   # CORRECT
if value == None:   # Works but not Pythonic
```

### Mistake 6: Complex Comparison Chains

```python
if 1 < x > 5:       # Confusing - what does this mean?

# Better:
if 1 < x and x > 5:     # Clear
```

Keep chains simple and intuitive.

---

## Lecture 9: Putting It Together - Decision Making

### The Pattern

Comparisons enable decision-making:

```python
if [comparison]:
    [do something based on yes]
else:
    [do something based on no]
```

Example:

```python
age = 20
if age >= 18:
    print("Can vote")      # Prints
else:
    print("Too young")
```

### Multiple Conditions

```python
if [comparison1] and [comparison2]:
    [both must be true]

if [comparison1] or [comparison2]:
    [at least one must be true]
```

Example:

```python
age = 25
is_citizen = True

if age >= 18 and is_citizen:
    print("Can vote")      # Prints (both conditions true)
else:
    print("Cannot vote")
```

### Validating Input

```python
password = "MyPass123"

if len(password) >= 8 and any(c.isupper() for c in password):
    print("Password valid")
else:
    print("Password invalid")
```

---

## Lecture 10: Best Practices

### 1. Use Named Constants for Boundaries

```python
VOTING_AGE = 18
LEGAL_DRINKING_AGE = 21

if age >= VOTING_AGE:
    print("Can vote")

if age >= LEGAL_DRINKING_AGE:
    print("Can drink")
```

This makes code maintainable if boundaries change.

### 2. Use Comparison Chains for Ranges

```python
# Good
if 1 <= x <= 10:
    print("In range")

# Avoid
if x > 1 and x < 10:
    print("In range")
```

Chains are more Pythonic and readable.

### 3. Use 'in' for Collection Membership

```python
# Good
if username in valid_users:
    print("Valid")

# Avoid
if username == "alice" or username == "bob" or username == "charlie":
    print("Valid")
```

The `in` operator is cleaner and faster.

### 4. Use isinstance() for Type Checking

```python
# Good
if isinstance(value, int):
    print("It's an integer")

# Avoid
if type(value) == int:
    print("It's an integer")
```

`isinstance()` handles inheritance correctly.

### 5. Use 'is None' for None Checking

```python
# Good
if value is None:
    print("No value")

# Avoid
if value == None:
    print("No value")
```

This is the Python convention.

---

## Summary

Comparisons are:
- **Questions** about data relationships
- **Fundamental** to all decision-making
- **Composed of:** left value, operator, right value
- **Return:** True or False

Operators:
- **Equality:** ==, !=
- **Ordering:** <, >, <=, >=
- **Identity:** is, is not
- **Membership:** in, not in

Master comparisons, and decision-making becomes natural.