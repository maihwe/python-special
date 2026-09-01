# Topic 2: Variables - Elaborate Examples
# Each example teaches a concept about how variables work

# ============================================================================
# EXAMPLE 1: Creating and Using Basic Variables
# ============================================================================
# When you create a variable, Python allocates memory and stores the value.
# The variable name becomes a label pointing to that memory location.

age = 25
print("Example 1 - Basic Variable Creation:")
print(f"  Variable name: age")
print(f"  Value stored: {age}")
print(f"  Data type: {type(age)}")
# Output: age is 25, and its type is <class 'int'> (integer)

print()

# ============================================================================
# EXAMPLE 2: Using the Same Variable Multiple Times
# ============================================================================
# Once a variable is created, you can use it in multiple places.
# Python retrieves the value each time you reference the name.

price = 19.99
quantity = 3
print("Example 2 - Using Variables in Calculations:")
print(f"  Price per item: ${price}")
print(f"  Quantity: {quantity}")
print(f"  Subtotal: ${price * quantity}")
print(f"  Total with 10% tax: ${price * quantity * 1.1}")
# The variable 'price' is used 3 times, Python looks it up each time

print()

# ============================================================================
# EXAMPLE 3: Reassigning Variables (Updating Values)
# ============================================================================
# Variables are called "variables" because they can change.
# When you reassign, the old value is discarded and replaced.

score = 85
print("Example 3 - Reassigning Variables:")
print(f"  Initial score: {score}")

score = 92  # Old value (85) is gone, now score is 92
print(f"  After first update: {score}")

score = score + 5  # Read current value (92), add 5, store back (97)
print(f"  After second update: {score}")
print(f"  Important: We cannot retrieve 85 anymore - it's lost")

print()

# ============================================================================
# EXAMPLE 4: Multiple Variables Storing Different Data
# ============================================================================
# A single program often needs many variables, each storing different data.
# This is like having many labeled drawers in your filing cabinet.

first_name = "Alice"
last_name = "Johnson"
age = 28
city = "New York"
is_employed = True

print("Example 4 - Multiple Variables in a Real Scenario:")
print(f"  Name: {first_name} {last_name}")
print(f"  Age: {age} years old")
print(f"  Location: {city}")
print(f"  Employed: {is_employed}")
print(f"  Internal representation:")
print(f"    - first_name (type: {type(first_name).__name__}): '{first_name}'")
print(f"    - last_name (type: {type(last_name).__name__}): '{last_name}'")
print(f"    - age (type: {type(age).__name__}): {age}")
print(f"    - city (type: {type(city).__name__}): '{city}'")
print(f"    - is_employed (type: {type(is_employed).__name__}): {is_employed}")

print()

# ============================================================================
# EXAMPLE 5: Variables Store References to Values (Not the Value Itself)
# ============================================================================
# This is an important concept: variables store memory addresses (references),
# not the values themselves. Python hides this complexity, but it matters.

balance = 1000.00
print("Example 5 - How Variables Reference Values:")
print(f"  We create: balance = 1000.00")
print(f"  Internally, Python:")
print(f"    1. Allocates memory at some address (e.g., 0x7f84c4)")
print(f"    2. Stores 1000.00 at that address")
print(f"    3. Creates binding: 'balance' → that address")
print(f"  When we use 'balance', Python:")
print(f"    1. Looks up 'balance'")
print(f"    2. Finds it points to 0x7f84c4")
print(f"    3. Retrieves value from that address: 1000.00")
print(f"  Current value: {balance}")

print()

# ============================================================================
# EXAMPLE 6: Variables Can Change Types
# ============================================================================
# Python allows a variable to change its data type by reassignment.
# This is flexible but can be error-prone.

value = 42  # Initially an integer
print("Example 6 - Variables Can Change Types:")
print(f"  value = 42")
print(f"    Type: {type(value)}")
print(f"    Value: {value}")

value = "42"  # Now it's a string
print(f"  value = '42'")
print(f"    Type: {type(value)}")
print(f"    Value: {value}")

value = [4, 2]  # Now it's a list
print(f"  value = [4, 2]")
print(f"    Type: {type(value)}")
print(f"    Value: {value}")

value = True  # Now it's a boolean
print(f"  value = True")
print(f"    Type: {type(value)}")
print(f"    Value: {value}")

print()

# ============================================================================
# EXAMPLE 7: Arithmetic with Variables
# ============================================================================
# Variables can be used in mathematical operations.
# Python evaluates the operations and stores results.

hours_worked = 40
hourly_rate = 25.00
overtime_hours = 5
overtime_rate = 37.50

print("Example 7 - Arithmetic with Variables (Payroll Calculation):")
regular_pay = hours_worked * hourly_rate
overtime_pay = overtime_hours * overtime_rate
total_pay = regular_pay + overtime_pay

print(f"  Regular hours: {hours_worked}")
print(f"  Regular rate: ${hourly_rate}/hour")
print(f"  Regular pay: {hours_worked} × ${hourly_rate} = ${regular_pay}")
print(f"")
print(f"  Overtime hours: {overtime_hours}")
print(f"  Overtime rate: ${overtime_rate}/hour")
print(f"  Overtime pay: {overtime_hours} × ${overtime_rate} = ${overtime_pay}")
print(f"")
print(f"  Total pay: ${regular_pay} + ${overtime_pay} = ${total_pay}")

print()

# ============================================================================
# EXAMPLE 8: Order of Operations Matters
# ============================================================================
# Python evaluates the right side of assignment completely
# before storing the result in the variable on the left side.

result = 2 + 3 * 4  # Not (2 + 3) * 4, but 2 + (3 * 4)
print("Example 8 - Order of Operations:")
print(f"  result = 2 + 3 * 4")
print(f"  Evaluates as: 2 + (3 * 4) = 2 + 12 = 14")
print(f"  Result: {result}")
print()

result_with_parens = (2 + 3) * 4
print(f"  result_with_parens = (2 + 3) * 4")
print(f"  Evaluates as: (2 + 3) * 4 = 5 * 4 = 20")
print(f"  Result: {result_with_parens}")
print(f"  Same expression, different parentheses, different results!")

print()

# ============================================================================
# EXAMPLE 9: Variable Names Matter for Readability
# ============================================================================
# The computer doesn't care about names, but humans do.
# Good names make code understandable.

# Version 1: Good names
student_gpa = 3.85
student_name = "Alice"
graduation_year = 2024
print("Example 9 - Variable Naming Matters:")
print("Version 1 (GOOD NAMES):")
print(f"  student_gpa = {student_gpa}")
print(f"  student_name = '{student_name}'")
print(f"  graduation_year = {graduation_year}")
print(f"  → Clear meaning. Easy to understand.")
print()

# Version 2: Bad names
a = 3.85
b = "Alice"
c = 2024
print("Version 2 (BAD NAMES):")
print(f"  a = {a}")
print(f"  b = '{b}'")
print(f"  c = {c}")
print(f"  → Unclear. What do a, b, c represent?")

print()

# ============================================================================
# EXAMPLE 10: Variables Enable Dynamic Programs
# ============================================================================
# Without variables, programs are static. Variables let programs respond
# to different inputs and situations.

print("Example 10 - Dynamic Program Using Variables:")
# Instead of hardcoding one calculation:
print("  Calculating cost for different quantities:")

unit_price = 9.99
for quantity in [1, 5, 10, 100]:
    total_cost = unit_price * quantity
    print(f"    {quantity} items × ${unit_price} = ${total_cost:.2f}")
    
# This works for any quantity! Without variables, we'd need separate code
# for each quantity. Variables make code flexible and reusable.

print()

# ============================================================================
# EXAMPLE 11: Updating Variables Based on Previous Values
# ============================================================================
# A common pattern: read current value, do something, store back.

balance = 1000.00
print("Example 11 - Bank Account Transactions:")
print(f"  Starting balance: ${balance}")

withdrawal = 250.00
balance = balance - withdrawal  # Read 1000, subtract 250, store back 750
print(f"  After $250 withdrawal: ${balance}")

deposit = 500.00
balance = balance + deposit  # Read 750, add 500, store back 1250
print(f"  After $500 deposit: ${balance}")

interest = balance * 0.02
balance = balance + interest  # Read 1250, add interest, store back
print(f"  After 2% interest: ${balance:.2f}")

print()

# ============================================================================
# EXAMPLE 12: String Variables and Concatenation
# ============================================================================
# Variables can store text. Text variables have different operations.

first_name = "John"
last_name = "Smith"
email = "john.smith@example.com"

print("Example 12 - String Variables:")
full_name = first_name + " " + last_name  # Concatenation (joining)
print(f"  full_name = '{full_name}'")
print(f"  Email: {email}")
print(f"  Greeting: Dear {full_name}, your account {email} is active.")

print()

# ============================================================================
# EXAMPLE 13: Boolean Variables (True/False)
# ============================================================================
# Booleans store true/false values, often used for program logic.

is_logged_in = True
is_admin = False
account_verified = True

print("Example 13 - Boolean Variables:")
print(f"  is_logged_in: {is_logged_in}")
print(f"  is_admin: {is_admin}")
print(f"  account_verified: {account_verified}")

if is_logged_in and account_verified:
    print("  → User can proceed (logged in AND verified)")
else:
    print("  → User cannot proceed")

if is_admin:
    print("  → User has admin privileges")
else:
    print("  → User has standard privileges")

print()

# ============================================================================
# EXAMPLE 14: Floating-Point Precision
# ============================================================================
# Float variables can have precision issues (important to know).

price1 = 0.1
price2 = 0.2
total = price1 + price2

print("Example 14 - Floating-Point Precision:")
print(f"  price1 = 0.1")
print(f"  price2 = 0.2")
print(f"  total = price1 + price2")
print(f"  Expected: 0.3")
print(f"  Actual: {total}")
print(f"  Note: {total} ≠ 0.3 exactly (floating-point representation)")
print(f"  This is a known issue in computer science, not a Python bug!")

print()

# ============================================================================
# EXAMPLE 15: Using Variables in Comparisons
# ============================================================================
# Variables can be compared to other values or variables.

age = 25
voting_age = 18
retirement_age = 65

print("Example 15 - Variables in Comparisons:")
print(f"  age = {age}")
print(f"  Can vote? {age >= voting_age}")  # True
print(f"  Can work? {age < retirement_age}")  # True
print(f"  Is retirement age? {age == retirement_age}")  # False

print()

# ============================================================================
# EXAMPLE 16: Multiple Assignment (Unpacking)
# ============================================================================
# You can assign multiple variables at once.

x, y, z = 10, 20, 30
print("Example 16 - Multiple Assignment:")
print(f"  x, y, z = 10, 20, 30")
print(f"  x = {x}, y = {y}, z = {z}")

# Useful for swapping values
a, b = 5, 10
print(f"  Before swap: a = {a}, b = {b}")
a, b = b, a  # Swap!
print(f"  After swap: a = {a}, b = {b}")

print()

# ============================================================================
# EXAMPLE 17: Compound Assignment Operators
# ============================================================================
# Shortcuts for updating variables.

count = 10
print("Example 17 - Compound Assignment Operators:")
print(f"  count = {count}")

count += 5  # Same as: count = count + 5
print(f"  count += 5 → {count}")

count -= 3  # Same as: count = count - 3
print(f"  count -= 3 → {count}")

count *= 2  # Same as: count = count * 2
print(f"  count *= 2 → {count}")

count //= 4  # Same as: count = count // 4
print(f"  count //= 4 → {count}")

print()

# ============================================================================
# EXAMPLE 18: Variables in Real-World Scenario (Inventory)
# ============================================================================
# Simulating a simple inventory system.

item_name = "Laptop"
initial_stock = 50
units_sold_monday = 8
units_sold_tuesday = 12
units_sold_wednesday = 5
unit_price = 999.99

print("Example 18 - Inventory Management System:")
print(f"  Product: {item_name}")
print(f"  Unit price: ${unit_price}")
print()

current_stock = initial_stock
print(f"  Monday - Starting stock: {current_stock}")
current_stock = current_stock - units_sold_monday
print(f"             Units sold: {units_sold_monday}")
print(f"             Ending stock: {current_stock}")
print()

print(f"  Tuesday - Starting stock: {current_stock}")
current_stock = current_stock - units_sold_tuesday
print(f"             Units sold: {units_sold_tuesday}")
print(f"             Ending stock: {current_stock}")
print()

print(f"  Wednesday - Starting stock: {current_stock}")
current_stock = current_stock - units_sold_wednesday
print(f"              Units sold: {units_sold_wednesday}")
print(f"              Ending stock: {current_stock}")
print()

total_units_sold = units_sold_monday + units_sold_tuesday + units_sold_wednesday
total_revenue = total_units_sold * unit_price
print(f"  Summary:")
print(f"    Total units sold: {total_units_sold}")
print(f"    Total revenue: ${total_revenue:,.2f}")
print(f"    Remaining stock: {current_stock}")

print()

# ============================================================================
# EXAMPLE 19: Type Conversion Between Variables
# ============================================================================
# Sometimes you need to convert a variable from one type to another.

score_text = "85"  # This is a string (text), not a number
print("Example 19 - Type Conversion:")
print(f"  score_text = '{score_text}'")
print(f"  Type: {type(score_text)}")
print(f"  Can we do math with it?")
try:
    result = score_text + 10
except TypeError as e:
    print(f"    ERROR: {e}")

print()
print(f"  Converting to integer...")
score_number = int(score_text)  # Convert string to integer
print(f"  score_number = int('{score_text}') → {score_number}")
print(f"  Type: {type(score_number)}")
print(f"  Can we do math now?")
result = score_number + 10
print(f"    {score_number} + 10 = {result} ✓")

print()

# ============================================================================
# EXAMPLE 20: Variables and Memory Addresses (Advanced Concept)
# ============================================================================
# Python hides memory addresses, but they exist. Python's `id()` shows them.

x = 100
y = 100
z = x

print("Example 20 - Understanding Variable Identity:")
print(f"  x = 100")
print(f"  y = 100")
print(f"  z = x")
print()
print(f"  Memory addresses (Python id):")
print(f"    id(x) = {id(x)}")
print(f"    id(y) = {id(y)}")
print(f"    id(z) = {id(z)}")
print()
print(f"  Analysis:")
if id(x) == id(z):
    print(f"    x and z point to SAME location (z = x copied the reference)")
if id(x) == id(y):
    print(f"    x and y happen to point to SAME location (Python optimization)")
else:
    print(f"    x and y are separate (different integers)")
print()
print(f"  Note: Python often optimizes small integers to share memory.")
print(f"  The key lesson: variables are references to memory locations.")

print()

# ============================================================================
# EXAMPLE 21: Real-World Grade Calculator
# ============================================================================
# A realistic program using multiple variables.

print("Example 21 - Student Grade Calculator:")
print()

student_name = "Emma"
midterm_score = 88
midterm_weight = 0.30
final_score = 92
final_weight = 0.40
project_score = 95
project_weight = 0.30

print(f"Student: {student_name}")
print()

midterm_contribution = midterm_score * midterm_weight
final_contribution = final_score * final_weight
project_contribution = project_score * project_weight

print(f"Breakdown:")
print(f"  Midterm ({midterm_weight*100:.0f}%): {midterm_score} × {midterm_weight} = {midterm_contribution:.1f}")
print(f"  Final ({final_weight*100:.0f}%): {final_score} × {final_weight} = {final_contribution:.1f}")
print(f"  Project ({project_weight*100:.0f}%): {project_score} × {project_weight} = {project_contribution:.1f}")
print()

course_grade = midterm_contribution + final_contribution + project_contribution
print(f"Final Grade: {course_grade:.2f}")

if course_grade >= 90:
    letter_grade = "A"
elif course_grade >= 80:
    letter_grade = "B"
elif course_grade >= 70:
    letter_grade = "C"
elif course_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Letter Grade: {letter_grade}")

