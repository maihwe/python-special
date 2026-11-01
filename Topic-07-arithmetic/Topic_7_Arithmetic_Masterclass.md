# Topic 7: Arithmetic in Python

## A mastery-level learning guide: mental models, execution, debugging, and practical engineering

> **Learning goal:** By the end of this topic, you should be able to
> explain arithmetic operators in your own words, predict Python's
> results before running code, trace expressions step by step, choose
> appropriate numeric representations, debug arithmetic mistakes, and
> apply arithmetic safely in small software projects.

------------------------------------------------------------------------

## How to use this document

Do not try to memorize every section in one sitting. Work through it in
this order:

1.  Read the mental model and explain it aloud in your own words.
2.  Trace each worked example with pencil and paper before running it.
3.  Predict the output of the code.
4.  Run the code and compare your prediction.
5.  If your answer differs, identify the exact step where your reasoning
    changed.
6.  Complete the practice and debugging exercises without looking at the
    solutions.
7.  Build the mini-project and defend your design decisions.

### A note about examples

The examples use ordinary numbers and simple variable names first. Later
sections introduce realistic situations such as sales, balances,
discounts, and transaction records. Money examples distinguish between
*learning arithmetic* and *production financial software*: binary
floating-point numbers should not be used carelessly for exact monetary
values.

------------------------------------------------------------------------

# Part 1 --- The foundations

## 1. What is arithmetic in programming?

Arithmetic is the use of mathematical operations to calculate new values
from existing values.

In Python, arithmetic is commonly used to:

-   calculate totals and balances;
-   measure differences;
-   distribute quantities;
-   calculate averages, rates, and percentages;
-   determine remainders and repeating patterns;
-   calculate areas, distances, and other measurements;
-   update counters and running totals.

A computer does not understand the real-world meaning of a number by
itself. It follows the operations and instructions in the program. If a
variable is named `bank_balance`, Python does not automatically know
that it represents money. The programmer gives the value meaning through
names, rules, validation, and program design.

### A simple example

``` python
income = 500
expense = 125
balance = income - expense

print(balance)
```

Output:

``` text
375
```

Interpretation:

-   `income` refers to the value `500`.
-   `expense` refers to the value `125`.
-   `-` tells Python to subtract the second operand from the first.
-   `balance = ...` stores the resulting value under the name `balance`.
-   `print()` displays the stored value.

### Important distinction: calculation versus display

An expression can be evaluated without being displayed.

``` python
5 + 3
```

In an interactive Python shell, the result may be shown automatically.
In a normal `.py` script, this expression does not print anything.

To display the result in a script:

``` python
print(5 + 3)
```

To store it:

``` python
result = 5 + 3
```

To both store and display it:

``` python
result = 5 + 3
print(result)
```

**Mental model:** An expression calculates a value. Assignment gives
that value a name. `print()` sends a representation of the value to the
output.

------------------------------------------------------------------------

## 2. What are operators, operands, and expressions?

An **operator** is a symbol or keyword that specifies an operation.

An **operand** is a value or expression that an operator acts on.

An **expression** is a combination of values, names, operators, and
possibly function calls that Python can evaluate to produce a value.

Example:

``` python
total = 5 + 3
```

In `5 + 3`:

-   `+` is the operator.
-   `5` is the left operand.
-   `3` is the right operand.
-   `5 + 3` is the expression.
-   `8` is the value produced by the expression.
-   `total` is the variable receiving that value.

### The tool model

Think of an operator as a tool and its operands as the materials
supplied to that tool.

``` text
Operand 1       Operator       Operand 2
   5       +       3
   \               /
    \             /
     \           /
      Addition operation
              |
              v
          Result: 8
```

The operator determines the operation. The operand types can also affect
the behaviour. For example, `+` can add numbers or concatenate strings.

### Unary and binary operators

A **unary operator** works with one operand:

``` python
temperature = 8
print(-temperature)  # -8
```

A **binary operator** works with two operands:

``` python
print(5 + 3)  # 8
```

The minus sign can therefore have different roles:

``` python
difference = 10 - 3  # binary subtraction
negative = -3        # unary negation
```

### Check your understanding

For `result = 12 * 4`, identify:

1.  the operator;
2.  the two operands;
3.  the expression;
4.  the result;
5.  the variable receiving the result.

------------------------------------------------------------------------

# Part 2 --- The arithmetic operators

## 3. Addition (`+`): combining quantities

### Conceptual foundation

Addition combines quantities to produce a sum.

``` python
apples = 5
oranges = 3
total_fruit = apples + oranges

print(total_fruit)  # 8
```

### Number-line model

``` text
0 ---- 1 ---- 2 ---- 3 ---- 4 ---- 5 ---- 6 ---- 7 ---- 8
                                      start
                                       +3
                                        ---------------->
```

Start at 5 and move three units to the right. You arrive at 8.

### Step-by-step trace

For:

``` python
total = 5 + 3
```

1.  Python evaluates the left operand: `5`.
2.  Python evaluates the right operand: `3`.
3.  Python applies `+` to the two values.
4.  The expression produces `8`.
5.  Assignment stores `8` in `total`.

### Real-world applications

**Combining income:**

``` python
salary = 50000
bonus = 5000
total_income = salary + bonus
```

**Combining daily sales:**

``` python
monday_sales = 1200
tuesday_sales = 1500
wednesday_sales = 900

three_day_sales = monday_sales + tuesday_sales + wednesday_sales
```

**Accumulating values in a loop:**

``` python
scores = [70, 80, 90]
total = 0

for score in scores:
    total += score

print(total)  # 240
```

### Addition with different types

The `+` operator does not always mean numerical addition.

``` python
print(5 + 3)                 # 8
print(2.5 + 1.5)             # 4.0
print("Hello " + "Python")   # Hello Python
```

But adding a number directly to a string is not allowed:

``` python
print("5" + 3)  # TypeError
```

Convert deliberately if that is what you intend:

``` python
print(int("5") + 3)  # 8
```

Do not convert blindly. First decide whether `"5"` represents text or a
number in your program.

### Common misunderstanding

This does not update `number`:

``` python
number = 5
number + 3
print(number)  # 5
```

The expression produces `8`, but the result is not assigned anywhere.

Correct:

``` python
number = 5
number = number + 3
print(number)  # 8
```

Or use compound assignment:

``` python
number = 5
number += 3
print(number)  # 8
```

------------------------------------------------------------------------

## 4. Subtraction (`-`): removing quantities or finding a difference

### Conceptual foundation

Subtraction can describe removing an amount from a starting quantity or
finding the difference between two values.

``` python
starting_balance = 1000
withdrawal = 250
remaining_balance = starting_balance - withdrawal

print(remaining_balance)  # 750
```

### Number-line model

``` text
500 ---- 600 ---- 700 ---- 750 ---- 800 ---- 900 ---- 1000
                         <-------------------------------
                                move left by 250
```

Starting at 1000 and moving 250 units left gives 750.

### Real-world examples

**Inventory:**

``` python
stock = 100
items_sold = 15
remaining_stock = stock - items_sold
```

**Price reduction:**

``` python
original_price = 100
new_price = 80
savings = original_price - new_price
```

**Negative balance:**

``` python
balance = 50
charge = 100
new_balance = balance - charge

print(new_balance)  # -50
```

A negative result is a valid number. Whether a negative balance is
allowed is a *business rule* that the application must enforce.

### Important distinction: arithmetic versus validation

Python permits this:

``` python
stock = 5
sold = 8
remaining = stock - sold  # -3
```

But an inventory application may need to reject selling more items than
are available. The arithmetic is valid; the business operation may not
be.

``` python
stock = 5
sold = 8

if sold > stock:
    print("Not enough stock")
else:
    stock -= sold
    print("Remaining:", stock)
```

------------------------------------------------------------------------

## 5. Multiplication (`*`): repeated groups and scaling

### Conceptual foundation

Multiplication can represent repeated equal groups.

If there are 5 boxes and each box contains 12 items:

``` python
boxes = 5
items_per_box = 12
total_items = boxes * items_per_box

print(total_items)  # 60
```

### Group model

``` text
Box 1: [12]
Box 2: [12]
Box 3: [12]
Box 4: [12]
Box 5: [12]

12 + 12 + 12 + 12 + 12 = 60
5 * 12 = 60
```

Multiplication is also used for scaling:

-   `value * 2`: twice the value;
-   `value * 0.5`: half the value;
-   `value * 1`: unchanged value;
-   `value * 0`: zero.

### Real-world applications

**Total price:**

``` python
price_per_item = 19.99
quantity = 3
total = price_per_item * quantity
```

**Area of a rectangle:**

``` python
width = 10
height = 5
area = width * height  # 50 square units
```

**Percentage amount:**

``` python
original_price = 100
discount_rate = 0.20
discount_amount = original_price * discount_rate
```

### Percentage mental model

A percentage is a ratio out of 100.

``` text
20% = 20 / 100 = 0.20
```

Therefore:

``` python
discount = 200 * 0.20  # 40
```

To calculate a price after a discount:

``` python
original_price = 200
discount_rate = 0.20

discount_amount = original_price * discount_rate
final_price = original_price - discount_amount

print(final_price)  # 160.0
```

A shorter equivalent expression is:

``` python
final_price = original_price * (1 - discount_rate)
```

Use the longer version while learning because it exposes each
calculation.

------------------------------------------------------------------------

## 6. True division (`/`): splitting and calculating rates

### Conceptual foundation

Division can split a quantity into equal parts or calculate how much of
one quantity exists per unit of another.

``` python
total_money = 100
people = 4
share_per_person = total_money / people

print(share_per_person)  # 25.0
```

### Splitting model

``` text
Total: 100

Person 1: 25
Person 2: 25
Person 3: 25
Person 4: 25

25 + 25 + 25 + 25 = 100
```

### Division in Python 3

The `/` operator performs true division and returns a `float`, even when
the mathematical result is a whole number.

``` python
print(10 / 2)  # 5.0
print(10 / 3)  # 3.3333333333333335
print(10 / 4)  # 2.5
```

Check the type:

``` python
print(type(10 / 2))  # <class 'float'>
```

### Division as a rate

A rate describes an amount relative to another quantity.

**Average score:**

``` python
scores = [85, 92, 78, 95]
average = sum(scores) / len(scores)
print(average)  # 87.5
```

**Speed:**

``` python
distance_km = 100
time_hours = 2
speed = distance_km / time_hours
print(speed)  # 50.0 km/h
```

**Unit price:**

``` python
total_cost = 60
item_count = 4
price_per_item = total_cost / item_count
```

### Division by zero

A denominator of zero is invalid for ordinary division:

``` python
print(10 / 0)  # ZeroDivisionError
```

Protect calculations when the denominator can be zero:

``` python
total = 100
people = 0

if people == 0:
    print("Cannot divide by zero people")
else:
    print(total / people)
```

Do not merely hide the error. Decide what the application should do when
the denominator is zero.

------------------------------------------------------------------------

## 7. Floor division (`//`): calculating complete groups

### Conceptual foundation

Floor division returns the quotient rounded down to the nearest integer
value. With integer operands, the result is an integer. With a float
operand, the result is a float.

``` python
print(23 // 4)  # 5
print(23 / 4)   # 5.75
```

### Complete-groups model

You have 23 cookies and want to make groups of 4.

``` text
23 cookies:

[4] [4] [4] [4] [4]  [3 left over]

5 complete groups
3 remaining cookies

23 // 4 = 5
23 % 4  = 3
```

### Practical applications

**Full boxes:**

``` python
items = 53
items_per_box = 10

full_boxes = items // items_per_box
leftover_items = items % items_per_box

print(full_boxes)      # 5
print(leftover_items)  # 3
```

**Full pages:**

``` python
total_items = 97
items_per_page = 10

full_pages = total_items // items_per_page
```

If you need the number of pages required to display *all* items,
including a partially filled final page, `//` alone is not enough:

``` python
pages_needed = (total_items + items_per_page - 1) // items_per_page
print(pages_needed)  # 10
```

Another readable option is:

``` python
pages_needed = (total_items + items_per_page - 1) // items_per_page
```

This formula assumes `items_per_page` is positive. Validate that
assumption.

### Important correction: floor does not mean simply remove decimals

For positive values, floor division can look like truncation:

``` python
print(7 // 2)  # 3
```

For negative values, the distinction becomes visible:

``` python
print(-7 // 2)  # -4
```

Why `-4`? Because `-3.5` rounded *down toward negative infinity* is
`-4`.

``` text
Number line:

-5 ---- -4 ---- -3 ---- -2 ---- -1 ---- 0
        ^
        floor(-3.5) = -4
```

Do not teach `//` as "remove everything after the decimal point." The
accurate rule is **floor the quotient**.

------------------------------------------------------------------------

## 8. Modulo (`%`): finding the remainder

### Conceptual foundation

Modulo returns the remainder associated with floor division.

For positive integers:

``` python
23 // 4  # 5 complete groups
23 % 4   # 3 remaining
```

The relationship is:

``` text
dividend = divisor * quotient + remainder

23 = 4 * 5 + 3
```

In Python, the quotient used in this relationship is the floor-division
result.

### Step-by-step calculation

``` python
dividend = 23
divisor = 4

quotient = dividend // divisor
remainder = dividend % divisor

print(quotient)   # 5
print(remainder)  # 3
```

### Visual model

``` text
23 items
|----4----|----4----|----4----|----4----|----4----|---3---|
    1          2        3        4        5       leftover

23 % 4 = 3
```

### Application 1: checking even and odd numbers

A number is even if it divides evenly by 2.

``` python
number = 14

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

Why?

-   `14 % 2` produces `0`.
-   A remainder of zero means the number is divisible by 2.
-   `15 % 2` produces `1`, so 15 is odd.

### Application 2: checking divisibility

``` python
number = 30

if number % 5 == 0:
    print("Divisible by 5")
```

### Application 3: cycling through days

Suppose day indexes repeat from 0 to 6.

``` text
0 Sunday
1 Monday
2 Tuesday
3 Wednesday
4 Thursday
5 Friday
6 Saturday
7 Sunday again
8 Monday again
```

Modulo wraps the count back into the range:

``` python
days_passed = 23
day_index = days_passed % 7

print(day_index)  # 2
```

If day 0 is Sunday, day 2 is Tuesday.

For a starting day other than zero:

``` python
current_day = 4
days_passed = 10

future_day = (current_day + days_passed) % 7
```

### Application 4: extracting digits

``` python
number = 12345

last_digit = number % 10
last_two_digits = number % 100
last_three_digits = number % 1000

print(last_digit)        # 5
print(last_two_digits)   # 45
print(last_three_digits) # 345
```

### Negative modulo: an important Python detail

Python's modulo result has the same sign as the divisor, unless the
result is zero.

``` python
print(7 % 3)    # 1
print(-7 % 3)   # 2
print(7 % -3)   # -2
print(-7 % -3)  # -1
```

This follows Python's floor-division relationship:

``` python
a == (a // b) * b + (a % b)
```

For example:

``` python
-7 == (-7 // 3) * 3 + (-7 % 3)
-7 == (-3 * 3) + 2
-7 == -9 + 2
```

This matters when using modulo for cyclic indexes or time calculations
involving negative offsets.

------------------------------------------------------------------------

## 9. Exponentiation (`**`): powers and repeated multiplication

### Conceptual foundation

Exponentiation raises a base to a power.

``` python
2 ** 3
```

-   `2` is the base.
-   `3` is the exponent.
-   The result is `2 * 2 * 2`, which is `8`.

### Repeated multiplication model

``` text
2 ** 1 = 2
2 ** 2 = 2 * 2 = 4
2 ** 3 = 2 * 2 * 2 = 8
2 ** 4 = 2 * 2 * 2 * 2 = 16
2 ** 5 = 2 * 2 * 2 * 2 * 2 = 32
```

### Special cases

**Power of one:**

``` python
5 ** 1  # 5
```

**Power of zero:**

``` python
5 ** 0    # 1
100 ** 0  # 1
```

For any nonzero base, raising it to the zero power produces 1. The
expression `0 ** 0` is a special mathematical case; Python evaluates it
as `1`, but do not generalize the nonzero-base rule to that case without
understanding the context.

**Negative exponent:**

``` python
2 ** -1  # 0.5
2 ** -2  # 0.25
```

A negative exponent means reciprocal:

``` text
2 ** -2 = 1 / (2 ** 2)
        = 1 / 4
        = 0.25
```

**Fractional exponent:**

``` python
4 ** 0.5       # 2.0
8 ** (1 / 3)   # approximately 2.0
```

A power of `1/2` represents a square root; a power of `1/3` represents a
cube root for positive real bases.

### Real-world application: compound growth

``` python
principal = 1000
annual_growth_factor = 1.05
years = 10

final_amount = principal * (annual_growth_factor ** years)
print(final_amount)
```

The factor `1.05` means the amount becomes 105% of its previous value
each year.

This is a simplified mathematical model. Real financial products may
include fees, taxes, different compounding intervals, deposits,
withdrawals, and rounding rules.

### Exponentiation is right-associative

``` python
print(2 ** 3 ** 2)
```

Python groups this as:

``` python
2 ** (3 ** 2)
2 ** 9
512
```

It does not group it as `(2 ** 3) ** 2`, which would produce 64.

### Unary minus and exponentiation

A subtle precedence rule:

``` python
print(-3 ** 2)    # -9
print((-3) ** 2)  # 9
```

The first expression means:

``` python
-(3 ** 2)
```

The second makes the negative number itself the base.

When in doubt, use parentheses to communicate your intention.

------------------------------------------------------------------------

# Part 3 --- How Python evaluates arithmetic

## 10. Order of operations and precedence

### Why precedence exists

Consider:

``` python
2 + 3 * 4
```

There are two possible groupings:

``` text
(2 + 3) * 4 = 20

2 + (3 * 4) = 14
```

Python needs a consistent rule. It follows operator precedence.

### Basic arithmetic precedence

From higher to lower precedence:

  -----------------------------------------------------------------------
  Operators               Meaning                 General grouping
  ----------------------- ----------------------- -----------------------
  `()`                    Parentheses / grouping  Explicitly grouped
                                                  first

  `**`                    Exponentiation          Right to left

  `+x`, `-x`              Unary plus and minus    High precedence; note
                                                  exponent interaction

  `*`, `/`, `//`, `%`     Multiplication,         Left to right
                          division, floor         
                          division, modulo        

  `+`, `-`                Addition, subtraction   Left to right
  -----------------------------------------------------------------------

This is a learning-focused table, not the complete Python
operator-precedence table. Comparisons, Boolean operators, bitwise
operators, and other syntax have additional precedence levels.

### Worked example 1

``` python
result = 2 + 3 * 4
```

Step 1: multiplication has higher precedence than addition.

``` text
2 + 3 * 4
    |
    v
2 + 12
```

Step 2: calculate the remaining addition.

``` text
2 + 12 = 14
```

Result: `14`.

### Worked example 2

``` python
result = 10 - 2 + 3 * 4 / 2
```

Step 1: multiplication and division share the same precedence and group
left to right.

``` text
3 * 4 = 12
12 / 2 = 6.0
```

Step 2: addition and subtraction share the same precedence and group
left to right.

``` text
10 - 2 = 8
8 + 6.0 = 14.0
```

Result: `14.0`.

### Worked example 3: parentheses change the grouping

``` python
a = 2 + 3 * 4
b = (2 + 3) * 4

print(a)  # 14
print(b)  # 20
```

Parentheses are not decoration. They explicitly group an expression.

### Associativity: what happens at equal precedence?

Most arithmetic operators at the same precedence level group left to
right.

``` python
print(10 - 2 - 3)
```

Grouping:

``` python
(10 - 2) - 3
8 - 3
5
```

Exponentiation groups right to left:

``` python
print(2 ** 3 ** 2)  # 512
```

### Engineering habit

Use parentheses when they make the intention easier to read, even when
Python's precedence rules already determine the answer.

``` python
# Correct, but requires the reader to remember precedence.
total = principal * rate ** years + fee

# More explicit.
growth = principal * (rate ** years)
total = growth + fee
```

Do not add parentheses randomly. Use them to clarify meaningful groups.

------------------------------------------------------------------------

## 11. Integer and floating-point values

Python's two common built-in numeric types are:

-   `int`: integers, such as `-4`, `0`, and `27`;
-   `float`: floating-point numbers, such as `3.14`, `-0.5`, and `2.0`.

``` python
whole_number = 10
decimal_number = 10.0

print(type(whole_number))    # <class 'int'>
print(type(decimal_number))  # <class 'float'>
```

The visible mathematical value can be equal while the types differ:

``` python
print(10 == 10.0)  # True
```

Equality of numeric value does not mean identical type.

### Division and result types

``` python
print(10 / 2)       # 5.0
print(type(10 / 2)) # float

print(10 // 2)       # 5
print(type(10 // 2)) # int

print(10.0 // 2)       # 5.0
print(type(10.0 // 2)) # float
```

The type of the result can depend on the operand types.

### Floor division versus truncation

Do not confuse these operations:

-   **Floor:** move down to the greatest integer less than or equal to
    the value.
-   **Truncation:** discard the fractional part, moving toward zero.

For positive numbers, the results can look the same. For negative
numbers, they differ:

``` python
print(-7 // 2)  # -4
print(int(-7 / 2))  # -3
```

Use `//` when you need floor division. Use `int()` only when truncating
toward zero is actually the desired conversion.

------------------------------------------------------------------------

## 12. Floating-point precision: why decimal calculations can surprise you

### The underlying problem

Computers commonly represent `float` values using binary floating-point.
Some decimal fractions cannot be represented exactly in a finite binary
representation.

This is similar to how one-third cannot be written as a finite decimal:

``` text
1 / 3 = 0.3333333333...
```

The binary representation of `0.1` also repeats rather than ending
neatly. A computer stores a nearby representable value.

### Demonstration

``` python
print(0.1 + 0.2)
```

A typical result is:

``` text
0.30000000000000004
```

This is not Python being careless. It is a consequence of
finite-precision binary floating-point representation.

### Why exact equality can fail

``` python
result = 0.1 + 0.2

print(result == 0.3)  # False
```

The two stored floating-point values are not exactly equal.

### Solution 1: compare with a tolerance

``` python
result = 0.1 + 0.2
expected = 0.3
tolerance = 1e-9

if abs(result - expected) < tolerance:
    print("Close enough")
```

`abs()` returns the absolute value: the distance from zero without a
negative sign.

For general-purpose floating-point comparisons, Python provides
`math.isclose()`:

``` python
import math

print(math.isclose(0.1 + 0.2, 0.3))
```

Its default relative and absolute tolerances are designed for common
numerical comparisons. For a particular application, choose tolerances
appropriate to the scale and meaning of the values.

### Solution 2: use `Decimal` for decimal arithmetic

``` python
from decimal import Decimal

price_a = Decimal("19.99")
price_b = Decimal("29.99")

total = price_a + price_b
print(total)  # 49.98
```

Construct `Decimal` from strings when you need the intended decimal
value.

Avoid this for exact decimal input:

``` python
Decimal(0.1)
```

That captures the already-approximated binary float value. Prefer:

``` python
Decimal("0.1")
```

### Solution 3: use integer minor units

For a simple currency model with two decimal places, store the smallest
unit as an integer:

``` python
price_a_kobo = 1999
price_b_kobo = 2999

total_kobo = price_a_kobo + price_b_kobo
print(total_kobo)  # 4998
```

This avoids floating-point rounding in the addition. The currency's
actual minor-unit rules must be understood; not every currency uses two
decimal places.

### Rounding is a business decision

``` python
value = 2.675
print(round(value, 2))
```

The result may surprise beginners because the input is a binary float
approximation. Python's `round()` also uses ties-to-even for exact
halfway cases.

For financial calculations, define: - the currency and its minor unit; -
when rounding occurs; - how halfway cases are handled; - whether
rounding is applied per item, per line, or to the final total.

With `Decimal`, make the rounding policy explicit:

``` python
from decimal import Decimal, ROUND_HALF_UP

amount = Decimal("2.675")
rounded = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(rounded)  # 2.68
```

Do not assume one rounding rule is correct for every business or
jurisdiction.

------------------------------------------------------------------------

## 13. Compound assignment operators

Compound assignment combines an operation with assignment.

### Ordinary assignment

``` python
balance = 100
balance = balance + 25
print(balance)  # 125
```

### Compound assignment

``` python
balance = 100
balance += 25
print(balance)  # 125
```

For a simple integer variable, `balance += 25` expresses the same
intended update as `balance = balance + 25`.

### Common compound operators

  Operator   Example     General meaning
  ---------- ----------- --------------------------
  `+=`       `x += 2`    Add 2 to `x`
  `-=`       `x -= 2`    Subtract 2 from `x`
  `*=`       `x *= 2`    Multiply `x` by 2
  `/=`       `x /= 2`    Divide `x` by 2
  `//=`      `x //= 2`   Floor-divide `x` by 2
  `%=`       `x %= 2`    Store the modulo result
  `**=`      `x **= 2`   Raise `x` to the power 2

### Worked example

``` python
score = 10

score += 5   # 15
score -= 3   # 12
score *= 2   # 24
score //= 4  # 6

print(score)  # 6
```

### Common uses

**Counter:**

``` python
count = 0

for item in ["a", "b", "c"]:
    count += 1
```

**Running total:**

``` python
total = 0

for amount in [100, 250, 50]:
    total += amount
```

**Balance updates:**

``` python
balance = 1000
balance += 200  # deposit
balance -= 75   # withdrawal
```

### A technical nuance

For immutable numeric values, compound assignment usually behaves as
beginners expect. For mutable objects, augmented assignment may modify
an object in place rather than create a new one. Therefore, `x += y` is
not universally identical in every detail to `x = x + y`.

Example:

``` python
numbers = [1, 2]
alias = numbers

numbers += [3]

print(numbers)  # [1, 2, 3]
print(alias)    # [1, 2, 3]
```

The list was modified in place, so both names still refer to the same
list.

------------------------------------------------------------------------

# Part 4 --- Thinking like a programmer

## 14. Trace an expression before running it

A trace is a written record of how values change as a program executes.

Consider:

``` python
total = 10
total += 5
total *= 2
total -= 4

print(total)
```

Trace table:

  Step   Statement        Value of `total`
  ------ -------------- ------------------
  1      `total = 10`                   10
  2      `total += 5`                   15
  3      `total *= 2`                   30
  4      `total -= 4`                   26

Output:

``` text
26
```

### A disciplined prediction method

Before running a program:

1.  Identify each variable.
2.  Write down its initial value.
3.  Read statements from top to bottom.
4.  Evaluate the right-hand side first.
5.  Update the variable only when assignment occurs.
6.  Track the data type when division or conversion is involved.
7.  Predict the output.
8.  Run the code and compare.

### Trace a more complex expression

``` python
a = 8
b = 3
result = a + b * 2 ** 2
```

Order:

1.  `2 ** 2` becomes `4`.
2.  `b * 4` becomes `12`.
3.  `a + 12` becomes `20`.
4.  `result` receives `20`.

------------------------------------------------------------------------

## 15. Arithmetic, assignment, and comparison are different

Beginners sometimes confuse these symbols:

  Symbol   Meaning               Example
  -------- --------------------- ----------
  `=`      Assignment            `x = 5`
  `==`     Equality comparison   `x == 5`
  `+`      Addition              `x + 2`
  `+=`     Add and assign        `x += 2`

Example:

``` python
x = 5       # store 5
x == 5      # evaluate to True
x = x + 2   # calculate and store 7
```

`x == 5` does not change `x`. It produces a Boolean value (`True` or
`False`).

------------------------------------------------------------------------

## 16. Arithmetic errors and debugging

An arithmetic bug is not always a Python exception. A program can run
successfully and still calculate the wrong answer.

### Error category 1: division by zero

Problem:

``` python
total = 100
count = 0
average = total / count
```

Python raises `ZeroDivisionError`.

Debugging approach: - Find the denominator. - Determine whether it can
be zero. - Decide what zero should mean in the application. - Validate
before dividing.

``` python
if count == 0:
    average = None
else:
    average = total / count
```

`None` means no average is available. Another application may prefer an
error message or a different result.

### Error category 2: wrong operator

Problem:

``` python
price = 50
quantity = 3
total = price + quantity  # 53, probably not intended
```

Correct:

``` python
total = price * quantity  # 150
```

The original code is syntactically valid. The problem is the
programmer's logic.

### Error category 3: accidental integer-style thinking

Problem:

``` python
distance = 10
time = 3
speed = distance // time
```

This gives `3`, not the more precise rate.

Correct for a decimal rate:

``` python
speed = distance / time
```

### Error category 4: incorrect order of operations

Problem:

``` python
subtotal = 100
tax_rate = 0.10
tax = subtotal + tax_rate * subtotal
```

This expression is mathematically valid, but a beginner may
misunderstand its grouping.

Make the intent explicit:

``` python
tax = subtotal * tax_rate
total = subtotal + tax
```

### Error category 5: floating-point equality

Problem:

``` python
if 0.1 + 0.2 == 0.3:
    print("Equal")
else:
    print("Not equal")
```

Use `math.isclose()` for approximate floating-point comparisons, or
choose an exact decimal/integer representation where appropriate.

### Error category 6: invalid assumptions about input

Problem:

``` python
amount = input("Enter amount: ")
total = amount + 10
```

`input()` returns a string. Convert and validate:

``` python
raw_amount = input("Enter amount: ")

try:
    amount = int(raw_amount)
except ValueError:
    print("Please enter a whole number.")
else:
    total = amount + 10
    print(total)
```

For decimal values, consider `Decimal` and validate the accepted input
format.

### Debugging checklist

When a calculation is wrong, ask:

-   Are the operands the values I expect?
-   Are their types correct?
-   Did I choose the correct operator?
-   Did I account for precedence?
-   Did I assign the result?
-   Could the denominator be zero?
-   Could a negative value occur?
-   Am I losing a remainder?
-   Am I comparing floats exactly?
-   Have I tested boundary values such as zero, one, negatives, and very
    large numbers?

------------------------------------------------------------------------

# Part 5 --- Practical applications

## 17. Application: calculate a shopping bill

Requirements:

-   Accept a unit price and quantity.
-   Calculate the subtotal.
-   Apply a percentage discount.
-   Calculate the final amount.
-   Display each stage clearly.

Learning version using simple numeric values:

``` python
unit_price = 25
quantity = 4
discount_rate = 0.10

subtotal = unit_price * quantity
discount = subtotal * discount_rate
final_total = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final total:", final_total)
```

Expected output:

``` text
Subtotal: 100
Discount: 10.0
Final total: 90.0
```

### Trace

  Variable          Calculation      Value
  ----------------- -------------- -------
  `unit_price`      Given               25
  `quantity`        Given                4
  `subtotal`        `25 * 4`           100
  `discount_rate`   Given             0.10
  `discount`        `100 * 0.10`      10.0
  `final_total`     `100 - 10.0`      90.0

### Improve it

Add validation:

``` python
unit_price = 25
quantity = 4
discount_rate = 0.10

if unit_price < 0:
    print("Price cannot be negative.")
elif quantity < 0:
    print("Quantity cannot be negative.")
elif not 0 <= discount_rate <= 1:
    print("Discount rate must be between 0 and 1.")
else:
    subtotal = unit_price * quantity
    discount = subtotal * discount_rate
    final_total = subtotal - discount

    print(f"Subtotal: {subtotal}")
    print(f"Discount: {discount}")
    print(f"Final total: {final_total}")
```

A real application should also define whether zero quantity is allowed,
whether fractional quantities are permitted, and how monetary rounding
works.

------------------------------------------------------------------------

## 18. Application: a simple account balance

This is a learning exercise, not a production banking system.

``` python
balance = 1000

deposit = 250
balance += deposit

withdrawal = 100
balance -= withdrawal

print("Final balance:", balance)
```

Expected result:

``` text
Final balance: 1150
```

### Add a withdrawal rule

``` python
balance = 1000
withdrawal = 1200

if withdrawal <= 0:
    print("Withdrawal must be greater than zero.")
elif withdrawal > balance:
    print("Insufficient funds.")
else:
    balance -= withdrawal
    print("Withdrawal successful.")
    print("Balance:", balance)
```

Notice the separation:

-   Arithmetic calculates the new balance.
-   Conditions enforce business rules.
-   Output communicates the result.

A production financial application needs much more: exact monetary
representation, authentication, authorization, transaction records,
concurrency control, audit trails, and secure persistence.

------------------------------------------------------------------------

## 19. Application: time conversion

Suppose a program receives a number of seconds and must calculate
complete hours, minutes, and remaining seconds.

``` python
total_seconds = 7384

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")
```

Expected output:

``` text
2 hours
3 minutes
4 seconds
```

### Why these operators?

-   `//` calculates complete hours or minutes.
-   `%` keeps the remainder for the next calculation.

### Visual decomposition

``` text
7384 seconds
    |
    | // 3600
    v
2 complete hours
    |
    | % 3600
    v
184 seconds remaining
    |
    | // 60
    v
3 complete minutes
    |
    | % 60
    v
4 seconds remaining
```

The original quantity is reconstructed as:

``` text
(2 * 3600) + (3 * 60) + 4 = 7384
```

------------------------------------------------------------------------

# Part 6 --- Mastery exercises

## 20. Predict the output

Try these without running the code first. Write down your reasoning, not
only the final answer.

### Exercise 1: basic operators

``` python
a = 12
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Questions: - How many lines are printed? - What is each result? - Which
result is a float?

### Exercise 2: floor division and modulo

``` python
print(23 // 5)
print(23 % 5)
```

Explain how the two results fit together.

### Exercise 3: precedence

``` python
result = 4 + 3 * 2 ** 2
print(result)
```

Show every evaluation step.

### Exercise 4: parentheses

``` python
first = (4 + 3) * 2
second = 4 + 3 * 2

print(first)
print(second)
```

Why are the results different?

### Exercise 5: variable updates

``` python
number = 5
number += 3
number *= 2
number -= 4

print(number)
```

Create a trace table.

### Exercise 6: negative floor division

``` python
print(-7 // 2)
print(-7 % 2)
```

Verify the relationship:

``` python
a == (a // b) * b + (a % b)
```

### Exercise 7: exponent grouping

``` python
print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
```

Explain why the outputs differ.

### Exercise 8: type prediction

``` python
a = 10
b = 2

print(type(a / b))
print(type(a // b))
print(type(10.0 // 2))
```

Predict all three types.

------------------------------------------------------------------------

## 21. Debugging challenges

For each challenge:

1.  State what the programmer probably intended.
2.  Identify the problem.
3.  Explain why the current code behaves as it does.
4.  Correct the code.
5.  Test at least one normal case and one edge case.

### Challenge 1: wrong total

``` python
price = 40
quantity = 5

total = price + quantity
print(total)
```

The expected bill is the price multiplied by the quantity.

### Challenge 2: division by zero

``` python
total_score = 0
number_of_students = 0

average = total_score / number_of_students
print(average)
```

Make the program handle the empty-class case safely.

### Challenge 3: missing assignment

``` python
balance = 500
balance - 100

print(balance)
```

The programmer expects the balance to become 400.

### Challenge 4: wrong page calculation

``` python
items = 101
items_per_page = 10

pages = items // items_per_page
print(pages)
```

The program must calculate the number of pages required to show every
item.

### Challenge 5: float comparison

``` python
if 0.1 + 0.2 == 0.3:
    print("Correct")
else:
    print("Unexpected result")
```

Rewrite the comparison using an appropriate floating-point strategy.

### Challenge 6: negative inventory

``` python
stock = 4
sold = 7

stock -= sold
print(stock)
```

Prevent the application from selling more items than it has.

------------------------------------------------------------------------

## 22. Practical mini-project: Sales and inventory calculator

### Project objective

Build a small command-line program that calculates a sales transaction
and updates inventory.

### Requirements

The program should:

1.  Start with a known stock quantity.
2.  Store a unit price.
3.  Receive a requested sales quantity.
4.  Reject a quantity that is zero or negative.
5.  Reject a sale larger than available stock.
6.  Calculate the subtotal using multiplication.
7.  Calculate a discount using a percentage.
8.  Calculate the final total using subtraction.
9.  Update stock only after validation succeeds.
10. Display the transaction summary and remaining stock.

### Suggested starting values

``` python
stock = 20
unit_price = 150
discount_rate = 0.10
```

### Suggested program structure

``` python
# 1. Store initial values

# 2. Get the requested quantity

# 3. Validate the quantity

# 4. Calculate subtotal

# 5. Calculate discount

# 6. Calculate final total

# 7. Update stock

# 8. Display the summary
```

### Test cases

  Test                  Requested quantity Expected behaviour
  ------------------- -------------------- -----------------------------------
  Normal sale                            3 Calculate sale and reduce stock
  Sell all stock                        20 Accept if the business permits it
  More than stock                       21 Reject; stock remains unchanged
  Zero quantity                          0 Reject
  Negative quantity                     -2 Reject

### Engineering questions

-   Why should validation happen before stock is updated?
-   What happens if the program updates stock and then discovers an
    invalid discount?
-   Why is multiplication appropriate for subtotal?
-   Why is subtraction appropriate for remaining stock?
-   What numeric representation would you choose for real currency?
-   How would you preserve the transaction if the program closes?

### Extension

Add multiple products, a list of transaction records, and a final report
containing total sales and remaining inventory.

------------------------------------------------------------------------

# Part 7 --- Interview and project-defense questions

## 23. Concept questions

Answer in your own words before reading documentation.

1.  What is an arithmetic operator?
2.  What is the difference between an operator and an operand?
3.  What is an expression?
4.  What is the difference between `=` and `==`?
5.  What is the difference between `/` and `//`?
6.  What does `%` return?
7.  Why can modulo be useful for checking even numbers?
8.  What does `**` do?
9.  What is operator precedence?
10. What is associativity?
11. Why do parentheses matter?
12. Why does `10 / 2` produce `5.0` in Python 3?
13. What is the difference between an integer and a float?
14. Why can `0.1 + 0.2` produce an unexpected-looking result?
15. What is compound assignment?

## 24. Deeper engineering questions

1.  Why is `//` not always equivalent to removing the decimal portion?
2.  Why does `-7 // 2` produce `-4`?
3.  How does Python's modulo operation behave with negative divisors?
4.  Why should floating-point values generally not be compared using
    exact equality?
5.  When would you choose `Decimal` instead of `float`?
6.  When would storing money as integer minor units be appropriate?
7.  Why is `Decimal("0.1")` preferable to `Decimal(0.1)` for decimal
    input?
8.  Why should rounding policy be defined in a financial application?
9.  Why can a program produce a wrong financial result without raising
    an exception?
10. Why must business validation be separate from arithmetic
    calculation?

## 25. Explain your code

Use the sales and inventory project.

Be prepared to explain:

-   Why you chose each arithmetic operator.
-   How the subtotal is calculated.
-   How the discount is calculated.
-   How the final amount is calculated.
-   How the remaining stock is calculated.
-   How you prevent invalid transactions.
-   What happens when quantity is zero.
-   What happens when requested quantity exceeds stock.
-   How you would test the calculations.
-   How you would make monetary calculations more reliable.

### A strong defense answer structure

When explaining a calculation, use this sequence:

1.  **Purpose:** What problem am I solving?
2.  **Inputs:** Which values are needed?
3.  **Operation:** Which operator or formula is appropriate?
4.  **Reason:** Why is that operation appropriate?
5.  **Result:** What value should be produced?
6.  **Validation:** What invalid inputs or edge cases exist?
7.  **Testing:** How did I confirm the calculation?

------------------------------------------------------------------------

# Part 8 --- Answer key and explanations

Do not read this section until you have attempted the exercises.

## 26. Predict-the-output answers

### Exercise 1

``` text
16
8
48
3.0
```

There are four `print()` calls, so four lines are printed. `/` produces
a float.

### Exercise 2

``` text
4
3
```

Because:

``` text
23 = (5 * 4) + 3
```

There are four complete groups of five and three remaining.

### Exercise 3

``` text
16
```

Evaluation:

``` text
2 ** 2 = 4
3 * 4 = 12
4 + 12 = 16
```

### Exercise 4

``` text
14
10
```

The first expression groups `4 + 3` before multiplication. The second
performs multiplication before addition.

### Exercise 5

``` text
12
```

Trace:

  Step   Operation         Value
  ------ --------------- -------
  1      `number = 5`          5
  2      `number += 3`         8
  3      `number *= 2`        16
  4      `number -= 4`        12

### Exercise 6

``` text
-4
1
```

Verification:

``` text
-7 = (-4 * 2) + 1
-7 = -8 + 1
-7 = -7
```

### Exercise 7

``` text
512
64
```

The exponent operator groups from right to left unless parentheses
specify otherwise.

### Exercise 8

``` text
<class 'float'>
<class 'int'>
<class 'float'>
```

True division returns a float. Floor division with integer operands
returns an integer; a float operand gives a float result.

## 27. Debugging challenge guidance

### Challenge 1

Use multiplication:

``` python
total = price * quantity
```

### Challenge 2

Check the denominator before division:

``` python
if number_of_students == 0:
    print("No students to calculate an average for.")
else:
    average = total_score / number_of_students
    print(average)
```

### Challenge 3

Store the result:

``` python
balance = balance - 100
```

or:

``` python
balance -= 100
```

### Challenge 4

Use a ceiling-division formula for positive item counts and positive
page sizes:

``` python
pages = (items + items_per_page - 1) // items_per_page
```

For `101` items and `10` per page, the result is `11`.

### Challenge 5

Use `math.isclose()`:

``` python
import math

if math.isclose(0.1 + 0.2, 0.3):
    print("Close enough")
else:
    print("Different")
```

### Challenge 6

Validate before changing stock:

``` python
if sold <= 0:
    print("Quantity must be greater than zero.")
elif sold > stock:
    print("Not enough stock.")
else:
    stock -= sold
    print("Remaining stock:", stock)
```

------------------------------------------------------------------------

# Part 9 --- Final mastery checklist

## 28. Can you do these independently?

Use this checklist to assess your understanding honestly.

### Foundations

-   [ ] I can explain what an operator is.
-   [ ] I can identify operands in an expression.
-   [ ] I can distinguish an expression from an assignment.
-   [ ] I understand that calculating a value does not automatically
    store it.

### Operators

-   [ ] I can explain addition and subtraction.
-   [ ] I can explain multiplication and division.
-   [ ] I can distinguish true division from floor division.
-   [ ] I can calculate a remainder using modulo.
-   [ ] I can explain exponentiation.
-   [ ] I can use compound assignment.

### Python behaviour

-   [ ] I understand `int` and `float`.
-   [ ] I can predict arithmetic result types.
-   [ ] I understand floor division with negative numbers.
-   [ ] I can explain Python's negative modulo behaviour.
-   [ ] I can apply precedence and associativity.
-   [ ] I understand floating-point precision limitations.

### Practical engineering

-   [ ] I can trace a multi-step calculation.
-   [ ] I can identify division-by-zero risks.
-   [ ] I can validate inputs before updating data.
-   [ ] I can choose a suitable representation for money.
-   [ ] I can debug a calculation that runs but produces the wrong
    answer.
-   [ ] I can defend the arithmetic decisions in my mini-project.

## 29. Self-assessment scale

  -----------------------------------------------------------------------
  Level                               Evidence of understanding
  ----------------------------------- -----------------------------------
  1 --- Recognition                   I recognize the operators but need
                                      help using them.

  2 --- Basic                         I can solve simple examples with
                                      guidance.

  3 --- Working                       I can solve familiar problems
                                      independently.

  4 --- Strong                        I can trace, debug, and explain
                                      unfamiliar examples.

  5 --- Mastery                       I can choose appropriate
                                      operations, handle edge cases, test
                                      my work, and defend my design
                                      decisions.
  -----------------------------------------------------------------------

Do not rate yourself based on how much of the document you have read.
Rate yourself based on what you can do without copying.

------------------------------------------------------------------------

# Part 10 --- Technical reference

## 30. Arithmetic operator summary

  Operator   Name             Example      Result
  ---------- ---------------- ---------- --------
  `+`        Addition         `5 + 3`         `8`
  `-`        Subtraction      `5 - 3`         `2`
  `*`        Multiplication   `5 * 3`        `15`
  `/`        True division    `5 / 2`       `2.5`
  `//`       Floor division   `5 // 2`        `2`
  `%`        Modulo           `5 % 2`         `1`
  `**`       Exponentiation   `5 ** 2`       `25`

## 31. Useful built-in functions and modules

  --------------------------------------------------------------------------------
  Tool                    Purpose                 Example
  ----------------------- ----------------------- --------------------------------
  `abs()`                 Absolute value          `abs(-5)` gives `5`

  `round()`               Round a number          `round(3.14159, 2)`

  `sum()`                 Add values in an        `sum([1, 2, 3])`
                          iterable                

  `min()`                 Find the smallest value `min(4, 2, 8)`

  `max()`                 Find the largest value  `max(4, 2, 8)`

  `type()`                Inspect a value's type  `type(3.5)`

  `math.isclose()`        Compare floats          `math.isclose(0.1 + 0.2, 0.3)`
                          approximately           

  `decimal.Decimal`       Decimal arithmetic      `Decimal("19.99")`
  --------------------------------------------------------------------------------

## 32. Final mental model

Arithmetic in programming is more than memorizing symbols.

A capable programmer understands the full chain:

``` text
Real-world problem
       |
       v
Identify the required values
       |
       v
Choose the correct mathematical operation
       |
       v
Write a Python expression
       |
       v
Understand precedence and data types
       |
       v
Evaluate and store the result
       |
       v
Validate the result against the rules
       |
       v
Test normal cases and edge cases
       |
       v
Explain and defend the implementation
```

**The goal is not to remember that `*` means multiplication. The goal is
to recognize when multiplication models the problem correctly, use it
safely, verify the result, and explain why your implementation is
correct.**

------------------------------------------------------------------------

## Accuracy notes and further study

This guide describes core Python arithmetic behaviour. For a deeper
reference, consult the official Python documentation:

-   [Python numeric types --- `int`, `float`, and
    `complex`](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
-   [Python expressions and operator
    precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
-   [Python floating-point arithmetic: issues and
    limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
-   [The `decimal`
    module](https://docs.python.org/3/library/decimal.html)
-   [The `math` module](https://docs.python.org/3/library/math.html)

These references provide the formal language and detailed behaviour
behind the beginner-friendly mental models in this document.
