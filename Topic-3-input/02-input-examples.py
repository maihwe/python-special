# Topic 3: Input - Elaborate Examples
# Each example demonstrates a real-world input scenario

# ============================================================================
# EXAMPLE 1: Basic Input - Getting User's Name
# ============================================================================
# The simplest input: ask for text, store it, use it.
# This shows the pause-and-wait behavior clearly.

print("Example 1: Basic Text Input")
print("-" * 50)
print("When you run this, the program will PAUSE here")
print("and wait for you to type something.")
print()

name = input("Enter your name: ")  # ← PROGRAM PAUSES HERE
# After you type and press Enter, execution continues

print(f"You entered: {name}")
print(f"Your name has {len(name)} characters")
print()

# ============================================================================
# EXAMPLE 2: Multiple Text Inputs
# ============================================================================
# Getting several pieces of text information from the user.
# Notice how the program asks multiple questions in sequence.

print("Example 2: Collecting Personal Information")
print("-" * 50)

first_name = input("First name: ")
last_name = input("Last name: ")
city = input("City: ")
country = input("Country: ")

full_name = first_name + " " + last_name
print()
print(f"Name: {full_name}")
print(f"From: {city}, {country}")
print()

# ============================================================================
# EXAMPLE 3: Converting Text to Integer
# ============================================================================
# The key concept: input() returns text, not numbers.
# We must convert explicitly using int().

print("Example 3: Converting String Input to Integer")
print("-" * 50)

print("Enter your age (user will type a number):")
age_text = input("Your age: ")
print(f"Type of input: {type(age_text)}")  # Will show <class 'str'>
print(f"Value received: '{age_text}'")
print()

# Now convert to integer
age = int(age_text)
print(f"Type after conversion: {type(age)}")  # Will show <class 'int'>
print(f"Value after conversion: {age}")
print()

# Now math works
next_year_age = age + 1
print(f"Next year you'll be: {next_year_age}")
print()

# ============================================================================
# EXAMPLE 4: One-Line Input with Conversion
# ============================================================================
# More common pattern: combine input() and conversion in one line.

print("Example 4: Input and Conversion in One Line")
print("-" * 50)

quantity = int(input("How many items? "))
print(f"You want {quantity} items")
print(f"At $9.99 each: ${quantity * 9.99:.2f}")
print()

# ============================================================================
# EXAMPLE 5: Working with Floating-Point Numbers
# ============================================================================
# Sometimes we need decimal numbers, not just integers.

print("Example 5: Decimal Number Input (float)")
print("-" * 50)

height_text = input("Your height in meters: ")
height = float(height_text)  # Convert to float (decimal)

print(f"Height: {height}m")
print(f"Height in cm: {height * 100}cm")
print()

# ============================================================================
# EXAMPLE 6: Multiple Conversions in One Program
# ============================================================================
# Real programs often get various types of input.

print("Example 6: Multiple Different Data Types")
print("-" * 50)

name = input("Product name: ")
price = float(input("Price ($): "))
quantity = int(input("Quantity in stock: "))
is_available = input("In stock? (yes/no): ") == "yes"

print()
print(f"Product: {name}")
print(f"Price: ${price:.2f}")
print(f"Stock: {quantity} units")
print(f"Available: {is_available}")
print(f"Total value: ${price * quantity:.2f}")
print()

# ============================================================================
# EXAMPLE 7: Simple Calculator
# ============================================================================
# A practical program: get two numbers and an operation, then calculate.

print("Example 7: Simple Calculator")
print("-" * 50)

num1 = float(input("First number: "))
num2 = float(input("Second number: "))
operation = input("Operation (+, -, *, /): ")

print()
print(f"Calculating: {num1} {operation} {num2}")
print()

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Error: Unknown operation"

print(f"Result: {result}")
print()

# ============================================================================
# EXAMPLE 8: Age-Based Decision
# ============================================================================
# Using input to drive program logic.

print("Example 8: Input-Driven Logic")
print("-" * 50)

age = int(input("What is your age? "))
print()

if age >= 18:
    print("You are an adult.")
    print("You can vote, work, and sign contracts.")
elif age >= 13:
    print("You are a teenager.")
    print("You can get a learner's permit.")
else:
    print("You are a child.")
    print("You must be supervised by adults.")

print()

# ============================================================================
# EXAMPLE 9: Student Grade Entry and Average Calculation
# ============================================================================
# Getting multiple related inputs and processing them.

print("Example 9: Grade Calculator")
print("-" * 50)

student_name = input("Student name: ")
score1 = int(input("Test 1 score: "))
score2 = int(input("Test 2 score: "))
score3 = int(input("Test 3 score: "))

print()

# Calculate average
average = (score1 + score2 + score3) / 3

print(f"Student: {student_name}")
print(f"Scores: {score1}, {score2}, {score3}")
print(f"Average: {average:.2f}")

# Determine grade
if average >= 90:
    grade_letter = "A"
elif average >= 80:
    grade_letter = "B"
elif average >= 70:
    grade_letter = "C"
elif average >= 60:
    grade_letter = "D"
else:
    grade_letter = "F"

print(f"Grade: {grade_letter}")
print()

# ============================================================================
# EXAMPLE 10: Price Calculator with Tax and Discount
# ============================================================================
# Real-world calculation: input prices, apply tax and discount.

print("Example 10: Price Calculation with Tax and Discount")
print("-" * 50)

price = float(input("Item price ($): "))
discount_percent = float(input("Discount (%): "))
tax_percent = float(input("Tax rate (%): "))

print()

# Calculate step by step
discount_amount = price * (discount_percent / 100)
price_after_discount = price - discount_amount

tax_amount = price_after_discount * (tax_percent / 100)
final_price = price_after_discount + tax_amount

print(f"Original price: ${price:.2f}")
print(f"Discount ({discount_percent}%): -${discount_amount:.2f}")
print(f"Price after discount: ${price_after_discount:.2f}")
print(f"Tax ({tax_percent}%): +${tax_amount:.2f}")
print(f"Final price: ${final_price:.2f}")
print()

# ============================================================================
# EXAMPLE 11: Password Verification
# ============================================================================
# Using input for security: comparing entered password to expected.

print("Example 11: Simple Password Check")
print("-" * 50)

correct_password = "secret123"
entered_password = input("Enter password: ")

print()

if entered_password == correct_password:
    print("✓ Password correct! Access granted.")
else:
    print("✗ Password incorrect! Access denied.")

print()

# ============================================================================
# EXAMPLE 12: String Input Processing
# ============================================================================
# Text input doesn't need conversion, but can be processed.

print("Example 12: Processing Text Input")
print("-" * 50)

text = input("Enter some text: ")

print()
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)} characters")
print(f"Reversed: {text[::-1]}")
print()

# ============================================================================
# EXAMPLE 13: yes/no Decision
# ============================================================================
# Converting simple text input to boolean logic.

print("Example 13: Yes/No Decision")
print("-" * 50)

response = input("Do you like programming? (yes/no): ")

# Convert yes/no to boolean
likes_programming = response.lower() == "yes"

print()
if likes_programming:
    print("Great! Keep learning and building.")
else:
    print("That's okay, programming isn't for everyone.")

print()

# ============================================================================
# EXAMPLE 14: Temperature Converter
# ============================================================================
# Getting number input and doing calculations.

print("Example 14: Temperature Conversion")
print("-" * 50)

celsius = float(input("Temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print()
print(f"  Celsius: {celsius}°C")
print(f"  Fahrenheit: {fahrenheit:.2f}°F")
print(f"  Kelvin: {kelvin:.2f}K")
print()

# ============================================================================
# EXAMPLE 15: Bill Splitter
# ============================================================================
# Practical calculation: split a bill among people.

print("Example 15: Bill Splitter")
print("-" * 50)

total_bill = float(input("Total bill amount ($): "))
tip_percent = float(input("Tip percentage (%): "))
num_people = int(input("Number of people: "))

print()

# Calculate total with tip
tip_amount = total_bill * (tip_percent / 100)
total_with_tip = total_bill + tip_amount

# Calculate per person
per_person = total_with_tip / num_people

print(f"Bill: ${total_bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total: ${total_with_tip:.2f}")
print(f"Per person: ${per_person:.2f}")
print()

# ============================================================================
# EXAMPLE 16: Age Difference Calculator
# ============================================================================
# Getting multiple related inputs and comparing them.

print("Example 16: Age Difference")
print("-" * 50)

person1_name = input("First person's name: ")
person1_age = int(input(f"{person1_name}'s age: "))

person2_name = input("Second person's name: ")
person2_age = int(input(f"{person2_name}'s age: "))

print()

age_difference = abs(person1_age - person2_age)
older_person = person1_name if person1_age > person2_age else person2_name

print(f"{person1_name}: {person1_age} years old")
print(f"{person2_name}: {person2_age} years old")
print(f"Age difference: {age_difference} years")
print(f"{older_person} is older")
print()

# ============================================================================
# EXAMPLE 17: Distance Calculator
# ============================================================================
# Using Pythagorean theorem with input coordinates.

print("Example 17: Distance Calculator")
print("-" * 50)

x1 = float(input("First point X coordinate: "))
y1 = float(input("First point Y coordinate: "))
x2 = float(input("Second point X coordinate: "))
y2 = float(input("Second point Y coordinate: "))

print()

# Calculate distance using Pythagorean theorem
dx = x2 - x1
dy = y2 - y1
distance = (dx**2 + dy**2) ** 0.5

print(f"Point 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")
print(f"Distance: {distance:.2f} units")
print()

# ============================================================================
# EXAMPLE 18: Time Converter
# ============================================================================
# Converting input seconds to hours, minutes, seconds.

print("Example 18: Time Converter")
print("-" * 50)

total_seconds = int(input("Total seconds: "))

print()

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"Total: {total_seconds} seconds")
print(f"= {hours} hours, {minutes} minutes, {seconds} seconds")
print()

# ============================================================================
# EXAMPLE 19: BMI Calculator
# ============================================================================
# Real-world calculation: Body Mass Index.

print("Example 19: BMI Calculator")
print("-" * 50)

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

print()

bmi = weight / (height ** 2)

print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.1f}")
print()

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")
print()

# ============================================================================
# EXAMPLE 20: Loan Interest Calculator
# ============================================================================
# Financial calculation with input values.

print("Example 20: Loan Interest Calculator")
print("-" * 50)

principal = float(input("Loan amount ($): "))
annual_rate = float(input("Annual interest rate (%): "))
years = int(input("Loan period (years): "))

print()

# Simple interest formula
total_interest = (principal * annual_rate * years) / 100
total_amount = principal + total_interest
monthly_payment = total_amount / (years * 12)

print(f"Principal: ${principal:.2f}")
print(f"Interest rate: {annual_rate}% per year")
print(f"Period: {years} years")
print(f"Total interest: ${total_interest:.2f}")
print(f"Total to repay: ${total_amount:.2f}")
print(f"Monthly payment: ${monthly_payment:.2f}")
print()

# ============================================================================
# EXAMPLE 21: String Comparison with Input
# ============================================================================
# Using input for conditional logic based on text.

print("Example 21: String Comparison")
print("-" * 50)

favorite_color = input("What's your favorite color? ").lower()

print()

if favorite_color == "blue":
    print("Blue is a cool color!")
elif favorite_color == "red":
    print("Red is a warm and energetic color!")
elif favorite_color == "green":
    print("Green is the color of nature!")
else:
    print(f"{favorite_color.capitalize()} is a great color!")

print()

# ============================================================================
# EXAMPLE 22: Multiple Conversions with Validation
# ============================================================================
# Practical example with different input types and formats.

print("Example 22: Product Purchase Simulation")
print("-" * 50)

product_name = input("Product name: ")
unit_price = float(input("Unit price ($): "))
quantity = int(input("Quantity to buy: "))
member = input("Are you a member? (yes/no): ") == "yes"

print()

# Calculate base cost
base_cost = unit_price * quantity

# Apply member discount if applicable
if member:
    discount = base_cost * 0.1  # 10% discount
    final_cost = base_cost - discount
    print(f"Product: {product_name}")
    print(f"Unit price: ${unit_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: ${base_cost:.2f}")
    print(f"Member discount (10%): -${discount:.2f}")
    print(f"Final cost: ${final_cost:.2f}")
else:
    print(f"Product: {product_name}")
    print(f"Unit price: ${unit_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total cost: ${base_cost:.2f}")
    print("(Join our membership for 10% off!)")

print()

# ============================================================================
# EXAMPLE 23: Text and Number Mixed Input
# ============================================================================
# Getting both text and numeric input together.

print("Example 23: Employee Information Entry")
print("-" * 50)

emp_name = input("Employee name: ")
emp_id = int(input("Employee ID: "))
emp_salary = float(input("Annual salary ($): "))
emp_department = input("Department: ")

print()

monthly_salary = emp_salary / 12

print(f"Name: {emp_name}")
print(f"ID: {emp_id}")
print(f"Department: {emp_department}")
print(f"Annual salary: ${emp_salary:,.2f}")
print(f"Monthly salary: ${monthly_salary:,.2f}")
print()

# ============================================================================
# EXAMPLE 24: Quiz with Scoring
# ============================================================================
# Educational: asking questions and scoring answers.

print("Example 24: Quiz Program")
print("-" * 50)
print("Answer the following questions (yes/no):\n")

score = 0

answer1 = input("Python is a programming language (yes/no): ").lower()
if answer1 == "yes":
    score += 1
    print("✓ Correct!")
else:
    print("✗ Incorrect!")
print()

answer2 = input("Python was created in 2000 (yes/no): ").lower()
if answer2 == "no":
    score += 1
    print("✓ Correct!")
else:
    print("✗ Incorrect!")
print()

answer3 = input("Lists in Python are mutable (yes/no): ").lower()
if answer3 == "yes":
    score += 1
    print("✓ Correct!")
else:
    print("✗ Incorrect!")
print()

print(f"Your score: {score}/3")
percentage = (score / 3) * 100
print(f"Percentage: {percentage:.0f}%")
print()

# ============================================================================
# EXAMPLE 25: Complex Real-World Scenario - Travel Budget
# ============================================================================
# Comprehensive example combining all concepts.

print("Example 25: Travel Budget Calculator")
print("-" * 50)

destination = input("Trip destination: ")
trip_length = int(input("Trip length (days): "))
daily_budget = float(input("Daily budget ($): "))
transport_cost = float(input("Transport cost ($): "))
accommodation_percent = float(input("Accommodation cost (% of daily budget): "))

print()

# Calculations
total_daily_food = daily_budget * trip_length
accommodation_per_day = daily_budget * (accommodation_percent / 100)
accommodation_total = accommodation_per_day * trip_length
remaining_daily_budget = daily_budget - accommodation_per_day
food_total = remaining_daily_budget * trip_length

total_budget = transport_cost + accommodation_total + food_total

print(f"Trip to: {destination}")
print(f"Duration: {trip_length} days")
print()
print(f"Budget Breakdown:")
print(f"  Transport: ${transport_cost:,.2f}")
print(f"  Accommodation: ${accommodation_total:,.2f} ({accommodation_percent}% of daily)")
print(f"  Food/Activities: ${food_total:,.2f}")
print()
print(f"Total Trip Budget: ${total_budget:,.2f}")
print(f"Average daily spend: ${total_budget / trip_length:,.2f}")
print()

if total_budget > 5000:
    print("This is a luxury trip!")
elif total_budget > 2000:
    print("This is a moderate trip.")
else:
    print("This is a budget-friendly trip.")

print()

