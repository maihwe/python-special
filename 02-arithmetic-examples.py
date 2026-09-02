# Topic 7: Arithmetic - Elaborate Examples
# Comprehensive examples of mathematical operations in Python

# ============================================================================
# EXAMPLE 1: Basic Arithmetic Operators
# ============================================================================
# The fundamental operations

print("Example 1: Basic Arithmetic Operators")
print("-" * 50)

a = 10
b = 3

print(f"a = {a}, b = {b}")
print()
print(f"Addition:       {a} + {b} = {a + b}")
print(f"Subtraction:    {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division:       {a} / {b} = {a / b}")
print(f"Integer div:    {a} // {b} = {a // b}")
print(f"Modulo:         {a} % {b} = {a % b}")
print(f"Exponent:       {a} ** {b} = {a ** b}")
print()

# ============================================================================
# EXAMPLE 2: Order of Operations (PEMDAS)
# ============================================================================
# Operations follow a specific order

print("Example 2: Order of Operations")
print("-" * 50)

expr1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {expr1}")
print(f"  (Multiplication first: 3*4=12, then 2+12=14)")
print()

expr2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {expr2}")
print(f"  (Parentheses first: 2+3=5, then 5*4=20)")
print()

expr3 = 10 - 5 + 2
print(f"10 - 5 + 2 = {expr3}")
print(f"  (Left to right: 10-5=5, then 5+2=7)")
print()

expr4 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {expr4}")
print(f"  (Right to left: 3**2=9, then 2**9=512)")
print()

# ============================================================================
# EXAMPLE 3: Division - True Division vs Integer Division
# ============================================================================
# Understanding the difference between / and //

print("Example 3: True Division vs Integer Division")
print("-" * 50)

numerator = 10
denominator = 3

print(f"True division: {numerator} / {denominator} = {numerator / denominator}")
print(f"  (Results in float with decimal)")
print()

print(f"Integer division: {numerator} // {denominator} = {numerator // denominator}")
print(f"  (Results in int, discards decimal)")
print()

print("Another example:")
print(f"10 / 2 = {10 / 2}  (5.0, a float)")
print(f"10 // 2 = {10 // 2}  (5, an integer)")
print()

# ============================================================================
# EXAMPLE 4: Modulo - Finding Remainders
# ============================================================================
# The % operator gives remainder

print("Example 4: Modulo Operator (Remainder)")
print("-" * 50)

print(f"10 % 3 = {10 % 3}  (10 divided by 3 leaves remainder 1)")
print(f"17 % 5 = {17 % 5}  (17 divided by 5 leaves remainder 2)")
print(f"20 % 4 = {20 % 4}  (20 divided by 4 leaves remainder 0)")
print()

print("Practical uses:")
print()

# Check if even
n = 7
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

# Get last digit
number = 12345
last_digit = number % 10
print(f"Last digit of {number}: {last_digit}")

# Cycle through indices
day_num = 8
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
day_name = days[day_num % 7]
print(f"Day {day_num} is: {day_name}")
print()

# ============================================================================
# EXAMPLE 5: Exponents - Powers and Roots
# ============================================================================
# Using ** for powers and roots

print("Example 5: Exponents")
print("-" * 50)

print("Powers:")
print(f"2 ** 3 = {2 ** 3}  (2 × 2 × 2)")
print(f"5 ** 2 = {5 ** 2}  (5 × 5, square)")
print(f"10 ** 3 = {10 ** 3}  (10 × 10 × 10, cube)")
print()

print("Roots (fractional exponents):")
print(f"4 ** 0.5 = {4 ** 0.5}  (square root of 4)")
print(f"8 ** (1/3) = {8 ** (1/3)}  (cube root of 8)")
print(f"27 ** (1/3) = {27 ** (1/3)}  (cube root of 27)")
print()

print("Large powers:")
print(f"2 ** 10 = {2 ** 10}")
print(f"2 ** 20 = {2 ** 20}")
print()

# ============================================================================
# EXAMPLE 6: Negative Numbers in Arithmetic
# ============================================================================
# Operations with negative values

print("Example 6: Negative Numbers")
print("-" * 50)

pos = 10
neg = -5

print(f"{pos} + {neg} = {pos + neg}")
print(f"{pos} - {neg} = {pos - neg}")
print(f"{pos} * {neg} = {pos * neg}")
print(f"{pos} / {neg} = {pos / neg}")
print()

print("Negation operator:")
x = 5
print(f"x = {x}")
print(f"-x = {-x}")
print(f"-(-x) = {-(-x)}")
print()

# ============================================================================
# EXAMPLE 7: Compound Assignment Operators
# ============================================================================
# Shorthand for updating variables

print("Example 7: Compound Assignment Operators")
print("-" * 50)

x = 10
print(f"Starting value: x = {x}")
print()

x += 5
print(f"After x += 5: {x}")

x -= 3
print(f"After x -= 3: {x}")

x *= 2
print(f"After x *= 2: {x}")

x /= 4
print(f"After x /= 4: {x}")

x //= 2
print(f"After x //= 2: {x}")

x **= 2
print(f"After x **= 2: {x}")
print()

# ============================================================================
# EXAMPLE 8: Building Complex Expressions
# ============================================================================
# Combining multiple operations

print("Example 8: Complex Expressions")
print("-" * 50)

# Quadratic formula: x = (-b ± √(b²-4ac)) / 2a
a = 1
b = -5
c = 6

discriminant = b**2 - 4*a*c
x1 = (-b + discriminant**0.5) / (2*a)
x2 = (-b - discriminant**0.5) / (2*a)

print(f"Quadratic equation: {a}x² + {b}x + {c} = 0")
print(f"Discriminant: {discriminant}")
print(f"x1 = {x1}")
print(f"x2 = {x2}")
print()

# ============================================================================
# EXAMPLE 9: Price Calculation with Multiple Operations
# ============================================================================
# E-commerce scenario

print("Example 9: Price Calculation")
print("-" * 50)

unit_price = 19.99
quantity = 3
tax_rate = 0.08  # 8% tax
discount_rate = 0.1  # 10% discount

subtotal = unit_price * quantity
discount = subtotal * discount_rate
after_discount = subtotal - discount
tax = after_discount * tax_rate
total = after_discount + tax

print(f"Unit price: ${unit_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount (10%): -${discount:.2f}")
print(f"After discount: ${after_discount:.2f}")
print(f"Tax (8%): +${tax:.2f}")
print(f"Total: ${total:.2f}")
print()

# ============================================================================
# EXAMPLE 10: Percentage Calculations
# ============================================================================
# Working with percentages

print("Example 10: Percentage Calculations")
print("-" * 50)

original = 100
increase = 25

new_value = original + (original * increase / 100)
print(f"Original: {original}")
print(f"Increase by {increase}%: {new_value}")
print()

price = 50
discount_pct = 20
discount_amount = price * (discount_pct / 100)
final_price = price - discount_amount
print(f"Price: ${price:.2f}")
print(f"Discount {discount_pct}%: -${discount_amount:.2f}")
print(f"Final price: ${final_price:.2f}")
print()

# ============================================================================
# EXAMPLE 11: Distance and Speed Calculations
# ============================================================================
# Physics: distance = speed × time

print("Example 11: Distance and Speed")
print("-" * 50)

speed = 60  # miles per hour
time = 2.5  # hours

distance = speed * time
print(f"Speed: {speed} mph")
print(f"Time: {time} hours")
print(f"Distance: {distance} miles")
print()

# Reverse calculation
distance = 150  # miles
time = 3  # hours
speed = distance / time
print(f"Distance: {distance} miles")
print(f"Time: {time} hours")
print(f"Speed: {speed} mph")
print()

# ============================================================================
# EXAMPLE 12: Temperature Conversion
# ============================================================================
# Formula: F = C × 9/5 + 32

print("Example 12: Temperature Conversion")
print("-" * 50)

celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")
print()

# Reverse
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.1f}°C")
print()

# ============================================================================
# EXAMPLE 13: Average Calculation
# ============================================================================
# Sum divided by count

print("Example 13: Average (Mean)")
print("-" * 50)

scores = [85, 92, 78, 95, 88]
total = sum(scores)
count = len(scores)
average = total / count

print(f"Scores: {scores}")
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average:.2f}")
print()

# ============================================================================
# EXAMPLE 14: Compound Interest
# ============================================================================
# Formula: A = P(1 + r)^t

print("Example 14: Compound Interest")
print("-" * 50)

principal = 1000  # Initial amount
rate = 0.05  # 5% annual rate
years = 10

final_amount = principal * (1 + rate) ** years

print(f"Principal: ${principal:.2f}")
print(f"Rate: {rate * 100}%")
print(f"Years: {years}")
print(f"Final amount: ${final_amount:.2f}")
print(f"Interest earned: ${final_amount - principal:.2f}")
print()

# ============================================================================
# EXAMPLE 15: Area and Volume Calculations
# ============================================================================
# Geometry

print("Example 15: Geometry Calculations")
print("-" * 50)

# Circle area: A = π × r²
import math
radius = 5
circle_area = math.pi * radius ** 2
circle_circumference = 2 * math.pi * radius

print(f"Circle with radius {radius}:")
print(f"  Area: {circle_area:.2f}")
print(f"  Circumference: {circle_circumference:.2f}")
print()

# Rectangle area: A = length × width
length = 10
width = 5
rect_area = length * width
rect_perimeter = 2 * (length + width)

print(f"Rectangle {length} × {width}:")
print(f"  Area: {rect_area}")
print(f"  Perimeter: {rect_perimeter}")
print()

# Sphere volume: V = (4/3) × π × r³
radius = 3
sphere_volume = (4/3) * math.pi * radius ** 3

print(f"Sphere with radius {radius}:")
print(f"  Volume: {sphere_volume:.2f}")
print()

# ============================================================================
# EXAMPLE 16: Floating-Point Precision Issues
# ============================================================================
# Rounding errors in decimal arithmetic

print("Example 16: Floating-Point Precision")
print("-" * 50)

print("Problem: 0.1 + 0.2 should equal 0.3")
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"Is it exactly 0.3? {result == 0.3}")
print()

print("This is a known limitation of binary floating-point")
print("Solution 1: Accept small differences")
if abs(result - 0.3) < 0.0001:
    print("  Close enough!")
print()

print("Solution 2: Round the result")
result_rounded = round(0.1 + 0.2, 2)
print(f"  Rounded: {result_rounded}")
print()

print("Solution 3: Use Decimal module (for money)")
from decimal import Decimal
price = Decimal("19.99")
tax = Decimal("1.60")
total = price + tax
print(f"  ${price} + ${tax} = ${total}")
print()

# ============================================================================
# EXAMPLE 17: Division by Zero Protection
# ============================================================================
# Preventing errors

print("Example 17: Division by Zero")
print("-" * 50)

numerator = 10
denominator = 0

if denominator != 0:
    result = numerator / denominator
    print(f"{numerator} / {denominator} = {result}")
else:
    print(f"Cannot divide {numerator} by {denominator}")
    print("(Division by zero is undefined)")
print()

# ============================================================================
# EXAMPLE 18: Calculating Discounted Price Step by Step
# ============================================================================
# Breaking down calculation for clarity

print("Example 18: Step-by-Step Calculation")
print("-" * 50)

original_price = 99.99
discount_percent = 15
tax_percent = 8

print(f"Original price: ${original_price:.2f}")
print()

# Step 1: Calculate discount
discount_amount = original_price * (discount_percent / 100)
print(f"Step 1: Calculate discount ({discount_percent}%)")
print(f"  ${original_price:.2f} × {discount_percent}% = ${discount_amount:.2f}")
print()

# Step 2: Subtract discount
discounted_price = original_price - discount_amount
print(f"Step 2: Subtract discount")
print(f"  ${original_price:.2f} - ${discount_amount:.2f} = ${discounted_price:.2f}")
print()

# Step 3: Calculate tax
tax_amount = discounted_price * (tax_percent / 100)
print(f"Step 3: Calculate tax ({tax_percent}%)")
print(f"  ${discounted_price:.2f} × {tax_percent}% = ${tax_amount:.2f}")
print()

# Step 4: Add tax
final_price = discounted_price + tax_amount
print(f"Step 4: Add tax")
print(f"  ${discounted_price:.2f} + ${tax_amount:.2f} = ${final_price:.2f}")
print()

print(f"FINAL PRICE: ${final_price:.2f}")
print()

# ============================================================================
# EXAMPLE 19: Bank Account Simulation
# ============================================================================
# Tracking account balance

print("Example 19: Bank Account Balance")
print("-" * 50)

balance = 1000
print(f"Starting balance: ${balance:.2f}")
print()

# Deposit
deposit = 500
balance = balance + deposit
print(f"Deposit: +${deposit:.2f}")
print(f"Balance: ${balance:.2f}")
print()

# Withdrawal
withdrawal = 200
balance = balance - withdrawal
print(f"Withdrawal: -${withdrawal:.2f}")
print(f"Balance: ${balance:.2f}")
print()

# Interest
interest_rate = 0.02  # 2% annual
interest = balance * interest_rate
balance = balance + interest
print(f"Annual interest (2%): +${interest:.2f}")
print(f"Balance: ${balance:.2f}")
print()

# Fee
fee = 10
balance = balance - fee
print(f"Monthly fee: -${fee:.2f}")
print(f"Final balance: ${balance:.2f}")
print()

# ============================================================================
# EXAMPLE 20: Loan Payment Calculation
# ============================================================================
# Simple interest loan

print("Example 20: Loan Payment Calculation")
print("-" * 50)

principal = 10000  # Borrowed amount
annual_rate = 0.06  # 6% per year
years = 5

# Simple interest formula: I = P × r × t
interest = principal * annual_rate * years
total_to_pay = principal + interest
monthly_payment = total_to_pay / (years * 12)

print(f"Loan amount: ${principal:,.2f}")
print(f"Annual rate: {annual_rate * 100}%")
print(f"Period: {years} years")
print()
print(f"Interest: ${interest:,.2f}")
print(f"Total to pay: ${total_to_pay:,.2f}")
print(f"Monthly payment: ${monthly_payment:,.2f}")
print()

# ============================================================================
# EXAMPLE 21: BMI Calculation
# ============================================================================
# Body Mass Index: BMI = weight / (height²)

print("Example 21: BMI (Body Mass Index)")
print("-" * 50)

weight_kg = 70  # kilograms
height_m = 1.75  # meters

bmi = weight_kg / (height_m ** 2)

print(f"Weight: {weight_kg} kg")
print(f"Height: {height_m} m")
print(f"BMI: {bmi:.1f}")
print()

# Categorize
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")
print()

# ============================================================================
# EXAMPLE 22: Tip Calculation
# ============================================================================
# Common tip calculation

print("Example 22: Tip Calculator")
print("-" * 50)

bill_amount = 45.00
tip_percent = 20  # 20% tip

tip_amount = bill_amount * (tip_percent / 100)
total_with_tip = bill_amount + tip_amount

print(f"Bill: ${bill_amount:.2f}")
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total: ${total_with_tip:.2f}")
print()

# Different tip options
print("Tip options:")
for pct in [15, 18, 20, 25]:
    tip = bill_amount * (pct / 100)
    total = bill_amount + tip
    print(f"  {pct}%: ${tip:.2f} → Total: ${total:.2f}")
print()

# ============================================================================
# EXAMPLE 23: Probability and Odds
# ============================================================================
# Basic probability calculations

print("Example 23: Probability")
print("-" * 50)

# Probability of an event
favorable = 3  # Red balls
total = 10     # Total balls

probability = favorable / total
percentage = probability * 100

print(f"Red balls: {favorable}")
print(f"Total balls: {total}")
print(f"Probability of red: {probability:.2f}")
print(f"Percentage: {percentage:.1f}%")
print()

# Odds (different from probability)
unfavorable = total - favorable
odds = favorable / unfavorable
print(f"Odds of red: {favorable}:{unfavorable} (or {odds:.2f})")
print()

# ============================================================================
# EXAMPLE 24: Power Consumption and Cost
# ============================================================================
# Calculate electricity usage and cost

print("Example 24: Electricity Cost")
print("-" * 50)

power_watts = 100  # Light bulb
hours_per_day = 8
days = 30
cost_per_kwh = 0.12  # Dollars per kilowatt-hour

# Calculate energy usage in kilowatt-hours
total_hours = hours_per_day * days
energy_kwh = (power_watts / 1000) * total_hours

# Calculate cost
cost = energy_kwh * cost_per_kwh

print(f"Power: {power_watts}W")
print(f"Usage: {hours_per_day} hours/day × {days} days")
print(f"Total hours: {total_hours}")
print(f"Energy used: {energy_kwh} kWh")
print(f"Cost per kWh: ${cost_per_kwh}")
print(f"Total cost: ${cost:.2f}")
print()

# ============================================================================
# EXAMPLE 25: Complex Formula - Friction Force
# ============================================================================
# Physics: F = μ × N, where N = m × g

print("Example 25: Physics - Friction Force")
print("-" * 50)

mass = 50  # kg
g = 9.8  # acceleration due to gravity
mu = 0.3  # coefficient of friction

# Normal force
normal_force = mass * g

# Friction force
friction_force = mu * normal_force

print(f"Mass: {mass} kg")
print(f"Gravity: {g} m/s²")
print(f"Coefficient of friction: {mu}")
print()
print(f"Normal force: {normal_force} N")
print(f"Friction force: {friction_force} N")
print()

# Acceleration if force applied
applied_force = 200
net_force = applied_force - friction_force
acceleration = net_force / mass

print(f"Applied force: {applied_force} N")
print(f"Net force: {net_force} N")
print(f"Acceleration: {acceleration:.2f} m/s²")
print()

