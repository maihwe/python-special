# Topic 2: Variables - Storing and Naming Data

## Goal

**Learn how to store data in variables. Understand that variables are labeled containers holding values in computer memory. Master the fundamental concept that programming is about storing, retrieving, and manipulating data.**

---

## Why This Matters - The Real Problem

Topic 1 let you display static text. But that's useless for real programs.

Real programs need to **work with changing data**:
- Calculate a student's grade (data: test scores)
- Track a bank balance (data: account balance)
- Manage inventory (data: item quantities)
- Play a game (data: player health, score, position)

Without variables, you'd have to hardcode everything:

```python
print("Student 1 average:", (85 + 92 + 88) / 3)
print("Student 2 average:", (90 + 95 + 87) / 3)
print("Student 3 average:", (78 + 85 + 80) / 3)
# ... this is nightmare code
```

With variables, you organize data meaningfully:

```python
student1_score1 = 85
student1_score2 = 92
student1_score3 = 88
student1_average = (student1_score1 + student1_score2 + student1_score3) / 3
print(f"Student 1 average: {student1_average}")
```

Variables are the **foundation of all programming**. Without them, you can't build anything real.

---

## Mental Model 1: The Filing Cabinet (Physical Storage Model)

Imagine your computer's memory as a massive filing cabinet with billions of drawers:

```
┌─────────────────────────────────────┐
│         FILING CABINET              │
│         (Computer Memory)           │
├─────────────────────────────────────┤
│                                     │
│  [Drawer 1000]  age: 25            │
│  Label: age                         │
│  Contents: 25                       │
│                                     │
│  [Drawer 1001]  name: "Alice"      │
│  Label: name                        │
│  Contents: Alice                    │
│                                     │
│  [Drawer 1002]  balance: 1500.50   │
│  Label: balance                     │
│  Contents: 1500.50                  │
│                                     │
│  [Drawer 1003]  is_student: True   │
│  Label: is_student                  │
│  Contents: True                     │
│                                     │
│  [Drawer 1004]  [empty]            │
│  [Drawer 1005]  [empty]            │
│                                     │
└─────────────────────────────────────┘
```

When you create a variable:

```python
age = 25
```

Python does this:
1. **Finds empty drawer** (Computer allocates free memory location)
2. **Puts value inside** (Stores 25 in that location)
3. **Creates label** (Associates "age" with that location)

When you use the variable:

```python
print(age)
```

Python does this:
1. **Reads the label** ("age")
2. **Finds the drawer** (Looks up which memory location has this label)
3. **Gets the contents** (Retrieves the value: 25)
4. **Uses it** (Displays or processes it)

**Key insight:** The label is NOT the data. The data is in the drawer. The label just helps you find it.

---

## Mental Model 2: Memory Locations - Where Variables Actually Live

This is deeper than the filing cabinet. Let's understand actual computer memory.

Your computer's RAM is like a row of numbered boxes:

```
Memory Visualization:
Address:  1000  1001  1002  1003  1004  1005  1006  1007  1008  1009
Contents: [25]  [?]  ["A"]  [?]  [True] [?]  [1500][50]  [?]  [?]
           ↑                          ↑              ↑
         age=25                  is_student   balance=1500.50
```

Each memory location has:
- **Address** (location number like 1000, 1001, etc.)
- **Contents** (the actual data stored there)

A variable is Python's way of creating a **human-readable label** for these addresses:

```python
age = 25
```

Internally, Python:
1. Allocates memory at address 1000
2. Stores 25 at address 1000
3. Creates internal mapping: "age" → 1000

When you use `age`, Python:
1. Looks up "age" in its mapping
2. Finds it points to address 1000
3. Retrieves the value at 1000 (which is 25)

**Why this matters:** This explains why variables can change:

```python
age = 25      # Location 1000 contains: 25
age = 26      # Location 1000 is updated to: 26 (old value discarded)
print(age)    # Retrieves from 1000, gets 26
```

The drawer stays the same; only the contents change.

---

## Mental Model 3: Variable Names Are Human Labels (Not Data)

This is critical to understand: **Variable names are for humans, not the computer.**

The name `age` is meaningless to the computer. It's just a label we created.

```python
age = 25
years_old = 25
a = 25
x = 25
```

All of these store the exact same number (25) in memory. The computer doesn't care which label you use.

But **naming matters for humans**:

```python
# Good names - crystal clear
student_gpa = 3.8
account_balance = 1500.50
is_logged_in = True
items_in_cart = 5

# Bad names - confusing
a = 3.8
b = 1500.50
c = True
d = 5

# Terrible names - meaningless
x = 3.8
y = 1500.50
z = True
w = 5
```

Imagine reading code six months later:
- `student_gpa = 3.8` → Crystal clear what this is
- `x = 3.8` → What is x? Is it important? How is it used?

**Variable naming is your communication with future programmers (including your future self).**

Professional code prioritizes readability because:
1. Most time is spent reading code, not writing it
2. Code is read by humans, even if executed by computers
3. Good names prevent bugs
4. Good names make maintenance easier

---

## Mental Model 4: Data Types - Different Kinds of Data (Type System)

Different types of data behave differently.

```python
age = 25              # Integer - whole number
gpa = 3.85           # Float - decimal number
name = "Alice"       # String - text
is_student = True    # Boolean - true/false
```

**Why types matter:**

```python
# Numbers can do math
price = 19.99
quantity = 5
total = price * quantity  # 99.95 (math works)

# Text cannot (it's different)
price_text = "19.99"
quantity_text = "5"
total = price_text * quantity_text  # ERROR - can't multiply text
```

Each type has different rules:

**Numbers (int, float):**
- Can do math: +, -, *, /, //, %, **
- Can compare: >, <, ==, !=
- Can convert to other types

**Strings (text):**
- Can concatenate (join): "Hello" + " " + "World" = "Hello World"
- Can repeat: "Ha" * 3 = "HaHaHa"
- Can access characters: "Hello"[0] = "H"
- Can check length: len("Hello") = 5

**Booleans (True/False):**
- Can combine with logic: True and False = False
- Used in conditions: if is_student: ...
- Result of comparisons: age > 18 = True or False

**Key insight:** Python tracks the type of each variable:

```python
age = 25
print(type(age))  # <class 'int'> - it's an integer

age = "25"
print(type(age))  # <class 'str'> - now it's a string!
```

You can **change the type** by assigning a different value:

```python
value = 42           # integer
value = "42"         # now a string
value = [4, 2]       # now a list
value = True         # now a boolean
```

This flexibility is powerful but also error-prone. Always know what type you're working with.

---

## Mental Model 5: Variable Assignment - The Equals Sign (Assignment Model)

The `=` sign in programming is NOT "equals" (like in math).

It's **assignment**: "Store this value in this location."

```python
age = 25  # Not "age equals 25" (math)
          # Rather: "Store 25 in location labeled age"
```

**Right side executes first:**

```python
x = 5 + 3  # Python calculates: 5 + 3 = 8
           # Then stores: x = 8
           # NOT: x = 5 + 3 (stores the math expression)
```

**You can reassign:**

```python
age = 25
print(age)  # 25

age = 30    # New value overwrites old
print(age)  # 30
            # The old value (25) is gone forever
```

**You can use old value to create new:**

```python
age = 25
age = age + 1  # Read: take current age (25), add 1, store back
print(age)     # 26
```

This is different from math where you can't solve `x = x + 1`.

In programming, it's normal:
1. Read current value of x
2. Calculate x + 1
3. Store result back in x

---

## Mental Model 6: Variable Scope - Where Variables Live (Scope Model)

A variable only exists in certain parts of your program.

**Global scope:** Accessible everywhere
```python
age = 25  # Defined at top level

print(age)  # Can use it here
```

**Local scope:** Accessible only in certain blocks (we'll cover this in functions)

For now, understand: **Variables are created where you define them, exist after definition.**

```python
print(x)  # ERROR - x doesn't exist yet
x = 5
print(x)  # Works - x now exists
```

---

## Mental Model 7: Mutability - Variables Can Change (State Model)

Variables are called "variables" because they **vary**.

Unlike constants, variables can change throughout your program:

```python
balance = 1000
print(f"Starting balance: {balance}")

balance = balance - 50  # Withdraw
print(f"After withdrawal: {balance}")

balance = balance + 200  # Deposit
print(f"After deposit: {balance}")
```

Each time you assign a new value, the variable changes.

This is powerful because it lets programs respond to events:
- User clicks a button → variable changes
- Time passes → variable updates
- Calculation completes → variable stores result
- Data arrives → variable receives it

Without mutability, programs would be static and useless.

---

## Mental Model 8: Naming Conventions - Python Culture (Style Model)

Python has style guidelines (PEP 8) that the community follows.

```python
# Good Python style
student_name = "Alice"
student_gpa = 3.8
is_graduated = False
item_count = 5

# Bad style (but still works)
StudentName = "Alice"      # CamelCase (not Python style)
student_Name = "Alice"     # Mixed (confusing)
STUDENT_NAME = "Alice"     # ALL_CAPS (reserved for constants)
studentname = "Alice"      # No separator (hard to read)
```

Python conventions:
- **Lowercase with underscores:** `student_name`, `account_balance`, `is_active`
- **Only UPPERCASE for constants:** `PI = 3.14159`, `MAX_USERS = 1000`
- **Clear, descriptive names:** `age` not `a`, `price` not `p`

**Why follow conventions?**
1. Other Python programmers expect it
2. Makes code readable
3. Professional teams enforce it
4. Many tools check for it

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "What's the Difference Between Variable Name and Value?"

**The question:** When I write `age = 25`, what's `age` and what's `25`?

**The answer:**
- `age` is the **variable name** (label for the drawer)
- `25` is the **value** (contents of the drawer)

```python
age = 25
│     │
│     └─ Value (the number stored)
└─ Name (the label)
```

When you use the variable:
```python
print(age)  # Use the name "age"
            # Python looks it up, finds value 25
            # Displays: 25
```

When you use the value:
```python
print(25)   # Use the value directly
            # Displays: 25
```

Both produce the same output, but work differently:
```python
print(age)   # Lookup → retrieval → display
print(25)    # Direct → display
```

### Confusion 2: "What Happens to Old Values When I Reassign?"

**The question:** If I do `x = 5` then `x = 10`, where does 5 go?

**The answer:** **It disappears. Permanently.**

```python
x = 5       # Memory location 1000 contains: 5
x = 10      # Memory location 1000 is overwritten: now contains 10
            # The 5 is gone forever (unless we saved it elsewhere)

print(x)    # 10 (there's no way to get 5 back)
```

If you need the old value, save it first:

```python
x = 5
old_x = x   # Save it
x = 10

print(old_x)  # 5 (we saved it, so we can use it)
print(x)      # 10
```

### Confusion 3: "Can Variable Names Have Spaces?"

**The question:** Why not `my age = 25` instead of `my_age = 25`?

**The answer:** Python syntax doesn't allow spaces in names.

```python
my age = 25      # SYNTAX ERROR
my_age = 25      # Correct - use underscore
myage = 25       # Also correct, but less readable
my-age = 25      # ERROR - hyphens not allowed (except subtraction)
```

This is because Python uses spaces to separate tokens:

```python
my age = 25
│  │
├─ token 1: my (variable name?)
└─ token 2: age (another name? math operation?)
   
Confusing! So Python disallows it.
```

With underscores:
```python
my_age = 25
│      │
└ One token: the variable name my_age
```

Clear and unambiguous.

### Confusion 4: "Why Do Variables Have Types?"

**The question:** Why can't I just store anything anywhere?

**The answer:** Types provide structure and safety.

```python
# Without types, anything could happen:
age = 25          # number
age = "25"        # string
age = [2, 5]      # list
age = {"years": 25}  # dictionary

# Later in code:
result = age + 10  # What does this mean?
                   # If age is 25: result is 35
                   # If age is "25": ERROR
                   # If age is [2,5]: ERROR
                   # If age is dict: ERROR
```

Types help prevent bugs:

```python
age = 25  # clearly a number
result = age + 10  # makes sense
print(result)  # 35
```

Python's dynamic typing (can change types) is flexible but error-prone if careless.

### Confusion 5: "What's the Difference Between `=` and `==`?"

**The question:** I see both in code. Aren't they the same?

**The answer:** Completely different!

```python
age = 25        # Assignment (store value)
age == 25       # Comparison (test if equal)
```

- `=` : **One equals sign** = assignment (stores value)
- `==` : **Two equals signs** = comparison (tests if equal, returns True/False)

```python
x = 5           # x now contains 5

if x == 5:      # Test: does x equal 5?
    print("Yes")  # Yes, it does

if x == 10:     # Test: does x equal 10?
    print("No")   # No, x is still 5
```

This is a common source of bugs (using `=` when you meant `==`).

---

## How Variable Assignment Actually Works (Internal Mechanism)

When Python executes `age = 25`:

```
Step 1: PARSE
  Python reads: age = 25
  Identifies:
    - Left side: age (target for assignment)
    - Right side: 25 (value to store)

Step 2: EVALUATE RIGHT SIDE
  Python evaluates: 25
  Result: 25 (it's a literal, already evaluated)

Step 3: ALLOCATE MEMORY
  Python checks if "age" already exists
  - If yes: will overwrite
  - If no: allocates new memory location

Step 4: DETERMINE TYPE
  Python looks at value: 25
  Determines type: integer (int)

Step 5: CREATE BINDING
  Python creates/updates mapping:
    Variable name: "age"
    Memory address: 1000
    Value: 25
    Type: int

Step 6: STORE
  Python writes 25 to memory address 1000

Step 7: COMPLETE
  Assignment done, Python continues
```

When you use the variable:

```
print(age)

Step 1: LOOKUP
  Python sees: age
  Looks up in variable table
  Finds: "age" → address 1000

Step 2: RETRIEVE
  Python reads memory at address 1000
  Gets value: 25

Step 3: USE
  Python passes 25 to print()
  print() displays: 25
```

---

## Real-World Variables (Why They Matter)

Variables are everywhere in real programs:

**Video game:**
```python
player_x = 100          # Player position
player_y = 200
player_health = 100     # Game state
player_score = 0
enemy_position_x = 500
enemy_position_y = 150
enemy_health = 50
game_running = True
```

**Bank app:**
```python
account_holder = "Alice"
account_number = "123456789"
balance = 5000.00
transaction_date = "2026-09-01"
transaction_amount = 250.00
transaction_type = "withdrawal"
```

**Temperature sensor:**
```python
current_temp = 23.5      # Celsius
is_too_hot = False
warning_threshold = 30
alarm_triggered = False
```

All of these work with variables to track state (what's happening right now).

---

## Summary - The Big Picture

**What you learned:**
1. Variables store data in memory
2. Variables have names (labels) and values (contents)
3. Variable names are for humans; computers use memory addresses
4. Variables have types (int, str, bool, float, etc.)
5. Variables can change (that's why they're called variables)
6. Assignment `=` differs from comparison `==`
7. Following naming conventions matters for code quality

**Why this matters:**
- Variables are the foundation of all programming
- Without them, programs can't track state
- Good variable names make code readable
- Understanding memory helps prevent bugs
- Types provide structure and catch errors

**What's next:**
Now you can store data. But what if you want data from the user?

Topic 3 teaches **input()** - how to get data from people, not just hardcode it.

---

## What You Should Be Able To Do Now

✅ Create variables and assign values
✅ Understand where variables live in memory
✅ Use meaningful variable names
✅ Know the type of a variable
✅ Change variables (reassignment)
✅ Use variables in calculations
✅ Understand assignment vs. comparison
✅ Explain what happens when you create a variable
✅ Predict output of variable operations

