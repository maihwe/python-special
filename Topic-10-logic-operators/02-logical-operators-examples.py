# Topic 10: Logical Operators - Elaborate Examples
# Comprehensive examples of combining conditions with and, or, not

# ============================================================================
# EXAMPLE 1: Basic 'and' Operator
# ============================================================================
# Both conditions must be true

print("Example 1: The 'and' Operator")
print("-" * 50)

age = 25
has_license = True

print(f"Age: {age}, Has License: {has_license}")
print()

print(f"age >= 18: {age >= 18}")
print(f"has_license: {has_license}")
print(f"age >= 18 and has_license: {age >= 18 and has_license}")
print()

age = 25
has_license = False

print(f"Age: {age}, Has License: {has_license}")
print(f"age >= 18 and has_license: {age >= 18 and has_license}")
print()

# ============================================================================
# EXAMPLE 2: Basic 'or' Operator
# ============================================================================
# At least one condition must be true

print("Example 2: The 'or' Operator")
print("-" * 50)

is_weekend = False
is_holiday = True

print(f"Is Weekend: {is_weekend}, Is Holiday: {is_holiday}")
print()

print(f"is_weekend: {is_weekend}")
print(f"is_holiday: {is_holiday}")
print(f"is_weekend or is_holiday: {is_weekend or is_holiday}")
print()

is_weekend = False
is_holiday = False

print(f"Is Weekend: {is_weekend}, Is Holiday: {is_holiday}")
print(f"is_weekend or is_holiday: {is_weekend or is_holiday}")
print()

# ============================================================================
# EXAMPLE 3: The 'not' Operator
# ============================================================================
# Reverses boolean value

print("Example 3: The 'not' Operator")
print("-" * 50)

is_raining = False

print(f"is_raining: {is_raining}")
print(f"not is_raining: {not is_raining}")
print()

is_raining = True
print(f"is_raining: {is_raining}")
print(f"not is_raining: {not is_raining}")
print()

# ============================================================================
# EXAMPLE 4: Truth Tables
# ============================================================================
# All combinations of and/or

print("Example 4: Truth Tables")
print("-" * 50)

print("AND Truth Table:")
print("A     B     A and B")
print("-" * 20)

for a in [True, False]:
    for b in [True, False]:
        result = a and b
        print(f"{str(a):5} {str(b):5} {str(result):7}")

print()

print("OR Truth Table:")
print("A     B     A or B")
print("-" * 20)

for a in [True, False]:
    for b in [True, False]:
        result = a or b
        print(f"{str(a):5} {str(b):5} {str(result):6}")

print()

# ============================================================================
# EXAMPLE 5: Three-Way 'and'
# ============================================================================
# All three must be true

print("Example 5: Multiple 'and' Conditions")
print("-" * 50)

age = 25
has_license = True
has_insurance = True

print(f"Age: {age}, License: {has_license}, Insurance: {has_insurance}")
print()

result = age >= 18 and has_license and has_insurance
print(f"Can drive: {result}")
print()

has_insurance = False
print(f"Age: {age}, License: {has_license}, Insurance: {has_insurance}")
result = age >= 18 and has_license and has_insurance
print(f"Can drive: {result}")
print()

# ============================================================================
# EXAMPLE 6: Three-Way 'or'
# ============================================================================
# At least one must be true

print("Example 6: Multiple 'or' Conditions")
print("-" * 50)

has_student_id = False
has_military_id = True
has_senior_card = False

print(f"Student ID: {has_student_id}")
print(f"Military ID: {has_military_id}")
print(f"Senior Card: {has_senior_card}")
print()

result = has_student_id or has_military_id or has_senior_card
print(f"Eligible for discount: {result}")
print()

has_military_id = False
print(f"Student ID: {has_student_id}")
print(f"Military ID: {has_military_id}")
print(f"Senior Card: {has_senior_card}")
result = has_student_id or has_military_id or has_senior_card
print(f"Eligible for discount: {result}")
print()

# ============================================================================
# EXAMPLE 7: Operator Precedence
# ============================================================================
# not > and > or

print("Example 7: Operator Precedence")
print("-" * 50)

result = True or False and False
print(f"True or False and False = {result}")
print(f"(Evaluated as: True or (False and False) = True)")
print()

result = (True or False) and False
print(f"(True or False) and False = {result}")
print()

result = not True or True
print(f"not True or True = {result}")
print(f"(Evaluated as: (not True) or True = False or True = True)")
print()

# ============================================================================
# EXAMPLE 8: De Morgan's Law 1
# ============================================================================
# not (A and B) = (not A) or (not B)

print("Example 8: De Morgan's Law 1")
print("-" * 50)

age = 15
has_license = False

# Method 1
result1 = not (age >= 18 and has_license)
print(f"not (age >= 18 and has_license): {result1}")

# Method 2 (De Morgan's)
result2 = (age < 18) or (not has_license)
print(f"(age < 18) or (not has_license): {result2}")

print(f"Both methods equal: {result1 == result2}")
print()

# ============================================================================
# EXAMPLE 9: De Morgan's Law 2
# ============================================================================
# not (A or B) = (not A) and (not B)

print("Example 9: De Morgan's Law 2")
print("-" * 50)

is_admin = False
is_moderator = False

# Method 1
result1 = not (is_admin or is_moderator)
print(f"not (is_admin or is_moderator): {result1}")

# Method 2 (De Morgan's)
result2 = (not is_admin) and (not is_moderator)
print(f"(not is_admin) and (not is_moderator): {result2}")

print(f"Both methods equal: {result1 == result2}")
print()

# ============================================================================
# EXAMPLE 10: Short-Circuit Evaluation with 'and'
# ============================================================================
# Second condition not evaluated if first is false

print("Example 10: Short-Circuit with 'and'")
print("-" * 50)

def check_something():
    print("  Checking something (expensive operation)")
    return True

username = "alice"

print("Test 1: username == 'bob' and check_something()")
result = username == "bob" and check_something()
print(f"Result: {result}")
print("(Note: check_something() was NOT called)")
print()

print("Test 2: username == 'alice' and check_something()")
result = username == "alice" and check_something()
print(f"Result: {result}")
print("(Note: check_something() WAS called)")
print()

# ============================================================================
# EXAMPLE 11: Short-Circuit Evaluation with 'or'
# ============================================================================
# Second condition not evaluated if first is true

print("Example 11: Short-Circuit with 'or'")
print("-" * 50)

def check_other():
    print("  Checking other (expensive operation)")
    return False

is_admin = True

print("Test 1: is_admin or check_other()")
result = is_admin or check_other()
print(f"Result: {result}")
print("(Note: check_other() was NOT called)")
print()

is_admin = False

print("Test 2: is_admin or check_other()")
result = is_admin or check_other()
print(f"Result: {result}")
print("(Note: check_other() WAS called)")
print()

# ============================================================================
# EXAMPLE 12: Combining 'and' and 'or'
# ============================================================================
# Mixed operators with precedence

print("Example 12: Mixing 'and' and 'or'")
print("-" * 50)

score = 85
is_makeup = False
is_extra_credit = True

# Original: (score >= 80) or ((is_makeup) and (is_extra_credit))
result = score >= 80 or is_makeup and is_extra_credit
print(f"score >= 80 or is_makeup and is_extra_credit")
print(f"Score: {score}, Makeup: {is_makeup}, Extra: {is_extra_credit}")
print(f"Result: {result}")
print()

# Different grouping
result = (score >= 80 or is_makeup) and is_extra_credit
print(f"(score >= 80 or is_makeup) and is_extra_credit")
print(f"Result: {result}")
print()

# ============================================================================
# EXAMPLE 13: Real-World: Login System
# ============================================================================
# Multiple conditions for access

print("Example 13: Login System")
print("-" * 50)

username = "alice"
password = "secret123"
is_2fa_verified = True
account_active = True

correct_username = "alice"
correct_password = "secret123"

print(f"Username: {username}")
print(f"Password: {password}")
print(f"2FA verified: {is_2fa_verified}")
print(f"Account active: {account_active}")
print()

can_login = (username == correct_username and 
             password == correct_password and 
             is_2fa_verified and 
             account_active)

print(f"Can login: {can_login}")
print()

# ============================================================================
# EXAMPLE 14: Real-World: Discount Eligibility
# ============================================================================
# Multiple paths to discount

print("Example 14: Discount Eligibility")
print("-" * 50)

purchase_amount = 50
is_member = True
is_sale_day = False
has_coupon = False

print(f"Purchase: ${purchase_amount}")
print(f"Is member: {is_member}")
print(f"Sale day: {is_sale_day}")
print(f"Has coupon: {has_coupon}")
print()

# Eligible if: member OR on sale day OR has coupon
eligible = is_member or is_sale_day or has_coupon
print(f"Eligible for discount: {eligible}")
print()

# Multiple discounts: best one wins
regular_discount = purchase_amount >= 50  # $50+
member_discount = is_member              # Members
sale_discount = is_sale_day              # Sale day

print(f"Regular discount (>=50): {regular_discount}")
print(f"Member discount: {member_discount}")
print(f"Sale discount: {sale_discount}")
print(f"Gets some discount: {regular_discount or member_discount or sale_discount}")
print()

# ============================================================================
# EXAMPLE 15: Real-World: Game Power-Up
# ============================================================================
# Complex game logic

print("Example 15: Game Power-Up Logic")
print("-" * 50)

player_health = 50
has_shield = False
has_invulnerability = True
enemy_strength = 30

print(f"Player health: {player_health}")
print(f"Has shield: {has_shield}")
print(f"Has invulnerability: {has_invulnerability}")
print(f"Enemy strength: {enemy_strength}")
print()

# Can survive attack if:
can_survive = (player_health > enemy_strength) or has_shield or has_invulnerability

print(f"Can survive attack: {can_survive}")
print()

# ============================================================================
# EXAMPLE 16: Validation with Multiple Checks
# ============================================================================
# Data quality checks

print("Example 16: Data Validation")
print("-" * 50)

email = "john@example.com"

has_at = "@" in email
has_dot = "." in email
has_domain = email.count("@") == 1
no_spaces = " " not in email

print(f"Email: {email}")
print(f"Has @: {has_at}")
print(f"Has dot: {has_dot}")
print(f"Valid domain: {has_domain}")
print(f"No spaces: {no_spaces}")
print()

is_valid = has_at and has_dot and has_domain and no_spaces
print(f"Is valid email: {is_valid}")
print()

# ============================================================================
# EXAMPLE 17: Access Control by Role
# ============================================================================
# Different permissions for different roles

print("Example 17: Permission by Role")
print("-" * 50)

user_role = "editor"
file_owner = False
is_admin = False

can_view = True
can_edit = (user_role == "editor" or user_role == "admin" or file_owner)
can_delete = (user_role == "admin" or (file_owner and user_role != "viewer"))
can_share = (user_role == "admin" or file_owner)

print(f"User role: {user_role}, File owner: {file_owner}, Admin: {is_admin}")
print()
print(f"Can view: {can_view}")
print(f"Can edit: {can_edit}")
print(f"Can delete: {can_delete}")
print(f"Can share: {can_share}")
print()

# ============================================================================
# EXAMPLE 18: Guard Clause Pattern
# ============================================================================
# Exit early if conditions not met

print("Example 18: Guard Clause")
print("-" * 50)

def process_user(user_age, user_verified):
    print(f"Processing user (age {user_age}, verified {user_verified})")
    
    if not user_verified:
        print("  ✗ User not verified - stopping")
        return
    
    if user_age < 18:
        print("  ✗ User too young - stopping")
        return
    
    print("  ✓ Processing user...")

process_user(25, True)
print()
process_user(15, True)
print()
process_user(25, False)
print()

# ============================================================================
# EXAMPLE 19: Complex Discount Logic
# ============================================================================
# Real-world e-commerce

print("Example 19: Complex Discount Logic")
print("-" * 50)

purchase_amount = 150
is_member = True
is_first_time = False
has_expired_coupon = False

# Multiple discount scenarios
is_large_purchase = purchase_amount >= 100
is_member_discount = is_member and purchase_amount >= 50
is_first_order_discount = is_first_time and not has_expired_coupon

print(f"Amount: ${purchase_amount}")
print(f"Member: {is_member}, First time: {is_first_time}")
print()

print(f"Large purchase (>=100): {is_large_purchase}")
print(f"Member discount (>=50): {is_member_discount}")
print(f"First order discount: {is_first_order_discount}")
print()

eligible_for_discount = is_large_purchase or is_member_discount or is_first_order_discount
print(f"Eligible for any discount: {eligible_for_discount}")
print()

# ============================================================================
# EXAMPLE 20: Password Strength
# ============================================================================
# Complex validation

print("Example 20: Password Strength")
print("-" * 50)

password = "SecurePass123!"

has_uppercase = any(c.isupper() for c in password)
has_lowercase = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*" for c in password)
is_long_enough = len(password) >= 8

print(f"Password: {password}")
print()
print(f"Has uppercase: {has_uppercase}")
print(f"Has lowercase: {has_lowercase}")
print(f"Has digit: {has_digit}")
print(f"Has special char: {has_special}")
print(f"Long enough (8+): {is_long_enough}")
print()

# Very strong: all requirements
is_very_strong = has_uppercase and has_lowercase and has_digit and has_special and is_long_enough
print(f"Very strong: {is_very_strong}")

# Strong: most requirements
is_strong = (has_uppercase and has_lowercase and has_digit and is_long_enough)
print(f"Strong: {is_strong}")

# Acceptable: at least length + one other
is_acceptable = is_long_enough and (has_uppercase or has_lowercase or has_digit)
print(f"Acceptable: {is_acceptable}")
print()

# ============================================================================
# EXAMPLE 21: Breaking Complex Conditions into Parts
# ============================================================================
# Readability strategy

print("Example 21: Named Conditions")
print("-" * 50)

# Hard to read all in one line
age = 25
income = 50000
credit_score = 750
has_collateral = True

# Bad: unclear what condition is for
if age >= 21 and income >= 30000 and credit_score >= 700 and has_collateral:
    print("Hard to understand what this is checking")

print()

# Good: each condition has meaning
is_age_ok = age >= 21
is_income_ok = income >= 30000
is_creditworthy = credit_score >= 700
has_security = has_collateral

if is_age_ok and is_income_ok and is_creditworthy and has_security:
    print("✓ Clear that this checks loan eligibility")
print()

# ============================================================================
# EXAMPLE 22: Or with Early Exit
# ============================================================================
# Finding acceptable values

print("Example 22: Or for Multiple Acceptable Values")
print("-" * 50)

response = "y"

# Verbose: many ifs
if response == "yes":
    accepted = True
elif response == "y":
    accepted = True
elif response == "Y":
    accepted = True
else:
    accepted = False

print(f"Response: '{response}'")
print(f"Accepted (verbose): {accepted}")

# Better: use or
accepted = response == "yes" or response == "y" or response == "Y"
print(f"Accepted (with or): {accepted}")

# Best: use in
accepted = response in ["yes", "y", "Y"]
print(f"Accepted (with in): {accepted}")
print()

# ============================================================================
# EXAMPLE 23: Not with Null Checking
# ============================================================================
# Safe null handling

print("Example 23: Safe Null Checking")
print("-" * 50)

user = None

# Unsafe: accesses user.name without checking if user exists
# if user.name == "admin":  # Would crash!

# Safe with 'not'
if user is not None and user.name == "admin":
    print("User is admin")
else:
    print("User not admin (or not logged in)")

print()

user = type('obj', (object,), {'name': 'alice'})()

if user is not None and user.name == "admin":
    print("User is admin")
else:
    print("User is not admin (or not logged in)")
print()

# ============================================================================
# EXAMPLE 24: Chained Comparisons with Logical Operators
# ============================================================================
# Combining both tools

print("Example 24: Comparisons + Logical Operators")
print("-" * 50)

score = 85
recent = True
verified = True

# Multiple ranges with or
grade = ""
if score >= 90 or (score >= 80 and recent and verified):
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"

print(f"Score: {score}, Recent: {recent}, Verified: {verified}")
print(f"Grade: {grade}")
print()

# ============================================================================
# EXAMPLE 25: Real-World: Spam Detection
# ============================================================================
# Complex multi-factor logic

print("Example 25: Spam Detection")
print("-" * 50)

message_length = 5
has_links = True
from_verified = False
sender_reputation = 0.2  # out of 1.0

# Flags for spam indicators
is_too_short = message_length < 10
has_suspicious_links = has_links and not from_verified
is_from_bad_sender = sender_reputation < 0.5

print(f"Message length: {message_length}")
print(f"Has links: {has_links}, From verified: {from_verified}")
print(f"Sender reputation: {sender_reputation}")
print()

print(f"Too short: {is_too_short}")
print(f"Suspicious links: {has_suspicious_links}")
print(f"Bad sender: {is_from_bad_sender}")
print()

# Likely spam if multiple indicators
likely_spam = (is_too_short and has_suspicious_links) or is_from_bad_sender
print(f"Likely spam: {likely_spam}")

# Definitely spam if all indicators
definitely_spam = is_too_short and has_suspicious_links and is_from_bad_sender
print(f"Definitely spam: {definitely_spam}")

