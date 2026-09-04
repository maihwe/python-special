# Topic 5: Type Conversion - Elaborate Examples
# Each example demonstrates real-world conversions between types

# ============================================================================
# EXAMPLE 1: String to Integer - Basic Conversion
# ============================================================================
# User input is always text, convert to numbers for calculation

print("Example 1: String to Integer Conversion")
print("-" * 50)

age_text = "25"
print(f"Age as text: '{age_text}' (type: {type(age_text).__name__})")

age = int(age_text)
print(f"Age as integer: {age} (type: {type(age).__name__})")

# Now we can do math
next_year = age + 1
print(f"Next year: {next_year}")
print()

# ============================================================================
# EXAMPLE 2: String to Float - Decimal Numbers
# ============================================================================
# When working with decimal values like prices or measurements

print("Example 2: String to Float Conversion")
print("-" * 50)

price_text = "19.99"
print(f"Price as text: '{price_text}' (type: {type(price_text).__name__})")

price = float(price_text)
print(f"Price as float: {price} (type: {type(price).__name__})")

# Now we can do calculations
tax = price * 0.08
total = price + tax
print(f"Price: ${price:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print()

# ============================================================================
# EXAMPLE 3: Number to String - Display Values
# ============================================================================
# Convert numbers to text for displaying or concatenating

print("Example 3: Number to String Conversion")
print("-" * 50)

count = 42
print(f"Count as integer: {count} (type: {type(count).__name__})")

count_text = str(count)
print(f"Count as text: '{count_text}' (type: {type(count_text).__name__})")

# Now we can concatenate with other text
message = "You have " + count_text + " items"
print(f"Message: {message}")
print()

# ============================================================================
# EXAMPLE 4: Type Check - Verifying Conversions
# ============================================================================
# Use type() to verify what type a value is after conversion

print("Example 4: Type Checking Before and After Conversion")
print("-" * 50)

value = "123"
print(f"Initial value: {value}")
print(f"Initial type: {type(value)}")
print()

converted = int(value)
print(f"After int(): {converted}")
print(f"After conversion type: {type(converted)}")
print()

# ============================================================================
# EXAMPLE 5: Converting User Input for Calculation
# ============================================================================
# Realistic scenario: get user numbers, convert, calculate

print("Example 5: User Input Conversion and Calculation")
print("-" * 50)

# Simulating user input
length_text = input("Length (meters): ")
width_text = input("Width (meters): ")

# Convert to numbers
length = float(length_text)
width = float(width_text)

# Calculate
area = length * width

# Display result
print(f"Area: {area} square meters")
print()

# ============================================================================
# EXAMPLE 6: Handling Conversion Errors
# ============================================================================
# What happens when conversion fails

print("Example 6: Conversion Error Handling")
print("-" * 50)

text = "abc"  # This can't be converted to a number
print(f"Attempting to convert: '{text}'")

try:
    number = int(text)
    print(f"Success: {number}")
except ValueError:
    print(f"✗ Error: '{text}' is not a valid integer")
    number = 0
    print(f"Using default value: {number}")

print()

# ============================================================================
# EXAMPLE 7: Converting to Boolean
# ============================================================================
# Convert values to True/False

print("Example 7: Converting to Boolean")
print("-" * 50)

values = [0, 1, "", "text", [], [1, 2], None, 42]
print("Value → bool(value)")
for val in values:
    result = bool(val)
    print(f"  {repr(val):15} → {result}")

print()
print("Pattern: Empty = False, Non-empty = True")
print()

# ============================================================================
# EXAMPLE 8: String to Yes/No Logic
# ============================================================================
# Convert text response to boolean

print("Example 8: User Response to Boolean")
print("-" * 50)

response = input("Do you want to continue? (yes/no): ").lower()
should_continue = (response == "yes")

print(f"Response: '{response}'")
print(f"Continue? {should_continue}")

if should_continue:
    print("Proceeding...")
else:
    print("Exiting...")

print()

# ============================================================================
# EXAMPLE 9: Chained Conversions
# ============================================================================
# Convert through multiple types in sequence

print("Example 9: Chained Type Conversions")
print("-" * 50)

# Start with string from user input
score_text = "92.5"
print(f"Step 1 - Input (string): '{score_text}'")

# Convert to float
score = float(score_text)
print(f"Step 2 - After float(): {score}")

# Do calculation (still float)
bonus = score * 1.1
print(f"Step 3 - After calculation: {bonus}")

# Round and convert to int
final = int(bonus)
print(f"Step 4 - After int(): {final}")

# Convert back to string for display
display = f"Final score: {final}"
print(f"Step 5 - Display: {display}")
print()

# ============================================================================
# EXAMPLE 10: Float to String with Formatting
# ============================================================================
# Display float with specific decimal places

print("Example 10: Float Formatting")
print("-" * 50)

price = 19.999
print(f"Raw float: {price}")
print(f"As string (f-string, 2 decimals): ${price:.2f}")
print(f"As string (str()): {str(price)}")

# Simulate price calculation
quantity = 3
total = price * quantity
print(f"Total: {total}")
print(f"Formatted total: ${total:.2f}")
print()

# ============================================================================
# EXAMPLE 11: Integer to Float - Adding Decimals
# ============================================================================
# Convert int to float for division

print("Example 11: Integer to Float Conversion")
print("-" * 50)

total_items = 7
people = 2

# Integer division (no decimals)
per_person_int = total_items // people
print(f"Integer division: {total_items} // {people} = {per_person_int}")

# Float division (with decimals)
per_person_float = total_items / people
print(f"Float division: {total_items} / {people} = {per_person_float}")

# Convert int to float explicitly
per_person_float2 = float(total_items) / people
print(f"Explicit float: float({total_items}) / {people} = {per_person_float2}")
print()

# ============================================================================
# EXAMPLE 12: Validating Numeric Input
# ============================================================================
# Convert and validate in one process

print("Example 12: Input Validation with Conversion")
print("-" * 50)

# Keep asking until valid input
while True:
    try:
        age = int(input("Enter your age: "))
        if 0 <= age <= 150:
            break
        else:
            print("✗ Age must be between 0 and 150")
    except ValueError:
        print("✗ Please enter a valid number")

print(f"✓ Accepted age: {age}")
print()

# ============================================================================
# EXAMPLE 13: Multiple Conversions in Sequence
# ============================================================================
# Realistic program: get multiple inputs, convert, calculate, display

print("Example 13: Complete Conversion Workflow")
print("-" * 50)

# Get inputs
name = input("Name: ")
age_text = input("Age: ")
gpa_text = input("GPA: ")

# Convert types
age = int(age_text)
gpa = float(gpa_text)

# Verify types
print(f"name type: {type(name).__name__} = {name}")
print(f"age type: {type(age).__name__} = {age}")
print(f"gpa type: {type(gpa).__name__} = {gpa}")

# Calculate
next_year_age = age + 1
gpa_rounded = round(gpa, 1)

# Display with formatted strings
print(f"\nSummary:")
print(f"  Student: {name}")
print(f"  Age: {age} (next year: {next_year_age})")
print(f"  GPA: {gpa_rounded}")
print()

# ============================================================================
# EXAMPLE 14: Boolean Conversion with Conditions
# ============================================================================
# Convert to boolean for decision making

print("Example 14: Boolean Conversion in Conditions")
print("-" * 50)

username = input("Username (or press Enter to skip): ")
is_logged_in = bool(username)  # Empty string = False, non-empty = True

print(f"Username: '{username}'")
print(f"Logged in: {is_logged_in}")

if is_logged_in:
    print(f"Welcome, {username}!")
else:
    print("Anonymous user")

print()

# ============================================================================
# EXAMPLE 15: Price Calculation with Multiple Conversions
# ============================================================================
# E-commerce scenario

print("Example 15: E-commerce Price Calculation")
print("-" * 50)

# Get inputs (all text)
price_text = input("Item price ($): ")
quantity_text = input("Quantity: ")
tax_rate_text = input("Tax rate (%): ")

# Convert to appropriate types
price = float(price_text)
quantity = int(quantity_text)
tax_rate = float(tax_rate_text) / 100  # Convert percent to decimal

# Calculate
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# Display with formatting
print()
print("Order Summary:")
print(f"  Unit price: ${price:.2f}")
print(f"  Quantity: {quantity}")
print(f"  Subtotal: ${subtotal:.2f}")
print(f"  Tax ({tax_rate*100:.1f}%): ${tax:.2f}")
print(f"  Total: ${total:.2f}")
print()

# ============================================================================
# EXAMPLE 16: Quiz Score Conversion
# ============================================================================
# Convert score to percentage and grade

print("Example 16: Score to Percentage and Grade Conversion")
print("-" * 50)

points = int(input("Points earned: "))
total = int(input("Total points: "))

# Calculate percentage (convert to float for division)
percentage = (points / total) * 100

# Convert to letter grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
else:
    grade = "F"

print()
print(f"Score: {points}/{total}")
print(f"Percentage: {percentage:.1f}%")
print(f"Grade: {grade}")
print()

# ============================================================================
# EXAMPLE 17: Temperature Conversion
# ============================================================================
# Convert between Celsius and Fahrenheit

print("Example 17: Temperature Conversion")
print("-" * 50)

celsius_text = input("Temperature (Celsius): ")
celsius = float(celsius_text)

# Formula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit:.1f}°F")
print()

# ============================================================================
# EXAMPLE 18: String Splitting and Converting
# ============================================================================
# Parse structured text

print("Example 18: Parsing CSV and Converting Types")
print("-" * 50)

# Simulating reading CSV
csv_line = "Alice,25,3.8,Engineer"
print(f"CSV line: {csv_line}")

# Split into fields
fields = csv_line.split(",")
print(f"Fields: {fields}")

# Convert to appropriate types
name = fields[0]              # Keep as string
age = int(fields[1])          # Convert to int
gpa = float(fields[2])        # Convert to float
job = fields[3]               # Keep as string

# Display with types verified
print()
print(f"Name: {name} ({type(name).__name__})")
print(f"Age: {age} ({type(age).__name__})")
print(f"GPA: {gpa} ({type(gpa).__name__})")
print(f"Job: {job} ({type(job).__name__})")
print()

# ============================================================================
# EXAMPLE 19: Safe Conversion with Try/Except
# ============================================================================
# Robust error handling

print("Example 19: Robust Conversion with Error Handling")
print("-" * 50)

user_inputs = ["42", "3.14", "abc", "12x", ""]

for user_input in user_inputs:
    print(f"Input: '{user_input}'", end=" → ")
    
    try:
        number = float(user_input)
        print(f"✓ Converted to {number}")
    except ValueError:
        print(f"✗ Cannot convert to number")

print()

# ============================================================================
# EXAMPLE 20: Type Conversion in Comparisons
# ============================================================================
# Convert before comparing

print("Example 20: Type Conversion in Comparisons")
print("-" * 50)

# Without conversion (comparison fails or gives unexpected result)
text_age = "25"
print(f"Comparing: '{text_age}' == 25")
print(f"Result: {text_age == 25}")  # False (text ≠ number)
print()

# With conversion (comparison works)
print(f"Comparing: int('{text_age}') == 25")
print(f"Result: {int(text_age) == 25}")  # True
print()

# ============================================================================
# EXAMPLE 21: Stripping Whitespace Before Converting
# ============================================================================
# Clean input before conversion

print("Example 21: Cleaning Before Converting")
print("-" * 50)

# Input might have extra spaces
messy_input = "  42  "
print(f"Messy input: '{messy_input}'")

# Try to convert without cleaning
try:
    num = int(messy_input)  # Might fail depending on spaces
    print(f"Direct conversion worked: {num}")
except ValueError:
    print("Direct conversion failed")
    # Clean then convert
    clean = messy_input.strip()
    num = int(clean)
    print(f"After strip(): '{clean}' → {num}")

print()

# ============================================================================
# EXAMPLE 22: Type Conversion in F-Strings
# ============================================================================
# Implicit conversion in formatted strings

print("Example 22: Conversion in F-Strings")
print("-" * 50)

number = 42
float_num = 3.14159
bool_val = True

# F-strings auto-convert to string for display
print(f"Number: {number}")           # Auto-converts int
print(f"Float: {float_num}")         # Auto-converts float
print(f"Boolean: {bool_val}")        # Auto-converts bool

# With formatting
print(f"Formatted float: {float_num:.2f}")
print(f"In expression: {number * 2}")

print()

# ============================================================================
# EXAMPLE 23: Percentage Calculation with Conversions
# ============================================================================
# Real-world percentage calculations

print("Example 23: Percentage and Discounts")
print("-" * 50)

# Get input
original_price_text = input("Original price ($): ")
discount_text = input("Discount (%): ")

# Convert
original_price = float(original_price_text)
discount_percent = float(discount_text)

# Calculate
discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount

# Display
print()
print(f"Original: ${original_price:.2f}")
print(f"Discount ({discount_percent}%): -${discount_amount:.2f}")
print(f"Final: ${final_price:.2f}")
print()

# ============================================================================
# EXAMPLE 24: Rating Score Conversion
# ============================================================================
# Convert numeric rating to text description

print("Example 24: Numeric Score to Text Description")
print("-" * 50)

rating_text = input("Rate 1-5: ")
rating = int(rating_text)

# Convert to description
descriptions = {
    1: "Poor",
    2: "Fair",
    3: "Good",
    4: "Very Good",
    5: "Excellent"
}

description = descriptions.get(rating, "Invalid")
print(f"Rating: {rating}/5 - {description}")
print()

# ============================================================================
# EXAMPLE 25: Complex Conversion Chain - Loan Calculator
# ============================================================================
# Multiple conversions in realistic financial calculation

print("Example 25: Loan Calculator (Complex Conversion Chain)")
print("-" * 50)

# Get inputs (all text initially)
principal_text = input("Loan amount ($): ")
rate_text = input("Annual interest rate (%): ")
years_text = input("Loan period (years): ")

# Convert to appropriate numeric types
principal = float(principal_text)
annual_rate = float(rate_text)
years = int(years_text)

# Convert percent to decimal
rate_decimal = annual_rate / 100

# Calculate using formula
# Simple interest: Interest = Principal * Rate * Time
total_interest = principal * rate_decimal * years
total_amount = principal + total_interest
monthly_payment = total_amount / (years * 12)

# Display results (auto-converted to strings in f-string)
print()
print("Loan Summary:")
print(f"  Principal: ${principal:,.2f}")
print(f"  Rate: {annual_rate}%/year")
print(f"  Period: {years} years")
print(f"  Total Interest: ${total_interest:,.2f}")
print(f"  Total Amount: ${total_amount:,.2f}")
print(f"  Monthly Payment: ${monthly_payment:,.2f}")
print()

