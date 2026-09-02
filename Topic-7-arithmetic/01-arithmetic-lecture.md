# Topic 7: Arithmetic - Mathematical Operations in Python

## Goal

**Learn how to perform mathematical operations in Python. Understand operators, order of operations, integer vs. float division, and how to use arithmetic in real programs. Master calculations that form the foundation of any data processing program.**

---

## Why This Matters - The Real Problem

Programming without arithmetic is like cooking without heat. You can't build anything real.

Real programs need arithmetic constantly:
- Financial calculations (prices, totals, taxes, discounts)
- Scientific computing (physics, chemistry, statistics)
- Game development (health, damage, scoring, physics)
- Data analysis (averages, percentages, trends)
- Machine learning (weights, gradients, predictions)
- Web development (pagination, rate limiting, metrics)

Without arithmetic, you're stuck displaying static text.

**Examples of arithmetic in action:**
- E-commerce: price × quantity + tax = total
- Games: player_health - damage = new_health
- Finance: principal × (1 + rate)^years = compound interest
- Statistics: sum(values) / count(values) = average
- Physics: distance = velocity × time

Arithmetic is the bridge from data to insights.

---

## Mental Model 1: What Are Operators? (The Tool Model)

An **operator** is a symbol that performs an operation on values.

```python
5 + 3       # + is the operator
x * y       # * is the operator
10 / 2      # / is the operator
```

Python has different operators for different purposes:
- **Arithmetic operators** - math operations
- **Comparison operators** - testing equality
- **Assignment operators** - storing values
- **Logical operators** - true/false logic

Focus on **arithmetic operators** first.

---

## Mental Model 2: Basic Arithmetic Operators (Core Operations)

Python provides operators for fundamental math:

```python
5 + 3       # Addition (5 plus 3)
5 - 3       # Subtraction (5 minus 3)
5 * 3       # Multiplication (5 times 3)
5 / 3       # Division (5 divided by 3)
5 // 3      # Integer division (5 divided by 3, no decimals)
5 % 3       # Modulo (remainder after division)
5 ** 3      # Exponent (5 to the power of 3)
-5          # Negation (opposite of 5)
+5          # Positive (emphasis, usually not needed)
```

**Let's understand each:**

**Addition (+):**
```python
5 + 3 = 8
x = 10
y = 20
total = x + y  # 30
```

**Subtraction (-):**
```python
10 - 3 = 7
height = 100
deduction = 25
remaining = height - deduction  # 75
```

**Multiplication (*):**
```python
5 * 3 = 15
price = 19.99
quantity = 3
total = price * quantity  # 59.97
```

**Division (/):**
```python
10 / 3 = 3.3333...  # Always produces float
# Even if result is whole:
10 / 2 = 5.0  # Still a float!
```

**Integer Division (//):**
```python
10 // 3 = 3  # Discards decimal part
10 // 2 = 5  # Still an int
10.5 // 3 = 3.0  # If operands are float, result is float
```

**Modulo (%):**
```python
10 % 3 = 1  # Remainder after division
# Useful for:
# - Check if divisible: if n % 2 == 0  (is even)
# - Wrapping: day_of_week = days % 7
# - Cycling through values
```

**Exponent (**):**
```python
5 ** 3 = 125  # 5 × 5 × 5
2 ** 10 = 1024
10 ** -1 = 0.1  # Negative exponent means division
```

**Negation (-):**
```python
x = 5
y = -x  # y is -5
z = -(-5)  # z is 5
```

---

## Mental Model 3: Order of Operations (PEMDAS/BODMAS)

Operations follow an order. Without it, expressions would be ambiguous.

```
PEMDAS / BODMAS:
P/B - Parentheses / Brackets    (first)
E/O - Exponents / Orders        
M/D - Multiplication / Division  (left to right)
A/S - Addition / Subtraction     (last, left to right)
```

**Example:**

```python
2 + 3 * 4

Without order: (2 + 3) * 4 = 20 (wrong)
With order: 2 + (3 * 4) = 14 (correct)
# Multiplication before addition!
```

**Python follows PEMDAS:**

```python
2 + 3 * 4           # = 2 + 12 = 14
(2 + 3) * 4         # = 5 * 4 = 20 (parentheses override)
10 - 2 + 3          # = 8 + 3 = 11 (left to right)
10 - (2 + 3)        # = 10 - 5 = 5 (parentheses override)
2 ** 3 ** 2         # = 2 ** 9 = 512 (right to left, special!)
100 / 10 / 2        # = 10 / 2 = 5 (left to right)
```

**Use parentheses liberally:**

```python
# Confusing
result = price * quantity + tax_rate * price * quantity

# Clear
subtotal = price * quantity
tax = tax_rate * subtotal
result = subtotal + tax
```

---

## Mental Model 4: Integer vs. Float Division (Type Matters)

Different operators produce different results based on input types.

```python
# True division (always float)
10 / 2 = 5.0      # Not 5! It's 5.0
10 / 3 = 3.333... # Float
-10 / 3 = -3.333...

# Integer division (rounds down)
10 // 2 = 5       # Integer result
10 // 3 = 3       # Rounds down
-10 // 3 = -4     # Rounds down (toward negative infinity!)
```

**Critical insight:**

```python
10 / 3 = 3.3333   # True division, keeps decimal
10 // 3 = 3       # Integer division, discards decimal
```

**Choosing which to use:**

- Want exact result with decimals? Use `/`
- Want whole number only? Use `//`
- Example: `items_per_box = total_items // 12`

---

## Mental Model 5: Modulo - Finding Remainders (Remainder Operator)

The **modulo** operator (`%`) gives the remainder after division.

```python
10 % 3 = 1  # 10 ÷ 3 = 3 remainder 1
17 % 5 = 2  # 17 ÷ 5 = 3 remainder 2
20 % 4 = 0  # 20 ÷ 4 = 5 remainder 0 (divides evenly)
```

**Real-world uses:**

```python
# Check if even
if number % 2 == 0:
    print("Even")

# Check if odd
if number % 2 == 1:
    print("Odd")

# Cycle through days of week
day_index = day_number % 7  # 0-6

# Get last digit
last_digit = number % 10  # 5 from 25, 0 from 20

# Get last two digits
last_two = number % 100  # 45 from 345
```

---

## Mental Model 6: Exponents - Powers and Roots (Exponent Operator)

The `**` operator raises a number to a power.

```python
2 ** 3 = 8      # 2 × 2 × 2
5 ** 2 = 25     # 5 × 5 (square)
10 ** 3 = 1000  # 10 × 10 × 10 (cube)

# Roots (negative exponent)
4 ** 0.5 = 2.0      # Square root of 4
8 ** (1/3) = 2.0    # Cube root of 8
27 ** (1/3) = 3.0   # Cube root of 27

# Large powers
2 ** 10 = 1024
10 ** 6 = 1000000

# Fractional powers
4 ** 2.5 = 32.0     # 4^2.5 = 32
```

**Why exponents matter:**

- Compound interest: `amount = principal * (1 + rate) ** years`
- Exponential growth: `population = initial * growth_rate ** time`
- Power calculations: `power = voltage ** 2 / resistance`
- Data scaling: many ML algorithms

---

## Mental Model 7: Operator Precedence and Associativity (Execution Order)

**Precedence** determines which operation happens first.

**Associativity** determines left-to-right or right-to-left when operators have same precedence.

```
Precedence (highest to lowest):
1. ** (exponent) - right to left
2. *, /, //, %   - left to right
3. +, -          - left to right
```

**Examples:**

```python
2 + 3 * 4       # 3*4 first (higher precedence), then +
                # = 2 + 12 = 14

10 - 2 - 3      # Left to right (same precedence)
                # = (10-2) - 3 = 8-3 = 5
                # NOT 10 - (2-3) = 11

2 ** 3 ** 2     # Right to left (special!)
                # = 2 ** (3**2) = 2**9 = 512
                # NOT (2**3)**2 = 8**2 = 64

10 / 5 * 2      # Left to right
                # = (10/5) * 2 = 2*2 = 4
                # NOT 10/(5*2) = 1
```

---

## Mental Model 8: Compound Assignment Operators (Shorthand Notation)

Combine assignment with arithmetic for concise code.

```python
x = 5
x = x + 3   # Traditional
x += 3      # Compound (same thing)

# All compound operators:
x += 5      # x = x + 5
x -= 3      # x = x - 3
x *= 2      # x = x * 2
x /= 4      # x = x / 4
x //= 3     # x = x // 3
x %= 5      # x = x % 5
x **= 2     # x = x ** 2
```

**When to use:**

```python
# Common in loops
count = 0
for item in items:
    count += 1  # More idiomatic than count = count + 1

# Financial calculations
balance = 1000
balance -= withdrawal  # More readable than balance = balance - withdrawal
```

---

## Mental Model 9: Floating-Point Precision Issues (Precision Matters)

Floats are approximate, not exact. This can cause subtle bugs.

```python
0.1 + 0.2           # 0.30000000000000004 (not 0.3!)
0.1 + 0.2 == 0.3    # False! (not equal)
```

**Why this happens:**

Computers can't represent all decimals exactly in binary. It's a fundamental limitation.

```
0.1 in binary: 0.0001100110011... (repeating, infinite)
Computer rounds to: 0.100000000000000005555...
```

**Solutions:**

```python
# 1. Accept small rounding errors
if abs(result - expected) < 0.0001:
    print("Close enough")

# 2. Use Decimal module (for money)
from decimal import Decimal
price = Decimal("19.99")  # Exact

# 3. Round results
result = round(0.1 + 0.2, 2)  # 0.3

# 4. Convert to integers (for money)
price_cents = 1999  # Represents $19.99
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Why Does 10 / 2 Equal 5.0, Not 5?"

**The question:** Shouldn't division of integers give an integer?

**The answer:** In Python 3, `/` always does true division (float result).

```python
10 / 2 = 5.0    # Float (even though result is whole)
10 // 2 = 5     # Integer division
```

This changed in Python 3. In Python 2, `/` gave integer if both operands were integers.

**When it matters:**

```python
items = 7
boxes = 2
per_box = items / boxes  # 3.5
per_box = items // boxes  # 3 (use this if you need whole)
```

### Confusion 2: "Order of Operations Is Confusing"

**The question:** How do I know what calculates first?

**The answer:** Use PEMDAS or parentheses.

```python
# Hard to read
result = 10 + 5 * 2 - 3 / 2

# Clear with parentheses
result = 10 + (5 * 2) - (3 / 2)  # Shows intent
```

**Rule:** When in doubt, add parentheses. It doesn't hurt.

### Confusion 3: "Negative Division and Modulo Are Weird"

**The question:** What's -10 // 3 or -10 % 3?

**The answer:** Python floors division (rounds toward negative infinity).

```python
10 // 3 = 3      # Rounds down: 3.333... → 3
-10 // 3 = -4    # Rounds down: -3.333... → -4 (not -3!)

10 % 3 = 1       # 10 = 3*3 + 1
-10 % 3 = 2      # -10 = 3*(-4) + 2
```

This is consistent but unintuitive. Most people don't use negative modulo.

### Confusion 4: "What's the Difference Between ** and pow()?"

**The question:** Should I use `2**3` or `pow(2, 3)`?

**The answer:** Same result, but `**` is more common and readable.

```python
2 ** 3 = 8      # Operator (preferred in most cases)
pow(2, 3) = 8   # Function (sometimes more powerful)
```

Use `**` unless you need `pow()`'s third argument (modulo).

### Confusion 5: "Why Does (1/3)*3 Not Equal 1?"

**The question:** Shouldn't this be exactly 1?

**The answer:** Floating-point rounding error.

```python
(1/3) * 3           # 0.9999999999999999
1/3                 # 0.3333...
0.3333... * 3       # 0.9999...
```

Always accept small floating-point errors:

```python
result = (1/3) * 3
if abs(result - 1) < 0.0001:
    print("It's 1")
```

---

## How Arithmetic Works Internally (Execution Model)

When Python evaluates `5 + 3 * 2`:

```
Step 1: PARSE
  Recognize: 5 + 3 * 2
  Identify operators: +, *

Step 2: DETERMINE PRECEDENCE
  * has higher precedence than +
  So: 5 + (3 * 2)

Step 3: EVALUATE SUBEXPRESSIONS
  Evaluate 3 * 2 first: 6
  Now have: 5 + 6

Step 4: EVALUATE REMAINING
  Evaluate 5 + 6: 11

Step 5: RETURN RESULT
  Result: 11
```

---

## Real-World Arithmetic (Practical Applications)

**Financial Calculation:**

```python
principal = 1000
rate = 0.05  # 5%
years = 10

# Compound interest formula
final_amount = principal * (1 + rate) ** years
print(f"${final_amount:.2f}")
```

**Statistics:**

```python
scores = [85, 92, 78, 95, 88]
average = sum(scores) / len(scores)
percentage = (average / 100) * 100  # Usually already 0-100
```

**Physics:**

```python
distance = 100  # meters
time = 5        # seconds
velocity = distance / time  # 20 m/s

# Kinetic energy: KE = (1/2) * m * v^2
mass = 10  # kg
kinetic_energy = (1/2) * mass * velocity ** 2
```

---

## Summary - The Big Picture

**What you learned:**
1. Basic operators: +, -, *, /, //, %, **
2. Order of operations (PEMDAS)
3. Integer vs. float division
4. Modulo for remainders
5. Exponents for powers
6. Operator precedence and associativity
7. Compound assignment operators
8. Floating-point precision issues

**Why this matters:**
- Arithmetic is fundamental to all programming
- Almost every program does calculations
- Wrong operator choice leads to bugs
- Order of operations affects results
- Floating-point precision affects accuracy

**What's next:**
Now you can do math. But what if you need to compare numbers?

Topic 8 teaches **Comparisons** - testing relationships between values.

---

## What You Should Be Able To Do Now

✅ Use arithmetic operators correctly
✅ Understand order of operations
✅ Choose between / and //
✅ Use modulo for real problems
✅ Calculate exponents
✅ Use compound assignment operators
✅ Understand floating-point limitations
✅ Build real-world arithmetic expressions
✅ Predict results of calculations
✅ Write clear, maintainable arithmetic code

