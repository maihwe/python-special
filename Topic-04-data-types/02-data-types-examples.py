# Topic 4: Data Types - Elaborate Examples
# Comprehensive examples of Python's basic data types in action

# ============================================================================
# EXAMPLE 1: Identifying Types - type() Function
# ============================================================================
# Every value has a type. Use type() to see what it is.

print("Example 1: Identifying Data Types with type()")
print("-" * 50)

values = [
    42,                    # integer
    3.14,                  # float
    "hello",               # string
    True,                  # boolean
    None,                  # none type
    [1, 2, 3],            # list (preview)
]

for value in values:
    type_name = type(value).__name__
    print(f"Value: {repr(value):20} → Type: {type_name}")

print()

# ============================================================================
# EXAMPLE 2: Integers - Whole Numbers
# ============================================================================
# Integers are whole numbers (positive, negative, or zero)

print("Example 2: Integer Type Properties")
print("-" * 50)

numbers = [0, 42, -5, 1_000_000, -999]
print("Integer examples:")
for num in numbers:
    print(f"  {num:15} (type: {type(num).__name__})")

print()
print("Operations on integers:")
a, b = 10, 3
print(f"  {a} + {b} = {a + b}")
print(f"  {a} - {b} = {a - b}")
print(f"  {a} * {b} = {a * b}")
print(f"  {a} // {b} = {a // b}  (integer division)")
print(f"  {a} % {b} = {a % b}   (remainder)")
print(f"  {a} ** {b} = {a ** b}  (exponent)")
print()

# ============================================================================
# EXAMPLE 3: Floats - Decimal Numbers
# ============================================================================
# Floats represent decimal numbers

print("Example 3: Float Type Properties")
print("-" * 50)

floats = [0.0, 3.14, -2.5, 1e-5, 1.23e3]
print("Float examples:")
for num in floats:
    print(f"  {num:15} (type: {type(num).__name__})")

print()
print("Float arithmetic:")
x, y = 10.5, 3.2
print(f"  {x} + {y} = {x + y}")
print(f"  {x} - {y} = {x - y}")
print(f"  {x} * {y} = {x * y}")
print(f"  {x} / {y} = {x / y}")
print()

# ============================================================================
# EXAMPLE 4: Strings - Text Data
# ============================================================================
# Strings represent text

print("Example 4: String Type Properties")
print("-" * 50)

strings = [
    "hello",
    'world',
    "123",
    "",
    "hello world",
]
print("String examples:")
for s in strings:
    print(f"  {repr(s):20} (length: {len(s)}, type: {type(s).__name__})")

print()
print("String operations:")
s1 = "hello"
s2 = "world"
print(f"  '{s1}' + ' ' + '{s2}' = '{s1} {s2}'  (concatenation)")
print(f"  '{s1}' * 3 = '{s1 * 3}'  (repetition)")
print(f"  '{s1}'[0] = '{s1[0]}'  (indexing)")
print(f"  '{s1}'[1:4] = '{s1[1:4]}'  (slicing)")
print(f"  '{s1}'.upper() = '{s1.upper()}'  (method)")
print()

# ============================================================================
# EXAMPLE 5: Booleans - True/False
# ============================================================================
# Booleans represent true or false

print("Example 5: Boolean Type Properties")
print("-" * 50)

print("Boolean values:")
print(f"  True (type: {type(True).__name__})")
print(f"  False (type: {type(False).__name__})")

print()
print("Results of comparisons (produce booleans):")
print(f"  5 > 3 = {5 > 3}")
print(f"  5 < 3 = {5 < 3}")
print(f"  5 == 5 = {5 == 5}")
print(f"  'a' < 'b' = {'a' < 'b'}")
print()

print("Logical operations:")
print(f"  True and False = {True and False}")
print(f"  True or False = {True or False}")
print(f"  not True = {not True}")
print()

# ============================================================================
# EXAMPLE 6: None - Absence of Value
# ============================================================================
# None represents no value or absence

print("Example 6: None Type")
print("-" * 50)

nothing = None
print(f"Value: {nothing}")
print(f"Type: {type(nothing).__name__}")
print()

print("Common uses of None:")
print("  - Initial placeholder (not set yet)")
print("  - Return value of functions with no return")
print("  - Indicating missing data")
print()

def function_with_no_return():
    print("  Doing something...")

result = function_with_no_return()
print(f"Result: {result}")
print(f"Type: {type(result).__name__}")
print()

# ============================================================================
# EXAMPLE 7: Type Conversion - Strings to Numbers
# ============================================================================
# Converting between types

print("Example 7: Converting String to Number")
print("-" * 50)

text_number = "42"
print(f"Text: '{text_number}' (type: {type(text_number).__name__})")

number = int(text_number)
print(f"After int(): {number} (type: {type(number).__name__})")

# Now we can do math
print(f"Math: {number} + 8 = {number + 8}")
print()

# ============================================================================
# EXAMPLE 8: Type Conversion - Numbers to String
# ============================================================================
# Converting numbers to text

print("Example 8: Converting Number to String")
print("-" * 50)

number = 42
print(f"Number: {number} (type: {type(number).__name__})")

text = str(number)
print(f"After str(): '{text}' (type: {type(text).__name__})")

# Now we can concatenate
message = "The answer is " + text
print(f"Concatenation: '{message}'")
print()

# ============================================================================
# EXAMPLE 9: Type Promotion - Mixed Arithmetic
# ============================================================================
# When different numeric types are used together

print("Example 9: Type Promotion in Arithmetic")
print("-" * 50)

a = 5       # int
b = 3.0     # float

result = a + b
print(f"{a} (int) + {b} (float) = {result}")
print(f"Result type: {type(result).__name__}")
print()

print("Pattern: When int and float are mixed, result is float")
print()

# ============================================================================
# EXAMPLE 10: Type Mismatch - Why It Matters
# ============================================================================
# Operations that fail due to type mismatches

print("Example 10: Type Mismatches and Errors")
print("-" * 50)

print("Valid operations:")
print(f"  5 + 3 = {5 + 3}  (int + int)")
print(f"  '5' + '3' = {'5' + '3'}  (str + str)")
print()

print("Invalid operation:")
print("  '5' + 3 would give error (str + int)")
print("  Solution: convert one type")
print(f"    int('5') + 3 = {int('5') + 3}  (convert string to int)")
print(f"    '5' + str(3) = {'5' + str(3)}  (convert int to string)")
print()

# ============================================================================
# EXAMPLE 11: Boolean to Integer Conversion
# ============================================================================
# Booleans have numeric values

print("Example 11: Boolean as Numbers")
print("-" * 50)

print(f"True as int: {int(True)}")
print(f"False as int: {int(False)}")
print()

print("You can do math with booleans:")
print(f"  True + True = {True + True}")
print(f"  True + False = {True + False}")
print(f"  True * 5 = {True * 5}")
print()

# ============================================================================
# EXAMPLE 12: Type Check in Conditions
# ============================================================================
# Using type information for logic

print("Example 12: Checking Type in Conditions")
print("-" * 50)

value = "hello"
if type(value) == str:
    print(f"'{value}' is a string")

value = 42
if type(value) == int:
    print(f"{value} is an integer")
print()

# ============================================================================
# EXAMPLE 13: Default Types from Operations
# ============================================================================
# Some operations always produce specific types

print("Example 13: Result Types from Operations")
print("-" * 50)

print("Division always produces float:")
print(f"  10 / 2 = {10 / 2} (type: {type(10 / 2).__name__})")
print(f"  10 / 3 = {10 / 3} (type: {type(10 / 3).__name__})")
print()

print("Integer division produces int (or float if operands are float):")
print(f"  10 // 3 = {10 // 3} (type: {type(10 // 3).__name__})")
print(f"  10.0 // 3 = {10.0 // 3} (type: {type(10.0 // 3).__name__})")
print()

print("Comparisons produce booleans:")
print(f"  5 > 3 = {5 > 3} (type: {type(5 > 3).__name__})")
print()

# ============================================================================
# EXAMPLE 14: Integer vs Float Precision
# ============================================================================
# Why choice of type matters

print("Example 14: Integer vs Float Precision")
print("-" * 50)

print("Integers are exact:")
num_int = 42
print(f"  {num_int} is exactly {num_int}")
print()

print("Floats can have precision issues:")
num_float = 0.1 + 0.2
print(f"  0.1 + 0.2 = {num_float}")
print(f"  (Expected: 0.3, but got: {num_float})")
print(f"  This is a computer science issue, not Python's fault")
print()

# ============================================================================
# EXAMPLE 15: String Representation vs Value
# ============================================================================
# Strings can contain anything

print("Example 15: String Representation")
print("-" * 50)

values_as_strings = ["42", "3.14", "True", "None"]
values_as_types = [42, 3.14, True, None]

print("As strings (text):")
for s in values_as_strings:
    print(f"  '{s}' (type: str)")

print()
print("As actual types:")
for v in values_as_types:
    print(f"  {repr(v)} (type: {type(v).__name__})")

print()

# ============================================================================
# EXAMPLE 16: Truthiness - Boolean Conversion
# ============================================================================
# All values can be converted to boolean (True/False)

print("Example 16: Truthiness of Different Types")
print("-" * 50)

test_values = [
    (0, "zero"),
    (1, "one"),
    (42, "any number"),
    (0.0, "zero float"),
    ("", "empty string"),
    ("text", "non-empty string"),
    ([], "empty list"),
    ([1], "non-empty list"),
    (None, "None"),
]

print("Value → Converts to bool as:")
for value, description in test_values:
    bool_value = bool(value)
    print(f"  {repr(value):20} ({description:20}) → {bool_value}")

print()
print("Pattern: Empty/zero/None = False, everything else = True")
print()

# ============================================================================
# EXAMPLE 17: Type Conversion Chain
# ============================================================================
# Converting through multiple types

print("Example 17: Multi-Step Type Conversion")
print("-" * 50)

# Start with string
text = "42"
print(f"1. Start: '{text}' (type: str)")

# Convert to int
num_int = int(text)
print(f"2. int():  {num_int} (type: int)")

# Convert to float
num_float = float(num_int)
print(f"3. float(): {num_float} (type: float)")

# Convert to string
text_again = str(num_float)
print(f"4. str(): '{text_again}' (type: str)")

# Convert to boolean
bool_value = bool(text_again)
print(f"5. bool(): {bool_value} (type: bool)")

print()

# ============================================================================
# EXAMPLE 18: Type in Real-World Scenario - Student Record
# ============================================================================
# Practical use of multiple types

print("Example 18: Using Multiple Types Together")
print("-" * 50)

# Student data with different types
name = "Alice"           # str
age = 20                # int
gpa = 3.8               # float
is_active = True        # bool
graduation_date = None  # NoneType (will be set later)

print(f"Student Record:")
print(f"  Name: {name} (type: {type(name).__name__})")
print(f"  Age: {age} (type: {type(age).__name__})")
print(f"  GPA: {gpa} (type: {type(gpa).__name__})")
print(f"  Active: {is_active} (type: {type(is_active).__name__})")
print(f"  Graduation: {graduation_date} (type: {type(graduation_date).__name__})")

# Later, when set:
graduation_date = 2024
print()
print(f"After setting graduation date:")
print(f"  Graduation: {graduation_date} (type: {type(graduation_date).__name__})")
print()

# ============================================================================
# EXAMPLE 19: Arithmetic Results Depend on Types
# ============================================================================
# Same operation, different results based on type

print("Example 19: Operations and Their Result Types")
print("-" * 50)

print("Multiplication with different types:")
print(f"  3 * 4 = {3 * 4} (int * int = int)")
print(f"  3.0 * 4 = {3.0 * 4} (float * int = float)")
print(f"  '3' * 4 = {'3' * 4} (str * int = str, repeated)")
print()

print("Addition with different types:")
print(f"  3 + 4 = {3 + 4} (int + int = int)")
print(f"  3.0 + 4 = {3.0 + 4} (float + int = float)")
print(f"  '3' + '4' = {'3' + '4'} (str + str = str, concatenated)")
print()

# ============================================================================
# EXAMPLE 20: None vs False vs 0 vs Empty String
# ============================================================================
# These are all "falsy" but different

print("Example 20: Falsy Values Are Different")
print("-" * 50)

falsy_values = [None, False, 0, 0.0, ""]

print("All convert to False:")
for val in falsy_values:
    print(f"  bool({repr(val)}) = {bool(val)}")

print()
print("But they're different types and values:")
for val in falsy_values:
    print(f"  {repr(val):10} → type: {type(val).__name__}")

print()
print("Comparison:")
print(f"  None == False: {None == False}")
print(f"  None == 0: {None == 0}")
print(f"  False == 0: {False == 0}")
print(f"  0 == '': {0 == ''}")
print()

# ============================================================================
# EXAMPLE 21: Type Affects Comparison Results
# ============================================================================
# Comparing different types

print("Example 21: Type Matters in Comparisons")
print("-" * 50)

print("Comparing same value, different types:")
print(f"  5 == 5: {5 == 5}")      # True (same value, same type)
print(f"  5 == 5.0: {5 == 5.0}")  # True (Python considers equal)
print(f"  5 == '5': {5 == '5'}")   # False (int ≠ str)
print()

print("Comparing different types:")
print(f"  5 > '3': raises TypeError")
print("  (Can't compare int and str)")
print()

# ============================================================================
# EXAMPLE 22: Special Integer Values
# ============================================================================
# Some special integer cases

print("Example 22: Special Integer Values")
print("-" * 50)

print("Very large integers:")
big = 10**100
print(f"  10^100 = {big}")
print(f"  Type: {type(big).__name__}")
print()

print("Negative integers:")
negative = -42
print(f"  -42 = {negative}")
print()

print("Zero:")
zero = 0
print(f"  0 = {zero}")
print()

# ============================================================================
# EXAMPLE 23: Using isinstance() for Type Checking
# ============================================================================
# Better way to check types

print("Example 23: Type Checking with isinstance()")
print("-" * 50)

value = 42
print(f"value = {value}")
print()

if isinstance(value, int):
    print(f"✓ value is an int")

if isinstance(value, float):
    print("✗ value is not a float")
else:
    print(f"✓ value is not a float")

print()

# ============================================================================
# EXAMPLE 24: Type Conversion Failures
# ============================================================================
# When conversion is impossible

print("Example 24: Conversions That Fail")
print("-" * 50)

impossible_conversions = [
    ("int('abc')", lambda: int("abc")),
    ("int('3.14')", lambda: int("3.14")),
    ("float('hello')", lambda: float("hello")),
]

for description, func in impossible_conversions:
    try:
        result = func()
        print(f"  {description} = {result}")
    except ValueError as e:
        print(f"  {description} → ValueError")

print()
print("These fail because the strings don't represent valid numbers")
print()

# ============================================================================
# EXAMPLE 25: Practical Type Decision
# ============================================================================
# Choosing the right type for different data

print("Example 25: Choosing the Right Type")
print("-" * 50)

print("Data and recommended types:")
print()

print("Age: 25")
print("  → Use int (whole number, exact)")
print()

print("Price: 19.99")
print("  → Use float (decimal places)")
print()

print("Name: Alice")
print("  → Use str (text)")
print()

print("Is active: true")
print("  → Use bool (yes/no)")
print()

print("Graduation date: not set yet")
print("  → Use None initially, then int when set")
print()

print("Email: john@example.com")
print("  → Use str (text)")
print()

print("Product ID: 12345")
print("  → Use int (numeric identifier)")
print()

