# Topic 10: Logical Operators - Combining and Reasoning About Conditions

## Goal

**Learn to combine multiple conditions elegantly using logical operators. Master and, or, and not operators. Understand operator precedence, De Morgan's laws, short-circuit evaluation, and how to write complex conditions that are both powerful and readable.**

---

## Why This Matters - The Real Problem

Real-world decisions rarely depend on a single condition:

- **Access control:** Is user logged in AND is user admin AND is 2FA verified?
- **Alerts:** Is temperature high OR is pressure high OR is smoke detected?
- **Game logic:** Is player alive AND has ammo AND is enemy visible?
- **Shopping:** Is item in stock AND is price under budget AND is seller trustworthy?
- **Data validation:** Is field not empty AND is length valid AND is format correct?

Without logical operators, code becomes bloated and hard to read:

**Without logical operators (ugly):**
```python
if is_adult:
    if has_license:
        if has_insurance:
            if not has_accidents:
                print("Can drive")
```

**With logical operators (clean):**
```python
if is_adult and has_license and has_insurance and not has_accidents:
    print("Can drive")
```

**Logical operators let you write powerful, readable conditions.**

---

## Mental Model 1: What Are Logical Operators? (The Tool Model)

**Logical operators** combine boolean values to create new boolean results.

Three main operators:
- **and**: Both must be True
- **or**: At least one must be True
- **not**: Reverses the boolean

```python
True and True      # True
True and False     # False
True or False      # True
not True           # False
```

**Why they matter:**

Without them, you can only test one condition at a time. With them, you can express complex real-world logic concisely.

```python
# Single condition (limited)
if age >= 18:
    can_vote = True

# Multiple conditions (realistic)
if age >= 18 and is_citizen and is_registered:
    can_vote = True
```

---

## Mental Model 2: The 'and' Operator (Both Must Be True)

**and** requires BOTH conditions to be True.

```python
True and True      # True
True and False     # False
False and True     # False
False and False    # False
```

Truth table:
```
A     B     A and B
---   ---   -------
True  True  True
True  False False
False True  False
False False False
```

**In conditionals:**

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
    # Requires BOTH to be true
```

**Real-world uses:**

```python
# Login validation
if username_correct and password_correct:
    print("Access granted")

# Game logic
if player_alive and has_ammo and enemy_visible:
    print("Attack")

# Data quality
if not empty and valid_format and within_range:
    print("Data accepted")
```

**Key insight:** If the first condition is False, the second is never checked.

```python
if has_account and is_verified:
    # If has_account is False,
    # is_verified is never evaluated (short-circuit)
    pass
```

---

## Mental Model 3: The 'or' Operator (At Least One Must Be True)

**or** requires AT LEAST ONE condition to be True.

```python
True or True      # True
True or False     # True
False or True     # True
False or False    # False
```

Truth table:
```
A     B     A or B
---   ---   ------
True  True  True
True  False True
False True  True
False False False
```

**In conditionals:**

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today")
    # Requires AT LEAST ONE to be true
```

**Real-world uses:**

```python
# Access permission
if is_admin or is_owner or is_moderator:
    print("Can delete user")

# Alerts
if temp_high or pressure_high or smoke_detected:
    print("Emergency alarm")

# Acceptable responses
if response == "yes" or response == "y" or response == "Y":
    print("Accepted")
```

**Key insight:** If the first condition is True, the second is never checked.

```python
if is_authorized or requires_approval:
    # If is_authorized is True,
    # requires_approval is never evaluated (short-circuit)
    pass
```

---

## Mental Model 4: The 'not' Operator (Reversal)

**not** reverses a boolean value.

```python
not True       # False
not False      # True
```

Truth table:
```
A     not A
---   ------
True  False
False True
```

**In conditionals:**

```python
is_raining = False

if not is_raining:
    print("Go outside")
    # Opposite of is_raining
```

**Real-world uses:**

```python
# Access denial
if not is_verified:
    print("Please verify email")

# Safety check
if not file_exists:
    print("File not found")

# Inversion logic
if not has_errors and not has_warnings:
    print("All clear")
```

**Alternative forms:**

```python
# These are equivalent
if not is_verified:
    process()

if is_verified == False:
    process()

if is_verified is False:
    process()
```

The first is clearest.

---

## Mental Model 5: Operator Precedence (Order Matters)

Logical operators have a specific precedence order:

```
Highest:  not
Middle:   and
Lowest:   or
```

**Example:**

```python
True or False and False

# Method 1: Left to right (wrong)
# (True or False) and False = True and False = False

# Method 2: With precedence (correct)
# True or (False and False) = True or False = True

# Python uses Method 2: Result is True
```

**Why it matters:**

```python
x = 5
is_valid = x > 0 and x < 10 or x == 20

# With precedence:
# (x > 0 and x < 10) or (x == 20)
# If x=5: (True and True) or False = True

# Without precedence (if read left-to-right):
# Would be different
```

**Use parentheses for clarity:**

```python
# Confusing without parentheses
if condition1 or condition2 and condition3:
    pass

# Clear with parentheses
if condition1 or (condition2 and condition3):
    pass

# Or different grouping
if (condition1 or condition2) and condition3:
    pass
```

---

## Mental Model 6: De Morgan's Laws (Simplification)

De Morgan's Laws let you simplify complex conditions.

**Law 1:** `not (A and B)` = `(not A) or (not B)`

```python
# These are equivalent:
if not (age >= 18 and has_license):
    print("Cannot drive")

if (age < 18) or (not has_license):
    print("Cannot drive")
```

**Law 2:** `not (A or B)` = `(not A) and (not B)`

```python
# These are equivalent:
if not (is_admin or is_moderator):
    print("Access denied")

if (not is_admin) and (not is_moderator):
    print("Access denied")
```

**Why use them:**

Sometimes inverting conditions makes code clearer:

```python
# Hard to read
if not (file_exists and file_readable):
    print("Cannot process")

# Clearer
if not file_exists or not file_readable:
    print("Cannot process")
```

---

## Mental Model 7: Short-Circuit Evaluation (Optimization)

Python stops evaluating as soon as the result is certain.

**with 'and':**

```python
condition1 and condition2

# If condition1 is False, condition2 is never checked
# Python knows the result is False regardless of condition2
```

**with 'or':**

```python
condition1 or condition2

# If condition1 is True, condition2 is never checked
# Python knows the result is True regardless of condition2
```

**Real-world impact:**

```python
def is_admin():
    print("Checking admin status (expensive)")
    return True

user = "alice"

# is_admin() is NOT called
if user == "bob" and is_admin():
    print("Bob is admin")
    # Output: Only "Checking admin..." does NOT print

# is_admin() IS called
if user == "alice" and is_admin():
    print("Alice is admin")
    # Output: "Checking admin status (expensive)" then "Alice is admin"
```

**Use for efficiency:**

```python
# Check cheap condition first, expensive second
if file_exists() and process_file():  # file_exists is cheap
    print("Done")

# Check likely False condition first
if unlikely_condition or expensive_check():
    pass
```

---

## Mental Model 8: Complex Boolean Expressions (Multi-Operator)

Combining multiple logical operators creates complex expressions.

```python
# All must be true
if condition1 and condition2 and condition3:
    pass

# At least one must be true
if condition1 or condition2 or condition3:
    pass

# Mixed: complex logic
if (condition1 or condition2) and (not condition3):
    pass
```

**Real-world example:**

```python
# Valid user?
is_age_ok = age >= 18
is_verified = email_verified
is_not_banned = not account_banned

if is_age_ok and is_verified and is_not_banned:
    print("User is valid")
```

**Strategy for readability:**

```python
# Hard to read in one line
if age >= 18 and email_verified and not account_banned and has_agreed_terms and not has_active_disputes:
    grant_access()

# Break into named conditions
is_age_ok = age >= 18
is_verified = email_verified
is_active = not account_banned
is_compliant = has_agreed_terms
is_clear = not has_active_disputes

if is_age_ok and is_verified and is_active and is_compliant and is_clear:
    grant_access()
```

---

## Mental Model 9: Common Logical Patterns (Idioms)

**Pattern 1: Guard Clause**

```python
# Check failure condition first
if not user_logged_in:
    print("Please login")
    return

# Rest of code assumes user is logged in
process_user()
```

**Pattern 2: Positive Logic**

```python
# Easier to understand
if user_is_admin and file_is_editable:
    allow_edit()

# Harder to understand
if not (not user_is_admin or not file_is_editable):
    allow_edit()
```

**Pattern 3: Short-Circuit for Null Checking**

```python
# Check if exists before accessing
if user is not None and user.is_active:
    process(user)

# If user is None, is_active is never checked
```

**Pattern 4: Multiple Acceptable Values**

```python
# Verbose
if command == "save" or command == "write" or command == "update":
    perform_save()

# Better
if command in ["save", "write", "update"]:
    perform_save()
```

**Pattern 5: Range Checking**

```python
# With logical operators
if score >= 80 and score < 90:
    print("B grade")

# Clearer with chained comparison
if 80 <= score < 90:
    print("B grade")
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Why Do 'and' and 'or' Have Different Precedence?"

**The question:** Why doesn't Python evaluate left-to-right?

**The answer:** Mathematical convention for Boolean algebra sets precedence:
1. not (negation)
2. and (conjunction)
3. or (disjunction)

This matches math and logic: `not` is strongest, `or` is weakest.

```python
A or B and C
# Means: A or (B and C)
# Not: (A or B) and C
```

### Confusion 2: "When Should I Use 'and' vs Multiple If Statements?"

**The question:** When is `and` better than nested if?

**The answer:** Use `and` for conditions that must ALL be true.

```python
# Use 'and'
if age >= 18 and has_license:  # Both required simultaneously
    drive()

# Use nested if
if application_submitted:      # Check first thing
    if application_approved:   # Then check approval
        notify_user()          # Each level has different meaning
```

### Confusion 3: "Why Doesn't 'not' Work the Way I Expect?"

**The question:** Why does `not variable == value` behave strangely?

**The answer:** Precedence! `not` has higher precedence than `==`.

```python
not x == 5      # Means: not (x == 5)
(not x) == 5    # Different! Means: reverse boolean of x, then compare

# Safer to use:
x != 5          # Not equal to
not (x == 5)    # Clear parentheses
```

### Confusion 4: "When Does Short-Circuit Matter?"

**The question:** Can short-circuit behavior cause bugs?

**The answer:** Yes, if second condition has side effects.

```python
# Dangerous
if index < len(array) and array[index] == target:
    # SHORT-CIRCUITS: index < len(array) is checked first
    # Prevents IndexError
    pass

# Would crash without short-circuit
if array[index] == target and index < len(array):
    # WITHOUT short-circuit, array[index] is accessed first
    # Could cause IndexError if index >= len(array)
    pass
```

### Confusion 5: "How Do I Debug Complex Boolean Expressions?"

**The question:** My condition is wrong but I can't find the bug.

**The answer:** Break it into parts:

```python
# Hard to debug
if user.is_verified and (user.has_permission or is_admin) and not user.is_banned:
    pass

# Easy to debug
is_verified = user.is_verified
has_access = user.has_permission or is_admin
is_not_banned = not user.is_banned

print(f"Verified: {is_verified}")
print(f"Has access: {has_access}")
print(f"Not banned: {is_not_banned}")

if is_verified and has_access and is_not_banned:
    pass
```

---

## How Logical Operators Work Internally (Execution Model)

**For 'and':**

```
Step 1: Evaluate first condition
Step 2: If False, return False immediately (short-circuit)
Step 3: If True, evaluate second condition
Step 4: Return result of second condition
```

**For 'or':**

```
Step 1: Evaluate first condition
Step 2: If True, return True immediately (short-circuit)
Step 3: If False, evaluate second condition
Step 4: Return result of second condition
```

**For 'not':**

```
Step 1: Evaluate condition
Step 2: Reverse the boolean value
Step 3: Return reversed value
```

---

## Real-World Logical Operators (Practical Applications)

**Permission system:**

```python
can_edit = (is_owner or is_admin or has_edit_permission) and not is_archived
can_delete = is_admin and not is_protected
can_view = not is_private or is_owner or is_shared_with_user
```

**Data validation:**

```python
is_valid_email = (has_at_symbol and has_domain) and not has_spaces
is_valid_password = (len(password) >= 8) and (has_letters) and (has_numbers)
is_valid_date = (1 <= month <= 12) and (1 <= day <= 31) and (year >= 1900)
```

**Game logic:**

```python
can_attack = player_alive and has_target and in_range and not is_stunned
can_flee = player_alive and enemy_distance > safe_distance and not is_trapped
is_game_over = player_dead or reached_final_boss
```

---

## Summary - The Big Picture

**What you learned:**
1. and operator (both must be true)
2. or operator (at least one must be true)
3. not operator (reversal)
4. Operator precedence (not > and > or)
5. De Morgan's Laws
6. Short-circuit evaluation
7. Complex boolean expressions
8. Common patterns
9. Debugging strategies

**Why this matters:**
- Logical operators make complex conditions readable
- They enable expressing real-world constraints
- Short-circuit evaluation improves efficiency
- Proper use prevents subtle bugs
- Clean code is maintainable code

**What's next:**
Now you can write elegant conditions.

Topic 11 teaches **While Loops** - repeating actions until a condition is false.

---

## What You Should Be Able To Do Now

✅ Use and, or, not correctly
✅ Understand operator precedence
✅ Apply De Morgan's Laws
✅ Leverage short-circuit evaluation
✅ Write complex boolean expressions
✅ Choose between logical operators and nested ifs
✅ Debug boolean logic
✅ Name conditions for clarity
✅ Recognize common patterns
✅ Write readable, maintainable conditions

