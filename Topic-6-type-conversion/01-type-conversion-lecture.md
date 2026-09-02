# Topic 5: Type Conversion - Transforming Between Data Types

## Goal

**Learn how to convert data between different types: strings to numbers, numbers to strings, and other transformations. Understand that Python provides explicit conversion functions. Master the concept that different types have different capabilities and representations.**

---

## Why This Matters - The Real Problem

You've learned three data types: strings, integers, and floats. But they don't work together automatically.

Real problems require **type conversion**:
- User enters age (string) → Need it as number for calculations
- Calculate price (float) → Need it as string for display
- Read temperature (string from file) → Need it as number for comparison
- Store year (integer) → Need it as string for formatting
- Get yes/no answer (string) → Need it as boolean for logic

Without type conversion, your programs can't exchange data between types.

**Examples of conversion needs:**
```python
# User input is always text
age = input("Age: ")  # "25" (text)
next_year = int(age) + 1  # Convert to do math

# Numbers need to be text for display
price = 19.99  # Float
display = f"Price: ${str(price)}"  # Convert for display

# Validation often needs conversion
response = input("Continue? (yes/no): ")  # "yes" (text)
should_continue = response.lower() == "yes"  # Convert to boolean logic
```

Type conversion is essential for almost every real program.

---

## Mental Model 1: Why Types Are Different (The Capability Model)

Different types have different **capabilities** and **operations**.

**Strings (Text):**
- Operations: concatenation, slicing, searching
- Can contain any characters
- Not suitable for math

**Integers (Whole Numbers):**
- Operations: addition, subtraction, multiplication, division
- Can do comparisons
- Don't have decimal points

**Floats (Decimal Numbers):**
- Operations: all math operations
- Can have decimal points
- Need precision handling

**Booleans (True/False):**
- Operations: logical (and, or, not)
- Two possible values only
- Used in conditions

You convert when you need **different capabilities**:

```python
# String: can't do math
text = "25"
text + 5  # ERROR

# Convert to number: now can do math
number = int(text)
number + 5  # 30 (works)

# Convert back to string: now can do text operations
display = str(number) + " items"  # "30 items"
```

**Key insight:** Conversion lets you use the right type for the right task.

---

## Mental Model 2: String to Integer - Reading Numbers from Text

This is the most common conversion.

User input is text, but often contains numbers. You must explicitly convert.

```python
age_text = input("Age: ")  # Returns: "25" (text)
age = int(age_text)        # Convert: 25 (integer)
```

**What int() does:**

```
Input: "25" (string)
↓
Examines each character: '2', '5'
↓
Checks if all are digits: yes
↓
Interprets as number: 25
↓
Returns: 25 (integer)
```

**What if it fails?**

```python
int("abc")      # ERROR: ValueError (not a number)
int("25.5")     # ERROR: ValueError (has decimal point)
int("25 ")      # ERROR: ValueError (has space)
```

**Safe conversion:**

```python
text = input("Number: ")
text = text.strip()  # Remove spaces

try:
    number = int(text)
except ValueError:
    print("Not a valid integer")
    number = 0
```

---

## Mental Model 3: String to Float - Reading Decimals from Text

Similar to int(), but handles decimal points.

```python
price_text = input("Price: ")  # Returns: "19.99"
price = float(price_text)      # Returns: 19.99
```

**What float() does:**

```
Input: "19.99" (string)
↓
Examines: '1', '9', '.', '9', '9'
↓
Checks if valid number: yes
↓
Interprets as decimal: 19.99
↓
Returns: 19.99 (float)
```

**Differences from int():**

```python
int("25.5")     # ERROR - can't interpret decimal point
float("25.5")   # 25.5 (works - understands decimals)
float("25")     # 25.0 (works - converts integers too)
int("25")       # 25 (works)
```

**When to use which:**

- Use `int()` for whole numbers: age, count, ID
- Use `float()` for decimals: price, temperature, measurements

---

## Mental Model 4: Number to String - Displaying Numbers

To display numbers or concatenate them with text, convert to string.

```python
age = 25
print("Age: " + str(age))  # Convert number to string
```

**What str() does:**

```
Input: 25 (integer)
↓
Represents as text: "25"
↓
Returns: "25" (string)
```

**Examples:**

```python
num = 42
str(num)           # "42"
str(3.14)          # "3.14"
str(True)          # "True"
str([1, 2, 3])     # "[1, 2, 3]"
```

**Why you need it:**

```python
# Without conversion
number = 25
text = "The number is " + number  # ERROR

# With conversion
number = 25
text = "The number is " + str(number)  # "The number is 25"
```

---

## Mental Model 5: Bool Conversion - Creating Logic (Boolean Model)

Converting to boolean (True/False) is crucial for conditions.

**Explicit conversion:**

```python
bool(1)      # True
bool(0)      # False
bool("text") # True
bool("")     # False
bool([1,2])  # True
bool([])     # False
```

**Pattern:**
- Most values are `True`
- Only "empty" values are `False`:
  - `0` (zero)
  - `""` (empty string)
  - `[]` (empty list)
  - `None` (nothing)
  - `False` itself

**Example use:**

```python
response = input("Continue? (yes/no): ")
should_continue = bool(response)  # True if non-empty, False if empty

# More commonly:
should_continue = response.lower() == "yes"  # Explicit comparison
```

---

## Mental Model 6: Chaining Conversions (Transformation Pipeline)

Often you convert multiple times in sequence.

```python
user_input = input("Price: ")           # "19.99" (string)
price = float(user_input)               # 19.99 (float)
price_increased = price * 1.1           # 21.989 (float)
display = f"${price_increased:.2f}"     # "$21.99" (string)
```

**Visual flow:**

```
User Input (string)
    ↓ float()
Float (decimal)
    ↓ * 1.1
Float (calculated)
    ↓ str() / format
String (display-ready)
    ↓
User sees it
```

**Another example:**

```python
age_text = input("Age: ")      # "25" (string)
age = int(age_text)            # 25 (integer)
next_year = age + 1            # 26 (integer)
message = f"Next year: {next_year}"  # "Next year: 26" (string)
```

---

## Mental Model 7: Implicit vs Explicit Conversion (When Python Helps)

Python sometimes converts automatically (implicit).

```python
result = 5 + 2.5  # Integer + Float
# Python automatically converts to: 5.0 + 2.5 = 7.5
print(result)  # 7.5 (float)
```

**But usually you must be explicit:**

```python
"5" + 2  # ERROR - Python won't auto-convert
```

**Best practice:** Always be explicit.

```python
"5" + str(2)    # "52" (explicit conversion)
int("5") + 2    # 7 (explicit conversion)
```

**Why explicit is better:**
- Makes intent clear
- Prevents silent bugs
- Shows you know what you're doing

---

## Mental Model 8: Type Information and type() Function

Python tracks the type of every value.

```python
value = 25
print(type(value))  # <class 'int'>

value = "25"
print(type(value))  # <class 'str'>

value = 25.0
print(type(value))  # <class 'float'>
```

**Use type() to verify conversions:**

```python
text = input("Age: ")
print(f"Input type: {type(text)}")  # <class 'str'>

age = int(text)
print(f"After conversion: {type(age)}")  # <class 'int'>
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Why Does int('25.5') Fail?"

**The question:** If 25.5 is a number, why can't int() handle it?

**The answer:** int() reads the string character by character.

```
Input: "25.5"
Character 1: '2' → OK, it's a digit
Character 2: '5' → OK, it's a digit
Character 3: '.' → ERROR! This isn't a digit
Character 4: '5' → Can't reach here
Result: ValueError
```

int() doesn't understand decimals because they have decimal points.

**Solution:**

```python
float("25.5")  # Works (float understands decimals)
int(float("25.5"))  # Convert to float first, then int (result: 25)
```

### Confusion 2: "What's the Difference Between int() and float()?"

**The question:** When should I use which?

**The answer:**
- `int()` for whole numbers
- `float()` for decimals

```python
age = int(input("Age: "))           # Whole number
height = float(input("Height (m): "))  # Decimal
```

**Key difference:**

```python
int("42")      # 42 (whole)
float("42")    # 42.0 (decimal)
int("42.9")    # ERROR
float("42.9")  # 42.9 (works)
```

### Confusion 3: "What if Conversion Fails?"

**The question:** What happens if int("abc")?

**The answer:** Raises ValueError (program crashes unless caught).

```python
int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
```

**Prevent crashes with try/except:**

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Not a valid number")
    number = 0
```

### Confusion 4: "Why Is 0 False But 1 True?"

**The question:** Why these specific values for boolean conversion?

**The answer:** Computer science convention.

```
0 = False (zero is empty, nothing)
1 = True (one is present, something)
```

This comes from:
- Binary (0 and 1)
- Counting (nothing vs something)
- Logic (off vs on, false vs true)

**Pattern:** Empty = False, Non-empty = True

```python
bool(0)      # False (empty)
bool(1)      # True (present)
bool(100)    # True (present)
bool("")     # False (empty string)
bool("text") # True (non-empty)
```

### Confusion 5: "Can I Convert Anything?"

**The question:** Can I convert any value to any type?

**The answer:** Not always.

```python
str(25)        # "25" (works)
int(25.9)      # 25 (works, truncates decimal)
float("abc")   # ERROR (can't interpret as number)
int([1, 2])    # ERROR (can't convert list to int)
```

**Conversions that work:**
- String to number (if string contains valid number)
- Number to string (always works)
- Any value to boolean (always works)
- Number to different number type (int ↔ float)

**Conversions that fail:**
- Non-numeric string to number
- Complex types to simple types
- Lists/dicts to numbers

---

## How Type Conversion Works Internally (Mechanisms)

**String to Integer:**

```
int("123")

Step 1: PARSE STRING
  Examine character by character
  '1', '2', '3'

Step 2: VALIDATE
  Check if all are digits
  Check for invalid characters
  If invalid: raise ValueError

Step 3: CONVERT
  Interpret as numeric value
  1 * 100 + 2 * 10 + 3 * 1 = 123

Step 4: RETURN
  Return: 123 (integer)
```

**Number to String:**

```
str(123)

Step 1: IDENTIFY TYPE
  Value is integer: 123

Step 2: REPRESENT
  Convert to text representation: "123"

Step 3: RETURN
  Return: "123" (string)
```

---

## Real-World Conversion Scenarios

**E-commerce price calculation:**

```python
price_text = input("Price: ")           # "19.99"
price = float(price_text)               # 19.99
quantity = int(input("Quantity: "))     # 5
tax_rate = 0.08

total = price * quantity * (1 + tax_rate)  # 107.964
display = f"${total:.2f}"               # "$107.96"
```

**Temperature conversion:**

```python
celsius_text = input("Celsius: ")       # "25"
celsius = float(celsius_text)           # 25.0
fahrenheit = (celsius * 9/5) + 32       # 77.0
print(f"{celsius}°C = {fahrenheit}°F")  # "25.0°C = 77.0°F"
```

**User validation:**

```python
age_text = input("Age: ")
age = int(age_text)
is_adult = age >= 18                    # Boolean
print(f"Can vote: {is_adult}")           # True/False
```

---

## Summary - The Big Picture

**What you learned:**
1. Different types have different capabilities
2. Conversion functions: int(), float(), str(), bool()
3. String to number conversion is most common
4. Conversions can fail (must handle errors)
5. Chaining conversions for complex workflows
6. type() shows the current type of a value
7. Explicit conversion is safer than relying on implicit
8. Most values convert to True, only empty to False

**Why this matters:**
- Almost all programs need type conversion
- User input is always text but often needs numbers
- Numbers need conversion to strings for display
- Type mismatches are common error source
- Understanding conversions prevents bugs

**What's next:**
Now you can work with different types. But what if you need to do math?

Topic 6 teaches **Arithmetic** - mathematical operations, operators, and calculations.

---

## What You Should Be Able To Do Now

✅ Convert strings to integers
✅ Convert strings to floats
✅ Convert numbers to strings
✅ Convert any value to boolean
✅ Use type() to check types
✅ Handle conversion errors
✅ Chain conversions together
✅ Know when conversions fail
✅ Design input validation with conversions
✅ Explain why conversion is necessary

