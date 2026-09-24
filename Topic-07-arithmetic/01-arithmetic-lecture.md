# Topic 7: Arithmetic - Detailed Mental Models (Expanded)

## Mental Model 1: What Are Operators? (The Tool Model) — EXPANDED

An **operator** is not just a symbol. It's an instruction to Python that says: "Take these values and perform a specific computation."

Think of operators like kitchen tools:
- A knife (operator) takes ingredients (values) and cuts them (performs an operation)
- A blender takes ingredients and mixes them
- An oven takes ingredients and heats them

Each tool transforms inputs into a specific output.

```python
5 + 3
```

This line is a **request** to Python:
- "I have two values: 5 and 3"
- "Apply the addition operation"
- "Tell me the result"

Python **executes** this by:
1. Reading the first value: 5
2. Reading the operator: +
3. Reading the second value: 3
4. Computing: 5 plus 3 is 8
5. Returning: 8

**The key insight:** An operator is an instruction that **transforms inputs into an output**.

Different operators transform differently:
- `+` transforms by summing
- `*` transforms by multiplying
- `-` transforms by subtracting
- Each operator has its own rule

```python
x = 10
y = 3

print(x + y)   # 13 (addition rule)
print(x - y)   # 7  (subtraction rule)
print(x * y)   # 30 (multiplication rule)
print(x / y)   # 3.333... (division rule)
```

Each line applies a different transformation to the same two numbers.

---

## Mental Model 2: Basic Arithmetic Operators — EXPANDED

Let's build intuition for each operator by thinking about what it represents in the real world.

### Addition (+): Combining Quantities

**Conceptual foundation:** Addition combines separate quantities into a total.

```python
apples = 5
oranges = 3
total_fruit = apples + oranges  # 8
```

The number line model:
```
Start at 0
Jump 5 steps right (apples): 0 ─→ 5
Then jump 3 more right (oranges): 5 ─→ 8
Final position: 8
```

**Why this matters:**
When you use `+`, Python is really asking: "What's the total if I combine these?"

```python
# Financial
income = 50000
bonus = 5000
total_pay = income + bonus  # 55000

# Accumulation
day1_sales = 1000
day2_sales = 1500
day3_sales = 1200
week_sales = day1_sales + day2_sales + day3_sales  # 3700
```

### Subtraction (-): Removing Quantities

**Conceptual foundation:** Subtraction removes or finds the difference between quantities.

```python
starting_balance = 1000
withdrawal = 250
remaining = starting_balance - withdrawal  # 750
```

The number line model:
```
Start at 1000
Jump 250 steps LEFT (remove): 1000 ←──── 750
Final position: 750
```

**Why this matters:**
When you use `-`, Python is asking: "What's left if I remove this?" or "What's the gap between these?"

```python
# Depletion (removing from a total)
inventory = 100
sold = 15
remaining = inventory - sold  # 85

# Finding difference
price_before = 99.99
price_after = 79.99
savings = price_before - price_after  # 20.00

# Negative results (owing money)
account_balance = 50
charge = 100
new_balance = account_balance - charge  # -50 (debt!)
```

**Important:** Subtraction can produce negative numbers. This isn't an error — it represents "going in the opposite direction."

### Multiplication (*): Scaling or Repetition

**Conceptual foundation:** Multiplication combines repeated groups.

Think of it as: "How many total if I have X groups of Y items?"

```python
boxes = 5
items_per_box = 12
total_items = boxes * items_per_box  # 60
```

The groups model:
```
Box 1: [12 items]
Box 2: [12 items]
Box 3: [12 items]
Box 4: [12 items]
Box 5: [12 items]
─────────────────
Total: 5 × 12 = 60 items
```

**Why this matters:**
Multiplication is *scaling* — making something bigger by a factor.

```python
# Area calculation (scaling in 2D)
width = 10
height = 5
area = width * height  # 50 square units

# Price calculation (quantity scaling)
price_per_item = 19.99
quantity = 3
total = price_per_item * quantity  # 59.97

# Percentage (scaling as a fraction)
original_price = 100
discount_rate = 0.20  # 20% off
discount_amount = original_price * discount_rate  # 20
```

**The scaling intuition:**
- `value * 2` means "make it twice as big"
- `value * 0.5` means "make it half as big"
- `value * 0` means "make it zero"
- `value * 1` means "keep it the same"

### Division (/): Splitting or Finding Rate

**Conceptual foundation:** Division splits a quantity into equal parts or finds how many times one thing fits into another.

Think of it as: "If I split X into Y groups, how much is in each group?"

```python
total_money = 100
people = 4
share_per_person = total_money / people  # 25
```

The splitting model:
```
Total: 100 dollars
Split into: 4 people
Each person gets: 25

Verify: 4 × 25 = 100 ✓
```

**Why this matters:**
Division finds the rate or ratio — "per unit."

```python
# Average (finding typical value)
scores = [85, 92, 78, 95]
average = sum(scores) / len(scores)  # 87.5

# Unit price (cost per item)
total_cost = 60
item_count = 4
price_per_item = total_cost / item_count  # 15

# Density (amount per unit)
population = 1000000
area_sq_km = 50000
density = population / area_sq_km  # 20 people per sq km

# Speed (distance per unit time)
distance = 100  # km
time = 2  # hours
speed = distance / time  # 50 km/h
```

**Critical distinction:**
In Python 3, `/` **always** produces a float (decimal number), even if the result is whole:

```python
10 / 2 = 5.0    # Not 5 — it's 5.0!
10 / 3 = 3.333...
```

This is intentional. Python is saying: "Division might not divide evenly, so I'll give you the exact result as a decimal."

### Integer Division (//): Splitting Into Whole Groups

**Conceptual foundation:** Integer division asks "How many complete groups can I make?" and discards any remainder.

Think of it as: "If I split X into groups of Y, how many complete groups?"

```python
cookies = 23
people = 4
cookies_per_person = cookies // 4  # 5 (with 3 left over)
```

The groups model:
```
Cookies: 23
Groups of 4:
Group 1: [4]  Group 2: [4]  Group 3: [4]  Group 4: [4]
Group 5: [4]
───────────────────────────────────────────────────────
Complete groups: 5
Leftover: 3 (not included in the result)
```

**Why this matters:**
When you need whole numbers only.

```python
# Pagination (how many pages of results?)
total_items = 97
items_per_page = 10
num_pages = total_items // items_per_page  # 9 full pages
# (1 page with fewer items remains)

# Distributing items evenly
students = 25
groups = 4
students_per_group = students // groups  # 6 students
# (1 student doesn't fit in a complete group)

# Converting minutes to hours
minutes = 150
hours = minutes // 60  # 2 full hours
```

**Compare with true division:**

```python
23 / 4 = 5.75   # "Exact answer with decimals"
23 // 4 = 5     # "How many complete groups?"
```

Choose based on what you need:
- Want exact? Use `/`
- Want whole numbers? Use `//`

### Modulo (%): Finding the Remainder

**Conceptual foundation:** Modulo asks "What's left over after dividing into complete groups?"

It's the **remainder operator**.

```python
23 % 4 = 3  # After making 5 complete groups of 4, 3 items remain
```

The remainder model:
```
23 divided by 4:
4 goes into 23 five times: 4 × 5 = 20
Leftover: 23 - 20 = 3
So: 23 % 4 = 3
```

**Mathematical relationship:**

```
dividend = (divisor × quotient) + remainder
23 = (4 × 5) + 3
```

**Why this matters:**
Modulo solves real problems about patterns and cycles.

```python
# Checking divisibility
if number % 2 == 0:
    print("Even number")  # Divides evenly by 2

if number % 3 == 0:
    print("Divisible by 3")

# Cycling (wrapping around)
days = [0, 1, 2, 3, 4, 5, 6]  # 0=Sunday, 1=Monday, etc
current_day = 25  # What day of week?
day_of_week = current_day % 7  # 4 = Thursday

# Last digit extraction
number = 12345
last_digit = number % 10  # 5

# Last two digits
last_two = number % 100  # 45

# Alternating pattern
if index % 2 == 0:
    print("Even index")
else:
    print("Odd index")
```

**The intuition:**
`a % b` means "What's the remainder when a is divided by b?"

```python
10 % 3 = 1   # 10 = 3×3 + 1
20 % 7 = 6   # 20 = 7×2 + 6
15 % 5 = 0   # 15 = 5×3 + 0 (divides evenly)
```

### Exponent (**): Repeated Multiplication

**Conceptual foundation:** Exponent means "multiply this by itself this many times."

```python
2 ** 3 = 2 × 2 × 2 = 8
```

The repetition model:
```
Start with: 2
Multiply by 2: 2 × 2 = 4
Multiply by 2 again: 4 × 2 = 8
(Do this 3 times total)

Result: 8
```

**Naming:**
- `2 ** 3` means "2 to the power of 3" or "2 cubed"
- `5 ** 2` means "5 to the power of 2" or "5 squared"
- `10 ** 6` means "10 to the power of 6"

**Why this matters:**
Exponents model explosive growth and scaling.

```python
# Compound interest (money growing over time)
principal = 1000
rate = 1.05  # 5% growth per year
years = 10
final_amount = principal * (rate ** years)
# After 10 years: 1000 × 1.05^10

# Exponential growth (bacteria, viruses)
initial_bacteria = 100
growth_factor = 2  # Doubles each hour
hours = 5
final_bacteria = initial_bacteria * (growth_factor ** hours)
# After 5 hours: 100 × 2^5 = 3200

# Area and volume scaling
# If you double each side of a square, area is 4× bigger (2²)
# If you double each side of a cube, volume is 8× bigger (2³)
```

**Special cases with exponents:**

```python
# Anything to power 0 = 1
5 ** 0 = 1
100 ** 0 = 1

# Anything to power 1 = itself
5 ** 1 = 5
100 ** 1 = 100

# Negative exponent = division (1/x)
2 ** -1 = 0.5       # 1/2
10 ** -2 = 0.01     # 1/100

# Fractional exponent = root
4 ** 0.5 = 2.0      # Square root of 4
8 ** (1/3) = 2.0    # Cube root of 8
27 ** (1/3) = 3.0   # Cube root of 27
```

**Intuition for fractional exponents:**

```python
4 ** 0.5 asks: "What number, multiplied by itself, equals 4?"
Answer: 2 (because 2 × 2 = 4)

8 ** (1/3) asks: "What number, multiplied by itself 3 times, equals 8?"
Answer: 2 (because 2 × 2 × 2 = 8)
```

---

## Mental Model 3: Order of Operations (PEMDAS/BODMAS) — EXPANDED

**The fundamental problem:** Without agreed-upon order, the same expression could mean different things.

```python
2 + 3 * 4

Interpretation 1: (2 + 3) * 4 = 5 * 4 = 20
Interpretation 2: 2 + (3 * 4) = 2 + 12 = 14
```

Which is correct? Ambiguity breaks everything.

**The solution:** Python (and all math) uses PEMDAS/BODMAS—a universal order.

```
PEMDAS / BODMAS:
P/B - Parentheses / Brackets    (calculate first)
E/O - Exponents / Orders        
M/D - Multiplication / Division  (same precedence, left to right)
A/S - Addition / Subtraction     (calculate last, left to right)
```

**The deep concept:** Precedence is a hierarchy of "importance." Higher precedence operations happen first.

```
Hierarchy (highest to lowest):
Level 1: Parentheses          (most important)
Level 2: Exponents            (very important)
Level 3: *, /, //, %          (important)
Level 4: +, -                 (least important)
```

**Example walkthrough:**

```python
2 + 3 * 4

Step 1: Identify operations
  Operators: +, *

Step 2: Find highest precedence
  * has precedence 3
  + has precedence 4
  So * happens first

Step 3: Calculate highest precedence
  3 * 4 = 12
  Expression becomes: 2 + 12

Step 4: Calculate remaining
  2 + 12 = 14

Result: 14
```

**More complex example:**

```python
10 - 2 + 3 * 4 / 2

Step 1: Identify operations
  Operators: -, +, *, /

Step 2: Find highest precedence
  * and / have precedence 3 (same level)
  - and + have precedence 4

Step 3: Calculate level 3 (left to right)
  3 * 4 = 12
  12 / 2 = 6
  Expression becomes: 10 - 2 + 6

Step 4: Calculate level 4 (left to right)
  10 - 2 = 8
  8 + 6 = 14

Result: 14
```

**The associativity rule:** When operators have the same precedence, go left to right (except exponents, which go right to left).

```python
# Left to right (normal)
10 - 2 - 3
= (10 - 2) - 3
= 8 - 3
= 5
# NOT: 10 - (2 - 3) = 10 - (-1) = 11

# Left to right (normal)
10 / 5 / 2
= (10 / 5) / 2
= 2 / 2
= 1
# NOT: 10 / (5 / 2) = 10 / 2.5 = 4

# Right to left (special for exponents!)
2 ** 3 ** 2
= 2 ** (3 ** 2)
= 2 ** 9
= 512
# NOT: (2 ** 3) ** 2 = 8 ** 2 = 64
```

**Parentheses override everything:**

```python
# Without parentheses
2 + 3 * 4 = 2 + 12 = 14

# With parentheses (overrides precedence)
(2 + 3) * 4 = 5 * 4 = 20
```

Parentheses say: "Do this first, regardless of normal precedence."

**Why this matters for writing clear code:**

```python
# Hard to read (relies on you knowing precedence)
total = principal * rate ** years + interest_paid - tax * deduction

# Clear (shows intent with parentheses)
compound_growth = principal * (rate ** years)
total_interest = interest_paid - (tax * deduction)
total = compound_growth + total_interest
```

**Pro tip:** Use parentheses liberally. They cost nothing and make code readable.

---

## Mental Model 4: Integer vs. Float Division — EXPANDED

This is a critical conceptual difference that confuses many programmers.

### The Core Distinction

**True division (/):** Gives the mathematically exact answer, as a decimal.

```python
10 / 2 = 5.0     # Exact (happens to be whole, but still a float)
10 / 3 = 3.3333... # Exact (decimal representation)
10 / 4 = 2.5     # Exact
```

Notice: The result is always a **float** (has a decimal point), even if the answer is mathematically whole.

**Integer division (//):** Gives the number of complete groups, discarding the remainder.

```python
10 // 2 = 5      # 5 complete groups of 2
10 // 3 = 3      # 3 complete groups of 3 (leftover 1 ignored)
10 // 4 = 2      # 2 complete groups of 4 (leftover 2 ignored)
```

The result is an **integer** (no decimal point).

### The Mental Models

**True division (/) asks:** "What's the exact answer?"

```python
cookies = 10
people = 3
per_person = cookies / people  # 3.333...
# Each person gets 3.333... cookies (mathematically exact)
```

**Integer division (//) asks:** "How many complete groups?"

```python
cookies = 10
people = 3
complete_per_person = cookies // people  # 3
leftover = cookies % people  # 1
# Each person gets 3 complete cookies, 1 leftover
```

### Real-World Difference

```python
# Splitting money (true division)
budget = 100
people = 3
per_person = budget / people  # 33.333... (everyone gets exact share)

# Distributing items (integer division)
books = 100
students = 3
books_per_student = books // students  # 33 books each
leftover_books = books % books  # 1 book remains
```

### Why Python Changed This

In Python 2, `/` behaved differently based on input types:

```python
# Python 2 (old behavior)
10 / 2 = 5       # Both integers → integer result
10 / 3 = 3       # Both integers → integer result (truncated!)
10.0 / 3 = 3.333... # One float → float result
```

This was confusing. Different results for essentially the same operation.

Python 3 simplified it:

```python
# Python 3 (current behavior)
10 / 2 = 5.0     # Always true division
10 / 3 = 3.333...
10 // 2 = 5      # Use // for integer division (explicit)
10 // 3 = 3
```

Now the operator type determines behavior, not the input types.

---

## Mental Model 5: Modulo - Finding Remainders — EXPANDED

**The deep concept:** Modulo solves the problem "What's left after grouping?"

### Understanding Through Decomposition

Every division can be decomposed into complete groups plus remainder:

```
dividend = (divisor × groups) + remainder
23 = (4 × 5) + 3
```

Modulo extracts just the remainder part.

```python
dividend = 23
divisor = 4

quotient = 23 // 4         # 5 (complete groups)
remainder = 23 % 4        # 3 (what's left)

# Verify the relationship
check = (divisor * quotient) + remainder
print(check)  # 23 (original dividend)
```

### Real-World Problem: Cycling

Imagine a calendar. Days of the week cycle 0-6:

```
Day 0: Sunday
Day 1: Monday
Day 2: Tuesday
...
Day 6: Saturday
Day 7: Sunday (cycles back)
Day 8: Monday (cycles back)
```

If today is day 0 and 23 days pass, what day is it?

```python
current_day = 0
days_pass = 23

future_day = (current_day + days_pass) % 7
# = 23 % 7
# = 2 (Tuesday)

# Verify: 7 groups of 3 days = 21 days
# 23 - 21 = 2 days remaining
# So we're at day 2 (Tuesday)
```

### Real-World Problem: Checking Divisibility

Some numbers divide evenly. Some don't.

```python
# Is 15 divisible by 3?
15 % 3 = 0  # Yes (divides evenly, no remainder)

# Is 16 divisible by 3?
16 % 3 = 1  # No (remainder of 1)

# Is 20 divisible by 5?
20 % 5 = 0  # Yes
```

Pattern: If `n % divisor == 0`, then n is divisible by divisor.

```python
# Check if even
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Check if divisible by 10
if number % 10 == 0:
    print("Multiple of 10")
```

### Real-World Problem: Extracting Digits

```python
number = 12345

last_digit = number % 10      # 5
last_two_digits = number % 100  # 45
last_three_digits = number % 1000  # 345
```

**Why this works:**
- `n % 10` removes everything except the last digit
- `n % 100` removes everything except the last 2 digits
- `n % 1000` removes everything except the last 3 digits

---

## Mental Model 6: Exponents - Powers and Roots — EXPANDED

**The deep concept:** Exponents represent repeated multiplication. They model scaling and growth.

### Repeated Multiplication

```
2 ** 1 = 2                      (2)
2 ** 2 = 2 × 2 = 4              (multiply once)
2 ** 3 = 2 × 2 × 2 = 8          (multiply twice)
2 ** 4 = 2 × 2 × 2 × 2 = 16     (multiply three times)
2 ** 5 = 2 × 2 × 2 × 2 × 2 = 32 (multiply four times)
```

**Pattern:** `base ** exponent` means "multiply base by itself (exponent - 1) times"

### Real-World: Compound Growth

Imagine money in a savings account growing at 5% per year:

```python
initial = 1000  # $1000
rate = 1.05     # 5% growth (multiply by 1.05 each year)

after_1_year = initial * rate           # 1000 * 1.05
after_2_years = initial * rate * rate   # 1000 * 1.05 * 1.05
after_3_years = initial * rate * rate * rate
...
after_10_years = initial * (rate ** 10)
```

Exponents let us express "multiply by 1.05 ten times" concisely.

### Special Cases: Powers of 0, 1, and Negatives

**Power of 1:**
```python
anything ** 1 = anything
5 ** 1 = 5
100 ** 1 = 100
0.5 ** 1 = 0.5
```

**Power of 0:**
```python
anything ** 0 = 1  (by mathematical definition)
5 ** 0 = 1
100 ** 0 = 1
0.5 ** 0 = 1
```

**Why 5^0 = 1:**

```
5 ** 3 = 5 × 5 × 5 = 125
5 ** 2 = 5 × 5 = 25
5 ** 1 = 5
5 ** 0 = ?

Pattern: Each step down, we divide by 5
125 / 5 = 25
25 / 5 = 5
5 / 5 = 1

So 5 ** 0 = 1
```

**Negative exponents: Division**

```python
2 ** -1 = 1 / 2 = 0.5
2 ** -2 = 1 / (2 * 2) = 0.25
2 ** -3 = 1 / (2 * 2 * 2) = 0.125
```

**The pattern:**
```
base ** -n = 1 / (base ** n)
```

### Fractional Exponents: Roots

**Question:** What number, when multiplied by itself 2 times, equals 4?

```python
x * x = 4
x = 2  # 2 * 2 = 4
```

This is called the "square root" of 4. In exponent form:

```python
4 ** 0.5 = 2  # 0.5 = 1/2
```

**Fractional exponent rule:**

```
base ** (1/n) = the nth root of base
base ** 0.5 = square root
base ** (1/3) = cube root
```

**Examples:**

```python
4 ** 0.5 = 2.0       # Square root: 2 * 2 = 4
9 ** 0.5 = 3.0       # Square root: 3 * 3 = 9
27 ** (1/3) = 3.0    # Cube root: 3 * 3 * 3 = 27
16 ** 0.25 = 2.0     # Fourth root: 2*2*2*2 = 16
```

---

## Mental Model 7: Floating-Point Precision — EXPANDED

**The deep problem:** Computers can't represent all decimal numbers exactly.

### Why Computers Can't Store 0.1 Exactly

Computers store numbers in binary (1s and 0s). Some decimals can't be expressed in binary:

```
0.1 in decimal: 0.1
0.1 in binary:  0.0001100110011... (repeating forever!)
```

It's like trying to write 1/3 in decimal: 0.333333... (repeating forever).

Computers have finite memory, so they round:

```python
0.1 (stored) ≈ 0.1000000000000000055511151231...
```

Not exact, but very close.

### The Problem This Creates

```python
0.1 + 0.2 = 0.30000000000000004  # Not exactly 0.3!
```

Each number has tiny rounding errors. When you add them, errors compound:

```python
a = 0.1         # 0.1000000000000000055...
b = 0.2         # 0.2000000000000000111...
c = a + b       # 0.3000000000000000166... ≈ 0.30000000000000004
```

### The Comparison Problem

```python
if 0.1 + 0.2 == 0.3:
    print("They're equal")
else:
    print("They're NOT equal")  # This prints!

# Why?
# 0.1 + 0.2 ≈ 0.30000000000000004
# 0.3 ≈ 0.29999999999999999
# They're not exactly the same!
```

### Solution 1: Accept Small Errors (Tolerance)

```python
result = 0.1 + 0.2
expected = 0.3
tolerance = 0.0001

if abs(result - expected) < tolerance:
    print("Close enough!")
```

**The abs() function:** Returns absolute value (distance from 0, ignoring sign).

### Solution 2: Use Decimal for Money

```python
from decimal import Decimal

price_1 = Decimal("19.99")
price_2 = Decimal("29.99")
total = price_1 + price_2  # Exact
```

Decimal stores numbers as exact decimals, not binary approximations.

### Solution 3: Round Results

```python
result = 0.1 + 0.2
rounded = round(result, 2)  # Round to 2 decimal places
print(rounded)  # 0.3
```

### Solution 4: Work with Integers (For Money)

Store amounts in cents, not dollars:

```python
price_1_cents = 1999    # $19.99
price_2_cents = 2999    # $29.99
total_cents = price_1_cents + price_2_cents  # 4998
total_dollars = total_cents / 100  # $49.98
```

Since integers are exact, this avoids floating-point errors.

---

## Mental Model 8: Operator Precedence and Associativity — EXPANDED

**The deep concept:** When you write an expression, Python needs to know: "What order do I calculate this in?"

### Precedence: The Hierarchy of Operations

Different operators have different "importance" or priority.

```
Priority 1 (Highest - Do First):
  Parentheses ()
  
Priority 2:
  Exponent **
  
Priority 3:
  Multiplication *, Division /, Integer Division //, Modulo %
  
Priority 4 (Lowest - Do Last):
  Addition +, Subtraction -
```

**Why precedence matters:**

Without it, math expressions would be ambiguous:

```python
2 + 3 * 4

If we calculated left to right:
(2 + 3) * 4 = 5 * 4 = 20

If we follow precedence (* before +):
2 + (3 * 4) = 2 + 12 = 14
```

Python follows precedence, so the answer is **14**.

### Associativity: Left-to-Right vs Right-to-Left

When two operators have the **same precedence**, which one runs first?

**Most operators:** Left-to-right (left associative)

```python
10 - 2 - 3

Left to right: (10 - 2) - 3 = 8 - 3 = 5
Right to left: 10 - (2 - 3) = 10 - (-1) = 11

Python uses left-to-right, so: 5
```

**Exponent:** Right-to-left (right associative)

```python
2 ** 3 ** 2

Right to left: 2 ** (3 ** 2) = 2 ** 9 = 512
Left to right: (2 ** 3) ** 2 = 8 ** 2 = 64

Python uses right-to-left, so: 512
```

This is the only exception in basic arithmetic.

### Complete Precedence Table (for reference)

```
Operator                Precedence    Associativity
─────────────────────────────────────────────────
() Parentheses         1 (Highest)    N/A
** Exponent            2              Right to left
*, /, //, %            3              Left to right
+, -                   4 (Lowest)     Left to right
```

### Practical Examples

**Example 1: Mixed operators**

```python
2 + 3 * 4 - 5

Step 1: Highest precedence first
  3 * 4 = 12
  Expression: 2 + 12 - 5

Step 2: Same precedence, left to right
  2 + 12 = 14
  Expression: 14 - 5

Step 3: Calculate remaining
  14 - 5 = 9

Result: 9
```

**Example 2: Multiple multiplications and divisions**

```python
100 / 5 / 2 * 3

Step 1: All same precedence, left to right
  100 / 5 = 20
  20 / 2 = 10
  10 * 3 = 30

Result: 30
```

**Example 3: Exponents with multiplication**

```python
2 * 3 ** 2

Step 1: Exponent first (higher precedence)
  3 ** 2 = 9
  Expression: 2 * 9

Step 2: Multiplication
  2 * 9 = 18

Result: 18
```

---

## Mental Model 9: Compound Assignment Operators — EXPANDED

**The deep concept:** Compound assignment combines an operation with storage in one step.

### The Traditional Way

```python
x = 5
x = x + 3  # "Add 3 to x, then store result back in x"
print(x)   # 8
```

This is clear but verbose. We're saying: "Take x, add 3, and put it back in x."

### The Compound Way

```python
x = 5
x += 3     # "Add 3 to x, in place"
print(x)   # 8
```

Both are identical. `+=` is shorthand for `= +`.

### All Compound Operators

```python
x = 10
x += 5      # x = 10 + 5 = 15
x -= 3      # x = 15 - 3 = 12
x *= 2      # x = 12 * 2 = 24
x /= 3      # x = 24 / 3 = 8.0
x //= 2     # x = 8.0 // 2 = 4.0
x %= 3      # x = 4.0 % 3 = 1.0
x **= 3     # x = 1.0 ** 3 = 1.0
```

**The pattern:** `x [op]= value` means `x = x [op] value`

### When to Use Compound Assignment

**Common in loops (accumulation):**

```python
# Counting
count = 0
for item in items:
    count += 1  # More idiomatic than count = count + 1

# Summing
total = 0
for score in scores:
    total += score  # More readable

# Building strings
result = ""
for word in words:
    result += word  # Cleaner than result = result + word
```

**In financial calculations:**

```python
balance = 1000
balance -= 50       # Withdrawal
balance += 100      # Deposit
balance *= 1.05     # Interest
```

**Why prefer compound assignment:**
- More concise
- Shows intent: "Modify in place"
- Standard in industry code
- Slightly more efficient (one operation instead of two)

---

This comprehensive document contains all expanded mental models with detailed conceptual foundations, real-world examples, and deep intuition-building explanations.
