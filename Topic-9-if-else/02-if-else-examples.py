# Topic 9: If/Else - Elaborate Examples
# Comprehensive examples of conditional decision-making in Python

# ============================================================================
# EXAMPLE 1: Simple If Statement
# ============================================================================
# Execute code only if condition is true

print("Example 1: Simple If Statement")
print("-" * 50)

age = 18

if age >= 18:
    print(f"Age {age}: You are an adult")

age = 15

if age >= 18:
    print(f"Age {age}: You are an adult")  # Does not execute
    
print("Program continues regardless")
print()

# ============================================================================
# EXAMPLE 2: If/Else - Two Branches
# ============================================================================
# Execute one branch or the other, never both

print("Example 2: If/Else Statement")
print("-" * 50)

score = 75

if score >= 70:
    print(f"Score {score}: PASS")
else:
    print(f"Score {score}: FAIL")

print()

score = 65

if score >= 70:
    print(f"Score {score}: PASS")
else:
    print(f"Score {score}: FAIL")

print()

# ============================================================================
# EXAMPLE 3: Elif - Multiple Branches
# ============================================================================
# Test multiple conditions until one is true

print("Example 3: Elif Statement (Grade Assignment)")
print("-" * 50)

scores = [95, 85, 75, 65, 55]

for score in scores:
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
    
    print(f"Score {score}: Grade {grade}")

print()

# ============================================================================
# EXAMPLE 4: Nested If Statements
# ============================================================================
# Conditions within conditions

print("Example 4: Nested If Statements")
print("-" * 50)

age = 25
has_license = True

if age >= 18:
    print(f"Age {age}: Adult")
    if has_license:
        print("  Has license: Can drive")
    else:
        print("  No license: Cannot drive")
else:
    print(f"Age {age}: Minor")
    print("  Must be 18 to drive")

print()

age = 15
has_license = True

if age >= 18:
    print(f"Age {age}: Adult")
    if has_license:
        print("  Has license: Can drive")
    else:
        print("  No license: Cannot drive")
else:
    print(f"Age {age}: Minor")
    print("  Must be 18 to drive")

print()

# ============================================================================
# EXAMPLE 5: Logical Operator 'and'
# ============================================================================
# Both conditions must be true

print("Example 5: Logical Operator 'and'")
print("-" * 50)

age = 25
has_license = True

if age >= 18 and has_license:
    print(f"✓ Can rent a car (age {age}, license: {has_license})")
else:
    print("✗ Cannot rent a car")

print()

age = 25
has_license = False

if age >= 18 and has_license:
    print(f"✓ Can rent a car (age {age}, license: {has_license})")
else:
    print("✗ Cannot rent a car")

print()

# ============================================================================
# EXAMPLE 6: Logical Operator 'or'
# ============================================================================
# At least one condition must be true

print("Example 6: Logical Operator 'or'")
print("-" * 50)

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("✓ No work today (weekend or holiday)")
else:
    print("✗ Regular work day")

print()

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("✓ No work today (weekend or holiday)")
else:
    print("✗ Regular work day")

print()

# ============================================================================
# EXAMPLE 7: Logical Operator 'not'
# ============================================================================
# Reverse the boolean value

print("Example 7: Logical Operator 'not'")
print("-" * 50)

is_raining = False

if not is_raining:
    print("✓ Go to the park")
else:
    print("✗ Stay inside")

print()

is_raining = True

if not is_raining:
    print("✓ Go to the park")
else:
    print("✗ Stay inside")

print()

# ============================================================================
# EXAMPLE 8: Combining Logical Operators
# ============================================================================
# Complex conditions with multiple operators

print("Example 8: Complex Conditions")
print("-" * 50)

age = 25
has_license = True
has_insurance = True

print(f"Age: {age}, License: {has_license}, Insurance: {has_insurance}")
print()

if age >= 18 and has_license and has_insurance:
    print("✓ Can legally drive")
else:
    print("✗ Cannot drive (missing requirement)")

print()

# Missing one requirement
has_insurance = False

print(f"Age: {age}, License: {has_license}, Insurance: {has_insurance}")
print()

if age >= 18 and has_license and has_insurance:
    print("✓ Can legally drive")
else:
    print("✗ Cannot drive (missing requirement)")

print()

# ============================================================================
# EXAMPLE 9: 'or' with Multiple Conditions
# ============================================================================
# At least one of several must be true

print("Example 9: Multiple 'or' Conditions")
print("-" * 50)

has_student_id = False
has_military_id = True
has_senior_card = False

print(f"Student ID: {has_student_id}")
print(f"Military ID: {has_military_id}")
print(f"Senior Card: {has_senior_card}")
print()

if has_student_id or has_military_id or has_senior_card:
    print("✓ Eligible for discount")
else:
    print("✗ No discount available")

print()

# ============================================================================
# EXAMPLE 10: Username and Password Validation
# ============================================================================
# Real-world: login system

print("Example 10: Login System")
print("-" * 50)

correct_username = "alice"
correct_password = "secret123"

username = "alice"
password = "secret123"

print(f"Login attempt: {username}")
print()

if username == correct_username and password == correct_password:
    print("✓ Login successful")
else:
    print("✗ Invalid credentials")

print()

username = "alice"
password = "wrong"

print(f"Login attempt: {username}")
print()

if username == correct_username and password == correct_password:
    print("✓ Login successful")
else:
    print("✗ Invalid credentials")

print()

# ============================================================================
# EXAMPLE 11: Eligibility Checker
# ============================================================================
# Real-world: multi-criteria approval

print("Example 11: Loan Eligibility")
print("-" * 50)

age = 25
income = 50000
credit_score = 720

print(f"Age: {age}")
print(f"Income: ${income:,}")
print(f"Credit Score: {credit_score}")
print()

is_age_ok = age >= 21
is_income_ok = income >= 30000
is_credit_ok = credit_score >= 650

if is_age_ok and is_income_ok and is_credit_ok:
    print("✓ APPROVED for loan")
else:
    print("✗ DENIED - missing requirements")
    if not is_age_ok:
        print("  - Must be 21 or older")
    if not is_income_ok:
        print("  - Income must be $30,000+")
    if not is_credit_ok:
        print("  - Credit score must be 650+")

print()

# ============================================================================
# EXAMPLE 12: Temperature Alert System
# ============================================================================
# Real-world: monitoring with multiple thresholds

print("Example 12: Temperature Monitoring")
print("-" * 50)

temperatures = [20, 50, 85, 95, 105, 120]

for temp in temperatures:
    if temp > 100:
        status = "CRITICAL - Shutdown"
    elif temp > 80:
        status = "WARNING - Running hot"
    elif temp > 50:
        status = "ELEVATED - Monitor closely"
    elif temp < 0:
        status = "CRITICAL - Freezing"
    else:
        status = "NORMAL"
    
    print(f"Temp: {temp:3}°F → {status}")

print()

# ============================================================================
# EXAMPLE 13: Inventory Status
# ============================================================================
# Real-world: stock level decisions

print("Example 13: Inventory Status")
print("-" * 50)

items = [
    ("Widget", 5, 10),
    ("Gadget", 15, 10),
    ("Gizmo", 3, 10),
]

print("Item       Stock  Min  Status")
print("-" * 40)

for name, stock, minimum in items:
    if stock < minimum:
        status = "🔴 REORDER"
    elif stock <= minimum * 1.5:
        status = "🟡 LOW"
    else:
        status = "🟢 OK"
    
    print(f"{name:10} {stock:5} {minimum:3}  {status}")

print()

# ============================================================================
# EXAMPLE 14: User Role Access Control
# ============================================================================
# Real-world: permission system

print("Example 14: Access Control by Role")
print("-" * 50)

user_role = "moderator"

print(f"User role: {user_role}")
print()

if user_role == "admin":
    print("✓ Can view users")
    print("✓ Can delete users")
    print("✓ Can manage settings")
    print("✓ Can view analytics")
elif user_role == "moderator":
    print("✓ Can view users")
    print("✓ Can ban users")
    print("✗ Cannot delete users")
    print("✗ Cannot manage settings")
elif user_role == "user":
    print("✓ Can view profile")
    print("✗ Cannot view users")
    print("✗ Cannot ban users")
else:
    print("✗ Unknown role")

print()

# ============================================================================
# EXAMPLE 15: Discount Calculation
# ============================================================================
# Real-world: e-commerce discount tiers

print("Example 15: Discount Tiers")
print("-" * 50)

purchase_amount = 150

print(f"Purchase: ${purchase_amount:.2f}")
print()

if purchase_amount >= 200:
    discount_percent = 20
elif purchase_amount >= 100:
    discount_percent = 10
elif purchase_amount >= 50:
    discount_percent = 5
else:
    discount_percent = 0

discount = purchase_amount * (discount_percent / 100)
final_price = purchase_amount - discount

print(f"Discount: {discount_percent}% (${discount:.2f})")
print(f"Final price: ${final_price:.2f}")

print()

# ============================================================================
# EXAMPLE 16: Game State - Boss Fight
# ============================================================================
# Real-world: game logic

print("Example 16: Game Boss Battle Logic")
print("-" * 50)

player_health = 30
boss_health = 50
player_mana = 20

print(f"Player HP: {player_health}, Mana: {player_mana}")
print(f"Boss HP: {boss_health}")
print()

if player_health <= 0:
    print("💀 Player defeated")
elif boss_health <= 0:
    print("✓ Boss defeated - Victory!")
elif player_health < 20:
    print("⚠️  Critical health - use health potion")
elif player_mana < 10 and boss_health > 30:
    print("⚠️  Low mana - switch to physical attack")
else:
    print("⚔️  Engage boss normally")

print()

# ============================================================================
# EXAMPLE 17: Conditional Assignment (Ternary)
# ============================================================================
# Assign value based on condition in one line

print("Example 17: Ternary Operator")
print("-" * 50)

age = 25
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

print()

age = 15
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

print()

# More examples
score = 75
result = "pass" if score >= 70 else "fail"
print(f"Score {score}: {result}")

is_raining = True
action = "stay inside" if is_raining else "go out"
print(f"Raining: {is_raining} → {action}")

print()

# ============================================================================
# EXAMPLE 18: Multiple Nested Conditions
# ============================================================================
# Deeply nested logic

print("Example 18: Deeply Nested Conditions")
print("-" * 50)

is_logged_in = True
is_email_verified = True
is_2fa_enabled = True

if is_logged_in:
    print("✓ Logged in")
    if is_email_verified:
        print("  ✓ Email verified")
        if is_2fa_enabled:
            print("    ✓ 2FA enabled - Full access granted")
        else:
            print("    ⚠️  2FA disabled - Limited access")
    else:
        print("  ✗ Email not verified - Verify email first")
else:
    print("✗ Please log in")

print()

# ============================================================================
# EXAMPLE 19: Guard Clauses (Early Exit)
# ============================================================================
# Exit early if condition fails

print("Example 19: Guard Clauses")
print("-" * 50)

def process_user(username, password):
    print(f"Processing user: {username}")
    
    if not username:
        print("  ✗ Username required")
        return  # Exit early
    
    if not password:
        print("  ✗ Password required")
        return  # Exit early
    
    if len(password) < 8:
        print("  ✗ Password too short")
        return  # Exit early
    
    print("  ✓ User processed successfully")

process_user("alice", "short")
process_user("alice", "verylongpassword")

print()

# ============================================================================
# EXAMPLE 20: String Containment Check
# ============================================================================
# Check if substring exists

print("Example 20: String Containment")
print("-" * 50)

email = "alice@example.com"
domain = "example.com"

if "@" in email:
    print("✓ Valid email format (has @)")
else:
    print("✗ Invalid email format")

if domain in email:
    print(f"✓ Email is from {domain}")
else:
    print(f"✗ Email is not from {domain}")

print()

# ============================================================================
# EXAMPLE 21: Membership in List
# ============================================================================
# Check if value is in a collection

print("Example 21: Membership Testing")
print("-" * 50)

valid_responses = ["yes", "no", "maybe"]
user_input = "yes"

if user_input in valid_responses:
    print(f"✓ '{user_input}' is valid")
else:
    print(f"✗ '{user_input}' is not valid")

print()

user_input = "maybe"
if user_input in valid_responses:
    print(f"✓ '{user_input}' is valid")
else:
    print(f"✗ '{user_input}' is not valid")

print()

# ============================================================================
# EXAMPLE 22: File Permission Check
# ============================================================================
# Real-world: file access simulation

print("Example 22: File Permissions")
print("-" * 50)

user_role = "editor"
file_read = True
file_write = True
file_delete = False

if user_role == "admin":
    can_access = True
elif user_role == "editor":
    can_access = file_read and file_write
elif user_role == "viewer":
    can_access = file_read
else:
    can_access = False

print(f"User: {user_role}")
print(f"Read: {file_read}, Write: {file_write}, Delete: {file_delete}")
print()

if can_access:
    print("✓ Access granted")
else:
    print("✗ Access denied")

print()

# ============================================================================
# EXAMPLE 23: Leap Year Checker
# ============================================================================
# Real-world: complex logic

print("Example 23: Leap Year Calculation")
print("-" * 50)

years = [2000, 2004, 2100, 2020, 1900]

for year in years:
    if year % 400 == 0:
        is_leap = True
    elif year % 100 == 0:
        is_leap = False
    elif year % 4 == 0:
        is_leap = True
    else:
        is_leap = False
    
    status = "leap" if is_leap else "not leap"
    print(f"{year}: {status} year")

print()

# ============================================================================
# EXAMPLE 24: Multiple Decision Paths
# ============================================================================
# Different actions based on multiple conditions

print("Example 24: Order Status Logic")
print("-" * 50)

order_status = "shipped"
is_paid = True
is_delivered = False

if not is_paid:
    print("⚠️  Order not paid - awaiting payment")
elif order_status == "pending":
    print("📋 Order pending - being processed")
elif order_status == "shipped":
    print("📦 Order shipped - in transit")
elif order_status == "delivered":
    print("✓ Order delivered - complete")
else:
    print("❓ Unknown order status")

print()

# ============================================================================
# EXAMPLE 25: Real-World: Age-Based Ticket Pricing
# ============================================================================
# Complex pricing logic

print("Example 25: Ticket Pricing by Age")
print("-" * 50)

ages = [5, 12, 18, 25, 65, 80]

print("Age → Ticket Price → Category")
print("-" * 40)

for age in ages:
    if age < 6:
        price = 0
        category = "Free (under 6)"
    elif age < 12:
        price = 10
        category = "Child"
    elif age < 18:
        price = 12
        category = "Teen"
    elif age < 65:
        price = 15
        category = "Adult"
    else:
        price = 10
        category = "Senior"
    
    print(f"{age:2} years → ${price:2} → {category}")

