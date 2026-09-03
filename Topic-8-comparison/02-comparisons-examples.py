# Topic 8: Comparisons - Elaborate Examples
# Comprehensive examples of comparing values in Python

# ============================================================================
# EXAMPLE 1: Basic Equality Comparisons
# ============================================================================
# Testing if values are the same

print("Example 1: Equality Comparisons")
print("-" * 50)

# Integers
print(f"5 == 5: {5 == 5}")
print(f"5 == 3: {5 == 3}")
print(f"5 != 3: {5 != 3}")
print(f"5 != 5: {5 != 5}")
print()

# Strings
print(f"'hello' == 'hello': {'hello' == 'hello'}")
print(f"'hello' == 'HELLO': {'hello' == 'HELLO'}")
print(f"'hello' != 'world': {'hello' != 'world'}")
print()

# Mixed numeric types
print(f"5 == 5.0: {5 == 5.0}")
print(f"5 != 5.0: {5 != 5.0}")
print()

# ============================================================================
# EXAMPLE 2: Greater Than and Less Than
# ============================================================================
# Testing ordering relationships

print("Example 2: Ordering Comparisons")
print("-" * 50)

a = 10
b = 5

print(f"a = {a}, b = {b}")
print()
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"b < a: {b < a}")
print(f"a > a: {a > a}")
print()

# With floats
x = 3.5
y = 3.2
print(f"x = {x}, y = {y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print()

# ============================================================================
# EXAMPLE 3: Greater/Less Than or Equal
# ============================================================================
# Testing boundary conditions

print("Example 3: Greater/Less Than or Equal")
print("-" * 50)

score = 85
passing_score = 85

print(f"Score: {score}, Passing: {passing_score}")
print(f"score >= passing_score: {score >= passing_score}")
print(f"score > passing_score: {score > passing_score}")
print()

# Temperature check
temp = 32
freezing = 32
print(f"Temperature: {temp}°F, Freezing point: {freezing}°F")
print(f"temp <= freezing: {temp <= freezing}")
print(f"temp < freezing: {temp < freezing}")
print()

# ============================================================================
# EXAMPLE 4: String Comparisons - Alphabetical Order
# ============================================================================
# Strings compare character by character

print("Example 4: String Comparisons")
print("-" * 50)

print(f"'apple' < 'banana': {'apple' < 'banana'}")
print(f"'zebra' > 'apple': {'zebra' > 'apple'}")
print(f"'apple' == 'apple': {'apple' == 'apple'}")
print(f"'Apple' == 'apple': {'Apple' == 'apple'}")
print()

print("Shorter strings come first:")
print(f"'cat' < 'dog': {'cat' < 'dog'}")
print(f"'cat' < 'category': {'cat' < 'category'}")
print()

print("Case matters (uppercase < lowercase in ASCII):")
print(f"'Apple' < 'apple': {'Apple' < 'apple'}")
print()

# ============================================================================
# EXAMPLE 5: Equality of Different Types
# ============================================================================
# Mixed type comparisons

print("Example 5: Different Type Comparisons")
print("-" * 50)

print(f"5 == 5.0: {5 == 5.0}")
print(f"5 == '5': {5 == '5'}")
print(f"5.0 == '5.0': {5.0 == '5.0'}")
print()

print("To compare across types, convert first:")
print(f"int('5') == 5: {int('5') == 5}")
print(f"str(5) == '5': {str(5) == '5'}")
print()

# ============================================================================
# EXAMPLE 6: Boolean Comparisons
# ============================================================================
# Comparing boolean values

print("Example 6: Boolean Comparisons")
print("-" * 50)

print(f"True == True: {True == True}")
print(f"True == False: {True == False}")
print(f"True == 1: {True == 1}")
print(f"False == 0: {False == 0}")
print()

print("Note: Python allows bool vs int comparison")
print(f"True > False: {True > False}")
print()

# ============================================================================
# EXAMPLE 7: Identity - is vs ==
# ============================================================================
# Difference between equality and identity

print("Example 7: Identity (is) vs Equality (==)")
print("-" * 50)

# Lists
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x = {x}")
print(f"y = {y}")
print(f"z = x")
print()

print(f"x == y: {x == y}  (same contents)")
print(f"x is y: {x is y}  (different objects)")
print(f"x is z: {x is z}  (same object)")
print()

# None checks
value = None
print(f"value = {value}")
print(f"value is None: {value is None}  (correct way)")
print(f"value == None: {value == None}  (works but not preferred)")
print()

# ============================================================================
# EXAMPLE 8: Membership Testing - in Operator
# ============================================================================
# Testing if value exists in collection

print("Example 8: Membership Testing (in)")
print("-" * 50)

numbers = [1, 2, 3, 4, 5]
print(f"List: {numbers}")
print()

print(f"3 in numbers: {3 in numbers}")
print(f"10 in numbers: {10 in numbers}")
print(f"3 not in numbers: {3 not in numbers}")
print(f"10 not in numbers: {10 not in numbers}")
print()

# Strings
text = "hello"
print(f"Text: '{text}'")
print(f"'h' in text: {'h' in text}")
print(f"'x' in text: {'x' in text}")
print(f"'ell' in text: {'ell' in text}")
print()

# ============================================================================
# EXAMPLE 9: Comparison Result Type
# ============================================================================
# Comparisons always return boolean

print("Example 9: Comparison Results Are Booleans")
print("-" * 50)

result = 5 > 3
print(f"result = 5 > 3")
print(f"result: {result}")
print(f"type(result): {type(result).__name__}")
print()

# Store comparison result in variable
age = 25
is_adult = age >= 18
print(f"age = {age}")
print(f"is_adult = age >= 18")
print(f"is_adult: {is_adult}")
print(f"type(is_adult): {type(is_adult).__name__}")
print()

# ============================================================================
# EXAMPLE 10: Comparison Chains
# ============================================================================
# Multiple comparisons in one expression

print("Example 10: Comparison Chains")
print("-" * 50)

x = 5
print(f"x = {x}")
print()

print(f"1 < x < 10: {1 < x < 10}")
print(f"Same as: (1 < x) and (x < 10): {(1 < x) and (x < 10)}")
print()

# Range checking
score = 85
print(f"Score: {score}")
print(f"80 <= score < 90: {80 <= score < 90}  (B grade range)")
print()

# More complex chain
a = 2
b = 5
c = 8
print(f"a={a}, b={b}, c={c}")
print(f"a < b < c: {a < b < c}")
print()

# ============================================================================
# EXAMPLE 11: Real-World Scenario - Age Verification
# ============================================================================
# Checking eligibility based on age

print("Example 11: Age Verification")
print("-" * 50)

age = 21
print(f"Age: {age}")
print()

if age >= 21:
    print("✓ Can buy alcohol")
else:
    print("✗ Cannot buy alcohol")

if age >= 18:
    print("✓ Can vote")
else:
    print("✗ Cannot vote")

if age >= 65:
    print("✓ Eligible for senior discount")
else:
    print("✗ Not yet senior")

if 13 <= age < 18:
    print("✓ Teenager")
else:
    print("✗ Not a teenager")
print()

# ============================================================================
# EXAMPLE 12: Real-World Scenario - Grade Assignment
# ============================================================================
# Assigning grades based on score ranges

print("Example 12: Grade Assignment")
print("-" * 50)

score = 87
print(f"Score: {score}")
print()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
print()

# Alternative using comparison chains
if 90 <= score <= 100:
    print("A grade range")
elif 80 <= score < 90:
    print("B grade range")
elif 70 <= score < 80:
    print("C grade range")
print()

# ============================================================================
# EXAMPLE 13: Real-World Scenario - Password Validation
# ============================================================================
# Checking password strength

print("Example 13: Password Validation")
print("-" * 50)

password = "mypassword123"
print(f"Password: {password}")
print()

is_long_enough = len(password) >= 8
print(f"Length >= 8: {is_long_enough}")

has_letter = any(c.isalpha() for c in password)
print(f"Has letter: {has_letter}")

has_digit = any(c.isdigit() for c in password)
print(f"Has digit: {has_digit}")

is_valid = is_long_enough and has_letter and has_digit
print(f"Valid password: {is_valid}")
print()

# ============================================================================
# EXAMPLE 14: Real-World Scenario - Inventory Status
# ============================================================================
# Checking if items need reordering

print("Example 14: Inventory Status")
print("-" * 50)

items = [
    ("Widget", 5, 10),
    ("Gadget", 15, 10),
    ("Gizmo", 3, 10),
]

print("Item       Stock  Min   Status")
print("-" * 40)

for name, stock, minimum in items:
    if stock < minimum:
        status = "REORDER"
    elif stock <= minimum * 1.5:
        status = "LOW"
    else:
        status = "OK"
    
    print(f"{name:10} {stock:5}  {minimum:5}  {status}")
print()

# ============================================================================
# EXAMPLE 15: Real-World Scenario - Temperature Alert System
# ============================================================================
# Monitoring temperature with thresholds

print("Example 15: Temperature Alerts")
print("-" * 50)

readings = [20, 45, 85, 95, 105, 120]

for temp in readings:
    if temp > 100:
        alert = "CRITICAL: Shutdown"
    elif temp > 80:
        alert = "WARNING: Running hot"
    elif temp > 50:
        alert = "INFO: Elevated"
    elif temp < 0:
        alert = "CRITICAL: Freezing"
    else:
        alert = "Normal"
    
    print(f"Temp: {temp:3}°F → {alert}")
print()

# ============================================================================
# EXAMPLE 16: Multiple Conditions
# ============================================================================
# Combining comparisons with logic

print("Example 16: Multiple Conditions")
print("-" * 50)

username = "alice"
password = "secret123"
is_admin = False

print(f"Username: {username}")
print(f"Password: {password}")
print(f"Is admin: {is_admin}")
print()

# Multiple conditions (all must be true)
if username == "alice" and password == "secret123":
    print("✓ Credentials are correct")
else:
    print("✗ Invalid credentials")

if username != "admin":
    print("✓ Not using admin account")

if not is_admin:
    print("✓ User is not admin")
print()

# ============================================================================
# EXAMPLE 17: Forbidden Values Check
# ============================================================================
# Testing membership for validation

print("Example 17: Forbidden Values")
print("-" * 50)

forbidden_usernames = ["admin", "root", "system", "administrator"]

test_usernames = ["john", "admin", "alice", "root", "bob"]

print(f"Forbidden: {forbidden_usernames}")
print()

for username in test_usernames:
    if username in forbidden_usernames:
        print(f"✗ '{username}' - FORBIDDEN")
    else:
        print(f"✓ '{username}' - Available")
print()

# ============================================================================
# EXAMPLE 18: Numeric Range Validation
# ============================================================================
# Checking if value is within acceptable range

print("Example 18: Range Validation")
print("-" * 50)

acceptable_values = [50, 95, 150, 200, 275, 350]
min_range = 0
max_range = 255

print(f"Valid range: {min_range} - {max_range}")
print()

for val in acceptable_values:
    if min_range <= val <= max_range:
        status = "✓ Valid"
    else:
        status = "✗ Out of range"
    print(f"Value {val}: {status}")
print()

# ============================================================================
# EXAMPLE 19: String Validation
# ============================================================================
# Checking string properties

print("Example 19: String Validation")
print("-" * 50)

words = ["hello", "WORLD", "Python123", "a", ""]

for word in words:
    is_empty = word == ""
    is_uppercase = word == word.upper()
    is_lowercase = word == word.lower()
    has_digit = any(c.isdigit() for c in word)
    
    print(f"'{word:15}' → Empty:{is_empty}, Upper:{is_uppercase}, Lower:{is_lowercase}, Digit:{has_digit}")
print()

# ============================================================================
# EXAMPLE 20: Equality vs Identity with Integers
# ============================================================================
# Python caches small integers

print("Example 20: Integer Caching Behavior")
print("-" * 50)

# Small integers (usually cached)
a = 5
b = 5
print(f"a = 5, b = 5")
print(f"a == b: {a == b}  (same value)")
print(f"a is b: {a is b}  (usually same object, cached)")
print()

# Large integers (usually not cached)
x = 257
y = 257
print(f"x = 257, y = 257")
print(f"x == y: {x == y}  (same value)")
print(f"x is y: {x is y}  (probably different objects, not cached)")
print()

# ============================================================================
# EXAMPLE 21: Case-Sensitive String Comparison
# ============================================================================
# Case matters in Python strings

print("Example 21: Case-Sensitive Comparison")
print("-" * 50)

password_stored = "SecurePassword123"
attempts = ["securepassword123", "SecurePassword123", "SECUREPASSWORD123"]

for attempt in attempts:
    if attempt == password_stored:
        print(f"'{attempt}' ✓ MATCH")
    else:
        print(f"'{attempt}' ✗ no match (case matters)")
print()

# Case-insensitive comparison
print("Case-insensitive check:")
for attempt in attempts:
    if attempt.lower() == password_stored.lower():
        print(f"'{attempt}' ✓ match (ignoring case)")
print()

# ============================================================================
# EXAMPLE 22: Comparison with None
# ============================================================================
# Proper way to check for None

print("Example 22: Checking for None")
print("-" * 50)

values = [None, 0, "", False, [], "hello"]

print("Value        is None?   == None?")
print("-" * 40)

for val in values:
    check_is = val is None
    check_eq = val == None
    print(f"{repr(val):15} {check_is:10} {check_eq:10}")
print()

# ============================================================================
# EXAMPLE 23: Comparing Mixed Lists
# ============================================================================
# Lists are compared element by element

print("Example 23: List Comparisons")
print("-" * 50)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
list4 = [1, 2]

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")
print(f"list4 = {list4}")
print()

print(f"list1 == list2: {list1 == list2}  (same contents)")
print(f"list1 == list3: {list1 == list3}  (different values)")
print(f"list1 < list3: {list1 < list3}  (first difference at index 2)")
print(f"list1 > list4: {list1 > list4}  (longer list is greater)")
print()

# ============================================================================
# EXAMPLE 24: Chained Comparisons with Variables
# ============================================================================
# Using variables in comparison chains

print("Example 24: Chained Comparisons with Variables")
print("-" * 50)

min_score = 70
user_score = 85
max_score = 100

print(f"Score range: {min_score}-{max_score}")
print(f"User score: {user_score}")
print()

print(f"min_score <= user_score <= max_score: {min_score <= user_score <= max_score}")
print(f"user_score > min_score and user_score < max_score: {user_score > min_score and user_score < max_score}")
print()

# ============================================================================
# EXAMPLE 25: Complex Comparisons in Decision Making
# ============================================================================
# Real-world logic combining multiple conditions

print("Example 25: Complex Decision Logic")
print("-" * 50)

# Loan approval system
age = 35
income = 75000
credit_score = 720
employment_years = 3
debt = 20000

print("Loan Application:")
print(f"  Age: {age}")
print(f"  Income: ${income:,}")
print(f"  Credit Score: {credit_score}")
print(f"  Employment: {employment_years} years")
print(f"  Debt: ${debt:,}")
print()

# Check eligibility
is_age_ok = age >= 21
is_income_ok = income >= 40000
is_credit_ok = credit_score >= 700
is_employed = employment_years >= 2
debt_to_income = (debt / income) <= 0.5

print("Checks:")
print(f"  Age >= 21: {is_age_ok}")
print(f"  Income >= $40k: {is_income_ok}")
print(f"  Credit >= 700: {is_credit_ok}")
print(f"  Employed 2+ years: {is_employed}")
print(f"  Debt-to-income ratio OK: {debt_to_income}")
print()

if is_age_ok and is_income_ok and is_credit_ok and is_employed and debt_to_income:
    print("✓ APPROVED")
else:
    print("✗ DENIED")

