#!/usr/bin/env python3
"""
Topic 8: Comparisons - Code Examples for Lectures

This file contains runnable examples for each lecture.
Run this file to see comparison concepts in action.
"""

# ============================================================================
# LECTURE 1: What Are Comparisons? (The Foundation)
# ============================================================================

print("=" * 80)
print("LECTURE 1: What Are Comparisons? (The Foundation)")
print("=" * 80)

# Example 1.1: Basic comparisons return True or False
print("\nExample 1.1: Comparisons Return Boolean Values")
print("-" * 80)

result1 = 5 > 3
print(f"5 > 3 → {result1}")
print(f"Type: {type(result1)}")

result2 = "apple" == "banana"
print(f"'apple' == 'banana' → {result2}")
print(f"Type: {type(result2)}")

# Example 1.2: Comparisons in decision-making
print("\nExample 1.2: Comparisons Enable Decision-Making")
print("-" * 80)

age = 16
if age >= 18:
    print(f"You (age {age}) can vote")
else:
    print(f"You (age {age}) cannot vote yet")

# Example 1.3: Structure of a comparison
print("\nExample 1.3: The Structure of a Comparison")
print("-" * 80)
print("""
Comparison: age >= 18
            │    ││ │
            │    ││ └─ Right value (reference: 18)
            │    │└── Operator (greater than or equal)
            │    └─── Left value (the variable being tested)
            └─────── Comparison = Question + Answer
""")

score = 95
left_value = score
operator_name = ">="
right_value = 90
result = left_value >= right_value
print(f"\nComparison: {score} {operator_name} {right_value}")
print(f"Answer: {result} (Is {score} ≥ {right_value}? {result})")

# ============================================================================
# LECTURE 2: Comparison Operators (The Tools)
# ============================================================================

print("\n" + "=" * 80)
print("LECTURE 2: Comparison Operators (The Tools)")
print("=" * 80)

# Example 2.1: Equality operators
print("\nExample 2.1: Equality Operators (== and !=)")
print("-" * 80)

x = 5
y = 5
z = 3

print(f"x = {x}, y = {y}, z = {z}")
print(f"\nx == y: {x == y} (Are they equal?)")
print(f"x == z: {x == z} (Are they equal?)")
print(f"x != z: {x != z} (Are they different?)")
print(f"x != y: {x != y} (Are they different?)")

print("\n⚠️  IMPORTANT: == is comparison, = is assignment")
print("x = 5      assigns 5 to x")
print("x == 5     compares: is x equal to 5?")

# Example 2.2: Ordering operators - strict
print("\nExample 2.2: Ordering Operators - Strict (> and <)")
print("-" * 80)

a = 10
b = 5
c = 10

print(f"a = {a}, b = {b}, c = {c}")
print(f"\na > b: {a > b} (Is 10 > 5? Yes)")
print(f"b > a: {b > a} (Is 5 > 10? No)")
print(f"a > c: {a > c} (Is 10 > 10? No - they're equal, not greater)")
print(f"\nNote: > does NOT include equality!")

# Example 2.3: Ordering operators - inclusive
print("\nExample 2.3: Ordering Operators - Inclusive (>= and <=)")
print("-" * 80)

print(f"\nSame values: a = {a}, c = {c}")
print(f"a > c: {a > c} (Is 10 > 10? No)")
print(f"a >= c: {a >= c} (Is 10 ≥ 10? Yes - INCLUDES equality)")
print(f"\nNote: >= INCLUDES equality!")

# Example 2.4: Real-world: age eligibility
print("\nExample 2.4: Real-World Example - Age Eligibility")
print("-" * 80)

ages = [16, 18, 21, 25]
for age in ages:
    can_vote = age >= 18
    can_drink = age >= 21
    print(f"Age {age}: Can vote? {can_vote:5} | Can drink? {can_drink:5}")

# ============================================================================
# LECTURE 3: Equality vs Identity (The Subtle Difference)
# ============================================================================

print("\n" + "=" * 80)
print("LECTURE 3: Equality vs Identity (== vs is)")
print("=" * 80)

# Example 3.1: Lists with same content vs same object
print("\nExample 3.1: Two Lists with Same Content (But Different Objects)")
print("-" * 80)

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"\nlist1 == list2: {list1 == list2} (Same content?)")
print(f"list1 is list2: {list1 is list2} (Same object?)")
print("\nThey have the same content but are different objects in memory.")

# Example 3.2: Pointing to the same object
print("\nExample 3.2: Two Variables Pointing to the Same Object")
print("-" * 80)

list1 = [1, 2, 3]
list2 = list1  # list2 now points to the SAME list

print(f"list1 = {list1}")
print(f"list2 = list1")
print(f"\nlist1 == list2: {list1 == list2} (Same content?)")
print(f"list1 is list2: {list1 is list2} (Same object?)")
print("\nNow they're the same object. Changing one affects the other:")

list1.append(4)
print(f"After list1.append(4):")
print(f"  list1 = {list1}")
print(f"  list2 = {list2}  ← Changed too!")

# Example 3.3: When to use each
print("\nExample 3.3: When to Use == vs is")
print("-" * 80)

# Use == for comparing values (99% of the time)
password_entered = "secret123"
password_stored = "secret123"
if password_entered == password_stored:
    print("✓ Password matches (using ==)")

# Use is for None (the main use case)
value = None
if value is None:
    print("✓ Value is None (using is None)")

# Example 3.4: The is None pattern
print("\nExample 3.4: Checking for None - The Standard Pattern")
print("-" * 80)

values = [5, None, "hello", None, 0]
for value in values:
    if value is None:
        print(f"Value is None")
    else:
        print(f"Value is {value}")

# ============================================================================
# LECTURE 4: Comparison Chains (Elegant Range Testing)
# ============================================================================

print("\n" + "=" * 80)
print("LECTURE 4: Comparison Chains (Elegant Range Testing)")
print("=" * 80)

# Example 4.1: Traditional range checking
print("\nExample 4.1: Traditional Range Check (Verbose)")
print("-" * 80)

x = 5
if x > 1 and x < 10:
    print(f"{x} is between 1 and 10")
else:
    print(f"{x} is NOT between 1 and 10")
print("This works but repeats x twice.")

# Example 4.2: Comparison chains
print("\nExample 4.2: Comparison Chains (Pythonic)")
print("-" * 80)

x = 5
if 1 < x < 10:
    print(f"{x} is between 1 and 10")
else:
    print(f"{x} is NOT between 1 and 10")
print("This reads naturally and repeats x only once.")

# Example 4.3: How chains work
print("\nExample 4.3: How Comparison Chains Work")
print("-" * 80)

test_values = [0, 5, 10, 15]
for x in test_values:
    result = 1 < x < 10
    print(f"1 < {x} < 10 → {result}")
    if not result:
        # Show why
        if not (1 < x):
            print(f"    (because 1 < {x} is False)")
        elif not (x < 10):
            print(f"    (because {x} < 10 is False)")

# Example 4.4: Grade boundaries with chains
print("\nExample 4.4: Grade Boundaries with Chains")
print("-" * 80)

def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

scores = [45, 65, 75, 85, 95, 105]
for score in scores:
    grade = get_grade(score)
    print(f"Score {score:3} → Grade {grade}")

# ============================================================================
# LECTURE 5: Type Matters in Comparisons
# ============================================================================

print("\n" + "=" * 80)
print("LECTURE 5: Type Matters in Comparisons")
print("=" * 80)

# Example 5.1: Comparing numbers (int and float)
print("\nExample 5.1: Comparing Numbers (int and float)")
print("-" * 80)

a = 5      # int
b = 5.0    # float
c = 5.5    # float

print(f"a = {a} (type: {type(a).__name__})")
print(f"b = {b} (type: {type(b).__name__})")
print(f"c = {c} (type: {type(c).__name__})")
print(f"\na == b: {a == b} (Python compares values, not types)")
print(f"type(a) == type(b): {type(a) == type(b)} (But types are different)")
print(f"\na < c: {a < c} (Numeric comparison works)")

# Example 5.2: Comparing strings
print("\nExample 5.2: Comparing Strings (Alphabetically)")
print("-" * 80)

s1 = "apple"
s2 = "banana"
s3 = "apple"

print(f"s1 = '{s1}'")
print(f"s2 = '{s2}'")
print(f"s3 = '{s3}'")
print(f"\ns1 == s3: {s1 == s3} (Exact match)")
print(f"s1 == s2: {s1 == s2} (Different strings)")
print(f"s1 < s2: {s1 < s2} (Alphabetically: 'a' comes before 'b')")

# Example 5.3: Case sensitivity
print("\nExample 5.3: Case Sensitivity in String Comparison")
print("-" * 80)

s1 = "Hello"
s2 = "hello"

print(f"s1 = '{s1}'")
print(f"s2 = '{s2}'")
print(f"\ns1 == s2: {s1 == s2} (Case matters)")
print(f"s1.lower() == s2.lower(): {s1.lower() == s2.lower()} (Case-insensitive)")

# Example 5.4: Type mismatch errors
print("\nExample 5.4: Type Mismatch in Comparisons")
print("-" * 80)

print("5 == '5':", 5 == "5", "(Different types, returns False)")
print("5 != '5':", 5 != "5", "(Different types, returns True)")

print("\nAttempting 5 < 'hello' causes TypeError...")
try:
    result = 5 < "hello"
    print(f"Result: {result}")
except TypeError as e:
    print(f"✗ Error: {e}")
    print("  Solution: Convert to same type first")
    result = str(5) < "hello"
    print(f"  str(5) < 'hello': {result}")

# ============================================================================
# LECTURE 6: String Comparisons Deep Dive
# ============================================================================

print("\n" + "=" * 80)
print("LECTURE 6: String Comparisons Deep Dive")
print("=" * 80)

# Example 6.1: Character-by-character comparison
print("\nExample 6.1: Character-by-Character Comparison")
print("-" * 80)

s1 = "apple"
s2 = "apricot"

print(f"Comparing '{s1}' and '{s2}':")
print(f"Position 0: '{s1[0]}' vs '{s2[0]}' → Equal, continue")
print(f"Position 1: '{s1[1]}' vs '{s2[1]}' → Equal, continue")
print(f"Position 2: '{s1[2]}' vs '{s2[2]}' → '{s1[2]}' < '{s2[2]}', stop")
print(f"\nResult: '{s1}' < '{s2}' → {s1 < s2}")

# Example 6.2: Prefix comparison
print("\nExample 6.2: Prefix Comparison")
print("-" * 80)

s1 = "cat"
s2 = "catalog"

print(f"Comparing '{s1}' and '{s2}':")
print(f"'{s1}' is a prefix of '{s2}'")
print(f"The shorter string comes first.")
print(f"'{s1}' < '{s2}' → {s1 < s2}")

# Example 6.3: Case sensitivity in ordering
print("\nExample 6.3: Case Sensitivity (ASCII Order)")
print("-" * 80)

names = ["alice", "Bob", "charlie", "Diana"]
print(f"Original: {names}")

sorted_names = sorted(names)
print(f"Sorted (case-sensitive): {sorted_names}")
print("Note: Uppercase letters come before lowercase in ASCII")

sorted_case_insensitive = sorted(names, key=str.lower)
print(f"Sorted (case-insensitive): {sorted_case_insensitive}")

# ============================================================================
# LECTURE 7: Membership Testing (in and not in)
# ============================================================================

print("\n" + "=" * 80)
print("LECTURE 7: Membership Testing (in and not in)")
print("=" * 80)

# Example 7.1: Basic membership testing
print("\nExample 7.1: Basic Membership Testing")
print("-" * 80)

valid_colors = ["red", "green", "blue"]
test_colors = ["red", "yellow", "blue"]

for color in test_colors:
    if color in valid_colors:
        print(f"✓ {color} is valid")
    else:
        print(f"✗ {color} is not valid")

# Example 7.2: Substring searching
print("\nExample 7.2: Substring Searching")
print("-" * 80)

text = "The quick brown fox jumps over the lazy dog"
substrings = ["quick", "yellow", "fox", "xyz"]

for substring in substrings:
    if substring in text:
        print(f"✓ '{substring}' found in text")
    else:
        print(f"✗ '{substring}' not found in text")

# Example 7.3: Using 'not in'
print("\nExample 7.3: Using 'not in'")
print("-" * 80)

forbidden_usernames = ["admin", "root", "system"]
test_usernames = ["alice", "admin", "bob", "root"]

for username in test_usernames:
    if username not in forbidden_usernames:
        print(f"✓ '{username}' is available")
    else:
        print(f"✗ '{username}' is forbidden")

# Example 7.4: Performance comparison
print("\nExample 7.4: Performance - Lists vs Sets")
print("-" * 80)

import time

# Create test data
size = 100000
test_list = list(range(size))
test_set = set(range(size))
search_value = 99999

# Time list search
start = time.time()
for _ in range(1000):
    _ = search_value in test_list
list_time = time.time() - start

# Time set search
start = time.time()
for _ in range(1000):
    _ = search_value in test_set
set_time = time.time() - start

print(f"Searching for {search_value} in {size} items (1000 times):")
print(f"  List time: {list_time:.4f} seconds")
print(f"  Set time:  {set_time:.4f} seconds")
print(f"  Sets are {list_time/set_time:.0f}x faster!")

# ============================================================================
# LECTURE 8: Common Mistakes and How to Avoid Them
# ============================================================================

print("\n" + "=" * 80)
print("LECTURE 8: Common Mistakes and How to Avoid Them")
print("=" * 80)

# Example 8.1: = vs ==
print("\nExample 8.1: Assignment (=) vs Comparison (==)")
print("-" * 80)

x = 5
print(f"x = 5      ← Assignment (stores 5 in x)")
print(f"x == 5     ← Comparison (asks: is x equal to 5?)")
print(f"Result: {x == 5}")

print("\n⚠️  This causes an error:")
print("if x = 5:   ← Tries to assign inside if condition")

# Example 8.2: Forgetting inclusivity
print("\nExample 8.2: Forgetting Inclusivity in Range Checks")
print("-" * 80)

score = 80
PASSING_SCORE = 80

print(f"score = {score}")
print(f"PASSING_SCORE = {PASSING_SCORE}")

if score > PASSING_SCORE:
    print(f"✓ Passing (using >)")
else:
    print(f"✗ Not passing (using >)")
print("  Wait - score equals PASSING_SCORE but > doesn't count equality!")

if score >= PASSING_SCORE:
    print(f"✓ Passing (using >=)")
else:
    print(f"✗ Not passing (using >=)")
print("  Correct - >= includes the boundary!")

# Example 8.3: Comparing incompatible types
print("\nExample 8.3: Comparing Incompatible Types")
print("-" * 80)

value = 5
name = "Alice"

print(f"value = {value} (int)")
print(f"name = '{name}' (str)")
print(f"\nvalue == name: {value == name} (Equality works, returns False)")

print("\nAttempting value < name:")
try:
    result = value < name
except TypeError as e:
    print(f"✗ Error: {e}")
    print("Solution: Convert to same type")
    result = str(value) < name
    print(f"str({value}) < '{name}': {result}")

# Example 8.4: Case-sensitive string comparison
print("\nExample 8.4: Case-Sensitive String Comparison")
print("-" * 80)

password1 = "MyPassword123"
password2 = "mypassword123"

if password1 == password2:
    print("✓ Passwords match")
else:
    print("✗ Passwords don't match (case differs)")

if password1.lower() == password2.lower():
    print("✓ Passwords match (ignoring case)")
else:
    print("✗ Passwords don't match")

# ============================================================================
# LECTURE 9: Putting It Together - Decision Making
# ============================================================================

print("\n" + "=" * 80)
print("LECTURE 9: Putting It Together - Decision Making")
print("=" * 80)

# Example 9.1: Single comparison
print("\nExample 9.1: Single Comparison Decision")
print("-" * 80)

age = 16
if age >= 18:
    print("You can vote")
else:
    print("You're too young to vote")

# Example 9.2: Multiple comparisons with AND
print("\nExample 9.2: Multiple Conditions with AND")
print("-" * 80)

age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")

# Example 9.3: Multiple comparisons with OR
print("\nExample 9.3: Multiple Conditions with OR")
print("-" * 80)

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print(f"{day} - It's the weekend!")
else:
    print(f"{day} - It's a weekday")

# Example 9.4: Complex decision-making
print("\nExample 9.4: Complex Decision-Making")
print("-" * 80)

def validate_password(password):
    """Validate password against multiple criteria."""
    is_long_enough = len(password) >= 8
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if is_long_enough and has_uppercase and has_digit:
        return "Strong"
    elif is_long_enough and (has_uppercase or has_digit):
        return "Medium"
    elif is_long_enough:
        return "Weak"
    else:
        return "Too Short"

passwords = ["test", "Test", "Test123", "Test123!"]
for pwd in passwords:
    strength = validate_password(pwd)
    print(f"'{pwd}' → {strength}")

# ============================================================================
# LECTURE 10: Best Practices
# ============================================================================

print("\n" + "=" * 80)
print("LECTURE 10: Best Practices")
print("=" * 80)

# Example 10.1: Using named constants
print("\nExample 10.1: Using Named Constants")
print("-" * 80)

# Bad: magic numbers
age = 20
if age >= 18:
    print("Can vote")

# Good: named constants
VOTING_AGE = 18
LEGAL_DRINKING_AGE = 21

if age >= VOTING_AGE:
    print("Can vote")

if age >= LEGAL_DRINKING_AGE:
    print("Can drink")

# Example 10.2: Using comparison chains for ranges
print("\nExample 10.2: Using Comparison Chains for Ranges")
print("-" * 80)

temperature = 72

# Bad
if temperature > 60 and temperature < 80:
    print("Comfortable")

# Good
if 60 < temperature < 80:
    print("Comfortable")

# Example 10.3: Using 'in' for collection membership
print("\nExample 10.3: Using 'in' for Collection Membership")
print("-" * 80)

status = "active"

# Bad
if status == "active" or status == "pending" or status == "waiting":
    print("Can proceed")

# Good
if status in ["active", "pending", "waiting"]:
    print("Can proceed")

# Example 10.4: Using isinstance() for type checking
print("\nExample 10.4: Using isinstance() for Type Checking")
print("-" * 80)

values = [5, 5.5, "hello", True]

for value in values:
    # Good practice
    if isinstance(value, int) and not isinstance(value, bool):
        print(f"{value}: integer")
    elif isinstance(value, float):
        print(f"{value}: float")
    elif isinstance(value, str):
        print(f"{value}: string")
    elif isinstance(value, bool):
        print(f"{value}: boolean")

# Example 10.5: Using 'is None' for None checking
print("\nExample 10.5: Using 'is None' for None Checking")
print("-" * 80)

values = [5, None, "hello", None, 0]

for value in values:
    # Good practice
    if value is None:
        print(f"Value is None")
    elif value == 0:
        print(f"Value is zero")
    else:
        print(f"Value is {value}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("SUMMARY: Key Takeaways")
print("=" * 80)
print("""
1. Comparisons ask yes/no questions about values
2. They return boolean: True or False
3. Different operators test different relationships:
   - ==, != for equality
   - <, >, <=, >= for ordering
   - is, is not for identity
   - in, not in for membership

4. Type matters - comparisons work differently with different types

5. Best practices:
   - Use == for values, is for None
   - Use comparison chains for ranges
   - Use 'in' for collection membership
   - Use named constants for boundaries
   - Use isinstance() for type checking

6. Comparisons are the foundation of decision-making
   Master them, and your programs gain intelligence
""")

print("=" * 80)
print("END OF CODE EXAMPLES")
print("=" * 80)