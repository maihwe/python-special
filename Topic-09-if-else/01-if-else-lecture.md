# Topic 9: If/Else - Conditional Execution and Decision Making

## Goal

**Learn to make decisions in programs. Understand if/else statements, multiple branches with elif, nested conditions, and how to control program flow based on conditions. Master the foundation of all interactive programs.**

---

## Why This Matters - The Real Problem

Every real program makes decisions:

- **Logins:** If password correct, login; else show error
- **Games:** If health = 0, game over; else continue
- **Shopping:** If item in stock, add to cart; else show unavailable
- **Banking:** If balance sufficient, allow withdrawal; else deny
- **Alerts:** If temperature high, trigger alarm; else continue
- **Grading:** If score >= 90, assign A; elif >= 80, assign B; etc.

Without if/else, programs can't respond intelligently.

If/else is **the structure that makes programs interactive**.

Without it, your program runs the same sequence every time. With it, your program adapts to circumstances.

---

## Mental Model 1: What Is an If Statement? (The Decision Model)

An **if statement** is a way to make decisions in code.

It says: "If this condition is true, do this. Otherwise, skip it."

```python
if condition:
    # Execute this if condition is True
    # This code only runs if the condition is true
```

**Visual representation:**

```
    Start
      ↓
  Is condition true?
    /         \
  Yes         No
   ↓           ↓
Execute      Skip
  code       code
   ↓           ↓
    End
```

**Real example:**

```python
age = 18

if age >= 18:
    print("You are an adult")
    # This prints because age >= 18 is True
```

**Another example:**

```python
age = 15

if age >= 18:
    print("You are an adult")
    # This does NOT print because age >= 18 is False
```

---

## Mental Model 2: If/Else - Two Branches (Binary Decision)

An **if/else statement** provides two paths:

"If condition is true, do this. Otherwise, do that."

```python
if condition:
    # Execute if condition is True
else:
    # Execute if condition is False
```

**Visual representation:**

```
      Start
        ↓
    Is condition true?
      /         \
    Yes         No
     ↓           ↓
Execute       Execute
if code       else code
     ↓           ↓
      End
```

**Real example:**

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# Output: You are not an adult
```

**Another example:**

```python
password = "secret123"
user_input = "secret123"

if user_input == password:
    print("Access granted")
else:
    print("Access denied")

# Output: Access granted
```

**Critically important:** Exactly ONE branch executes, never both.

---

## Mental Model 3: Elif - Multiple Branches (Multi-way Decision)

An **elif** (else if) lets you test multiple conditions.

```python
if condition1:
    # Execute if condition1 is True
elif condition2:
    # Execute if condition1 is False and condition2 is True
elif condition3:
    # Execute if condition1 and condition2 are False, condition3 is True
else:
    # Execute if all conditions are False
```

**Visual representation:**

```
        Start
          ↓
    condition1 true?
      /         \
    Yes         No
     ↓           ↓
Execute       condition2 true?
code1           /        \
     ↓        Yes         No
     ↓         ↓           ↓
     ↓      Execute      condition3?
     ↓      code2           ...
     ↓         ↓
      End
```

**Real example - Grade assignment:**

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Output: Grade: B
```

**Real example - Authentication:**

```python
user_role = "moderator"

if user_role == "admin":
    print("Full access")
elif user_role == "moderator":
    print("Limited access")
elif user_role == "user":
    print("View only")
else:
    print("Access denied")

# Output: Limited access
```

**Critical insight:** Only the FIRST true condition executes. Once one elif matches, the rest are skipped.

```python
score = 95

if score >= 90:
    print("Grade: A")
elif score >= 80:  # This is NOT checked because score >= 90 was True
    print("Grade: B")

# Output: Grade: A only
```

---

## Mental Model 4: Nested If Statements (Conditions Within Conditions)

You can put if statements inside other if statements.

```python
if condition1:
    if condition2:
        # Execute if BOTH condition1 AND condition2 are True
        pass
    else:
        # Execute if condition1 is True but condition2 is False
        pass
else:
    # Execute if condition1 is False
    pass
```

**Real example - Access control:**

```python
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Admin panel access")
    else:
        print("User dashboard access")
else:
    print("Please log in")

# Output: User dashboard access
```

**Real example - Age and status verification:**

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can rent a car")
    else:
        print("You need a license first")
else:
    print("You must be 18 to rent a car")

# Output: You can rent a car
```

**When to use nested vs elif:**

Nested: When you need to check one thing ONLY IF another is true.
```python
if age >= 18:        # First check if adult
    if has_license:  # Only then check license
        print("Can rent")
```

Elif: When checking alternative conditions.
```python
if score >= 90:      # Check this
    grade = "A"
elif score >= 80:    # Or check this
    grade = "B"
```

---

## Mental Model 5: Logical Operators in Conditions (and, or, not)

Combine multiple conditions with logical operators.

**and:** Both conditions must be True.

```python
if age >= 18 and has_license:
    print("Can drive")
```

Only executes if BOTH are true.

**or:** At least one condition must be True.

```python
if is_weekend or is_holiday:
    print("No work today")
```

Executes if EITHER is true (or both).

**not:** Reverses the boolean value.

```python
if not is_raining:
    print("Go outside")
```

Executes if is_raining is False.

**Real example - Login with multiple conditions:**

```python
username = "alice"
password = "secret"
is_2fa_verified = True

if username == "alice" and password == "secret" and is_2fa_verified:
    print("Login successful")
else:
    print("Access denied")

# Output: Login successful
```

**Real example - Notification logic:**

```python
has_new_messages = False
has_new_notifications = True
is_phone_silent = False

if (has_new_messages or has_new_notifications) and not is_phone_silent:
    print("Alert the user")
else:
    print("No alert")

# Output: Alert the user
```

---

## Mental Model 6: Execution Flow and Indentation (The Structure)

Python uses **indentation** (spacing) to show which code belongs to which block.

```python
if age >= 18:
    print("You are an adult")  # Indented 4 spaces
    print("You can vote")       # Also part of if block
print("Program continues")      # Not indented, runs regardless

# All three prints will execute (last one always)
```

**Visual structure:**

```
No indent: This runs always
├─ if condition:
│  Indent: This runs if true
│  Indent: Multiple statements here
│  Indent: All must be indented the same
Outdented: Back to normal, runs always
```

**Critical rule:** Indentation matters in Python!

```python
# Wrong - syntax error
if age >= 18:
print("Adult")  # Error: not indented

# Correct
if age >= 18:
    print("Adult")  # Indented properly
```

---

## Mental Model 7: Boolean Short-Circuit Evaluation (Optimization)

Python evaluates conditions left-to-right and stops early if result is certain.

```python
# and: stops when first False is found
if condition1 and condition2:
    # If condition1 is False, condition2 is never checked
    pass

# or: stops when first True is found
if condition1 or condition2:
    # If condition1 is True, condition2 is never checked
    pass
```

**Real example:**

```python
def is_admin():
    print("Checking admin status")
    return True

username = "alice"

if username == "alice" and is_admin():
    print("Both conditions checked")
    # Output will include "Checking admin status"

username = "bob"

if username == "alice" and is_admin():
    # is_admin() is NOT called because username != "alice"
    # Output will NOT include "Checking admin status"
    pass
```

**Why it matters:**

```python
# Efficient ordering
if not file_exists() or file_is_empty():
    # Check cheap condition (not) before expensive one (file_is_empty)
    pass
```

---

## Mental Model 8: Conditional Assignment (Ternary Operator)

Assign values based on conditions in one line.

```python
value = value_if_true if condition else value_if_false
```

**Real example:**

```python
age = 25
status = "adult" if age >= 18 else "minor"
print(status)  # Output: adult
```

**Equivalent to:**

```python
age = 25
if age >= 18:
    status = "adult"
else:
    status = "minor"
print(status)
```

**More examples:**

```python
score = 85
result = "pass" if score >= 70 else "fail"

is_raining = True
action = "stay inside" if is_raining else "go out"
```

**Use when:** Simple one-line decisions. Don't nest multiple ternary operators - it becomes unreadable.

---

## Mental Model 9: Common Conditional Patterns (Idioms)

**Pattern 1: Check and set flag**

```python
is_valid = False
if user_input and len(user_input) >= 8:
    is_valid = True
```

**Pattern 2: Guard clause (early return)**

```python
def process_user(user):
    if user is None:
        return  # Exit early if invalid
    
    # Process user...
```

**Pattern 3: Multiple conditions with meaningful names**

```python
is_age_ok = age >= 18
is_verified = email_verified
is_active = account_active

if is_age_ok and is_verified and is_active:
    print("User qualified")
```

**Pattern 4: Fallback values**

```python
user_role = "guest"  # Default

if user_logged_in:
    if user_is_admin:
        user_role = "admin"
    else:
        user_role = "member"
```

**Pattern 5: Check membership**

```python
command = "delete"
safe_commands = ["list", "view", "export"]

if command not in safe_commands:
    print("Unsafe command blocked")
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Why Doesn't My elif Execute?"

**The question:** I have multiple elif blocks, but the wrong one executes.

**The answer:** Only the FIRST true condition executes. Once a condition matches, the rest are skipped.

```python
score = 95

if score >= 90:
    print("A")  # This executes
elif score >= 80:  # NEVER reached because previous if was true
    print("B")
```

Solution: Make sure conditions don't overlap, or use separate if statements if you need multiple branches.

### Confusion 2: "= vs == in Conditions"

**The question:** Why does `if x = 5:` error out?

**The answer:** `=` is assignment. `==` is comparison.

```python
if x = 5:       # ERROR: assigns 5 to x
if x == 5:      # Correct: compares x to 5
```

### Confusion 3: "Why Doesn't My Nested If Work?"

**The question:** My nested condition never executes.

**The answer:** Check outer condition first.

```python
if age >= 18:              # This is False
    if has_license:        # Never checked because outer is false
        print("Can drive")

# If age is 15, inner condition never runs
```

### Confusion 4: "and vs or is Confusing"

**The question:** When do I use and vs or?

**The answer:**
- **and:** Both must be true (stricter)
- **or:** At least one must be true (looser)

```python
# and: stricter
if age >= 18 and has_license:  # BOTH required

# or: looser
if is_weekend or is_holiday:   # Either works
```

### Confusion 5: "My Multiple Conditions Seem Wrong"

**The question:** I'm checking multiple things and it's hard to debug.

**The answer:** Name your conditions.

```python
# Hard to read
if age >= 18 and income > 30000 and credit_score > 700:
    print("Approved")

# Clear
is_age_ok = age >= 18
is_income_ok = income > 30000
is_credit_ok = credit_score > 700

if is_age_ok and is_income_ok and is_credit_ok:
    print("Approved")
```

---

## How If/Else Works Internally (Execution Model)

When Python encounters an if statement:

```
Step 1: EVALUATE CONDITION
  Compute the comparison/condition
  Result is a boolean (True or False)

Step 2: CHECK RESULT
  Is result True?
    - Yes: Go to Step 3
    - No: Go to Step 4

Step 3: EXECUTE IF BLOCK
  Run all indented statements under if
  Then go to Step 5

Step 4: CHECK ELIF BLOCKS
  If there are elif blocks, check each in order
  First true elif block executes, others skip
  If no elif is true, execute else (if present)
  Then go to Step 5

Step 5: CONTINUE
  Continue with code after if/else block
```

**Example execution trace:**

```python
score = 85

if score >= 90:          # Step 1-2: 85 >= 90? False
    print("A")           # Step 4: Skip this
elif score >= 80:        # Step 1-2: 85 >= 80? True
    print("B")           # Step 3: Execute this
elif score >= 70:        # Skipped (previous elif was true)
    print("C")
else:                    # Skipped (an elif already matched)
    print("F")

# Output: B
```

---

## Real-World If/Else (Practical Applications)

**E-commerce - Add to cart:**

```python
item_price = 19.99
user_budget = 50
item_in_stock = True

if item_in_stock:
    if user_budget >= item_price:
        print("Item added to cart")
    else:
        print("Insufficient budget")
else:
    print("Item out of stock")
```

**Game - Health check:**

```python
player_health = 0

if player_health <= 0:
    print("Game Over")
elif player_health < 20:
    print("Critical health - find health pack")
elif player_health < 50:
    print("Low health - use caution")
else:
    print("Good health - ready to fight")
```

**Banking - Transaction validation:**

```python
balance = 1000
withdrawal = 500
daily_limit = 2000

if withdrawal > balance:
    print("Insufficient funds")
elif withdrawal > daily_limit:
    print("Exceeds daily limit")
elif withdrawal <= 0:
    print("Invalid amount")
else:
    print("Withdrawal approved")
    balance -= withdrawal
    print(f"New balance: {balance}")
```

---

## Summary - The Big Picture

**What you learned:**
1. If statements - execute when condition is true
2. Else - execute when condition is false
3. Elif - check multiple conditions in sequence
4. Nested if - conditions within conditions
5. Logical operators (and, or, not)
6. Indentation matters
7. Conditional assignment
8. Common patterns and idioms

**Why this matters:**
- If/else is the foundation of decision-making
- Almost every program makes choices
- Proper structure prevents bugs
- Readability is critical

**What's next:**
Now you can make single decisions.

Topic 10 teaches **Logical Operators** - how to combine multiple conditions elegantly.

---

## What You Should Be Able To Do Now

✅ Write if statements correctly
✅ Use if/else for two-branch decisions
✅ Use elif for multi-branch decisions
✅ Nest if statements
✅ Use logical operators (and, or, not)
✅ Understand execution flow
✅ Format code with proper indentation
✅ Debug conditional logic
✅ Write readable condition expressions
✅ Choose appropriate conditional structures

