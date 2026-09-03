# Topic 11: While Loops - Repeating Actions Until a Condition Changes

## Goal

**Learn to repeat code using while loops. Understand when to use loops, how to control repetition with conditions, loop variables, preventing infinite loops, and using break/continue. Master the foundation of iteration.**

---

## Why This Matters - The Real Problem

Many problems require repetition:

- **User input:** Keep asking until valid input received
- **Game loops:** Repeat game logic until player quits
- **Data processing:** Process items until list is empty
- **Animations:** Repeat frames until animation finishes
- **Waiting:** Retry action until it succeeds
- **Simulations:** Repeat time steps until simulation ends

Without loops, you'd write the same code over and over:

**Without loops (horrible):**
```python
print("Enter age:")
age = int(input())
if age < 0 or age > 150:
    print("Invalid age")
    print("Enter age:")
    age = int(input())
    if age < 0 or age > 150:
        print("Invalid age")
        print("Enter age:")
        age = int(input())
        # ... repeat forever
```

**With loops (elegant):**
```python
while True:
    print("Enter age:")
    age = int(input())
    if 0 <= age <= 150:
        break  # Exit loop when valid
    print("Invalid age")
```

**While loops let you repeat with elegance.**

---

## Mental Model 1: What Is a While Loop? (The Repetition Model)

A **while loop** repeats code AS LONG AS a condition is True.

```python
while condition:
    # Repeat this code while condition is True
    # When condition becomes False, loop stops
```

**Visual representation:**

```
        Start
          ↓
    Is condition true?
      /         \
    Yes         No
     ↓           ↓
Execute      Stop loop
  code       Continue
 (repeat)     program
     ↑           ↓
     └─ Go back to check condition
```

**Real example:**

```python
count = 0
while count < 3:
    print(f"Count: {count}")
    count = count + 1

# Output:
# Count: 0
# Count: 1
# Count: 2
```

**Critical insight:** The condition is checked BEFORE each iteration.

```python
x = 10
while x < 5:
    print(x)  # Never executes because x < 5 is False initially
```

---

## Mental Model 2: Loop Variables and Updates (The Counter Pattern)

A **loop variable** tracks the loop's state. It must **update** each iteration, or you get an infinite loop.

```python
count = 0         # Loop variable
while count < 3:  # Check condition
    print(count)
    count += 1    # UPDATE the loop variable!
```

**Three essential parts:**

1. **Initialization:** Set loop variable before loop
2. **Condition:** Check loop variable
3. **Update:** Change loop variable inside loop

```python
# 1. Initialize
i = 0

# Loop starts
while i < 5:  # 2. Condition
    print(i)
    i += 1    # 3. Update (CRITICAL!)
# Loop ends when i >= 5
```

**Missing any part causes problems:**

```python
# Missing initialization
while i < 5:        # ERROR: i not defined
    print(i)

# Missing condition
while True:         # Infinite loop!
    print("Stuck")

# Missing update
count = 0
while count < 5:
    print(count)    # Infinite loop! count never changes
```

---

## Mental Model 3: Infinite Loops and How to Stop Them (The Exit Model)

An **infinite loop** repeats forever.

```python
while True:
    print("This repeats forever")
    # No exit condition!
```

**Intentional infinite loops are okay WITH an exit:**

```python
while True:
    response = input("Continue? (yes/no): ")
    if response == "no":
        break  # Exit the loop
    print("Continuing...")
```

**Accidental infinite loops happen when:**

```python
# Problem 1: Condition never changes
x = 5
while x > 0:
    print(x)
    # Missing: x -= 1
    # x never changes, loop never ends!

# Problem 2: Condition always true
while True:
    print("Stuck")
    # No break statement

# Problem 3: Wrong operator
count = 0
while count != 5:
    print(count)
    count += 2  # Skips 5 (0, 2, 4, 6...)
    # count will never equal 5!
```

**Safe infinite loops with break:**

```python
# Good pattern
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break  # Exit here
    # Process input...
```

---

## Mental Model 4: Break and Continue (Loop Control)

**break:** Exits the loop immediately.

```python
while True:
    response = input("Continue? (yes/no): ")
    if response == "no":
        break  # Stop loop now
    print("Continuing...")
```

**continue:** Skips to the next iteration.

```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip rest of loop, go to next iteration
    print(count)

# Output: 1, 2, 4, 5 (skips 3)
```

**Visual:**

```
        Check condition
            ↓
        Execute code
            ↓
    ┌──────→ continue? ────→ (Skip to top)
    │
    │ break? (Exit)
    │        ↓
    │    Exit loop
    │
    └──→ Next iteration
```

**When to use:**

- **break:** When you want to stop the loop completely
- **continue:** When you want to skip the rest of current iteration

---

## Mental Model 5: Loop Accumulation Patterns (The Accumulator Model)

A common pattern: accumulate a result while looping.

```python
total = 0  # Accumulator
count = 0
while count < 5:
    total += count  # Add to accumulator
    count += 1
print(total)  # 0 + 1 + 2 + 3 + 4 = 10
```

**Real-world examples:**

```python
# Sum numbers
total = 0
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Total: {total}")

# Count occurrences
text = "hello world"
count = 0
index = 0
while index < len(text):
    if text[index] == "l":
        count += 1
    index += 1
print(f"Count of 'l': {count}")

# Build string
result = ""
i = 0
while i < 3:
    result += str(i)
    i += 1
print(result)  # "012"
```

---

## Mental Model 6: Nested Loops (Loops Within Loops)

You can put loops inside other loops.

```python
i = 0
while i < 3:           # Outer loop
    j = 0
    while j < 2:       # Inner loop
        print(f"({i}, {j})")
        j += 1
    i += 1
```

**Output:**
```
(0, 0)
(0, 1)
(1, 0)
(1, 1)
(2, 0)
(2, 1)
```

**Real-world uses:**

```python
# Game board
row = 0
while row < 3:
    col = 0
    while col < 3:
        print("□", end=" ")
        col += 1
    print()  # New line
    row += 1

# Matrix operations
rows = 3
cols = 3
row = 0
while row < rows:
    col = 0
    while col < cols:
        # Process cell at (row, col)
        col += 1
    row += 1
```

---

## Mental Model 7: Input Validation Pattern (Common Loop Use)

A typical use: keep asking for input until valid.

```python
while True:
    try:
        age = int(input("Age (0-150): "))
        if 0 <= age <= 150:
            break  # Valid, exit loop
        print("Age must be 0-150")
    except ValueError:
        print("Please enter a number")

print(f"Your age: {age}")
```

**Pattern:**

```
Loop until valid input:
1. Prompt user
2. Try to process
3. If invalid, show error and loop back
4. If valid, break
```

---

## Mental Model 8: Simulation and State Machines (Advanced Loop Use)

Loops can simulate real-world processes by tracking state.

```python
# Simulation: ball bouncing
height = 100
velocity = 0
gravity = 10

while height > 0:
    height -= velocity
    velocity += gravity
    print(f"Height: {height}, Velocity: {velocity}")
    if height < 0:
        break

# Simulation: character health
health = 100
turn = 0

while health > 0:
    enemy_damage = 10
    health -= enemy_damage
    turn += 1
    print(f"Turn {turn}: Health {health}")

print("Game Over")
```

---

## Mental Model 9: Loop Patterns and Best Practices (Idioms)

**Pattern 1: Counting up**

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

**Pattern 2: Counting down**

```python
i = 10
while i > 0:
    print(i)
    i -= 1
```

**Pattern 3: While until condition**

```python
response = ""
while response != "quit":
    response = input("Enter command: ")
    if response != "quit":
        process(response)
```

**Pattern 4: Flag-based**

```python
is_running = True
while is_running:
    # Do something
    if some_condition:
        is_running = False
```

**Pattern 5: Accumulation**

```python
total = 0
while # condition:
    total += next_value()
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Why Does My Loop Never Run?"

**The question:** My while loop doesn't execute at all.

**The answer:** The condition is False from the start.

```python
x = 10
while x < 5:       # x is 10, 10 < 5 is False
    print(x)       # Never executes
```

Solution: Check condition logic.

### Confusion 2: "How Do I Exit an Infinite Loop?"

**The question:** I created `while True:` but can't get out.

**The answer:** Use `break` statement.

```python
while True:
    response = input("Enter 'quit' to exit: ")
    if response == "quit":
        break  # Exits the loop
```

### Confusion 3: "My Loop Updates but Still Runs Forever"

**The question:** I update the variable but loop doesn't stop.

**The answer:** Check your condition logic.

```python
count = 0
while count != 5:
    count += 2  # 0, 2, 4, 6, 8...
    # Never equals 5! Loop never ends!

# Fix:
while count < 5:
    count += 2
```

### Confusion 4: "When Should I Use While vs If?"

**The question:** What's the difference?

**The answer:**
- **if:** Execute ONCE if true
- **while:** Execute REPEATEDLY while true

```python
if x > 5:           # Check once
    print("Big")

while x > 5:        # Repeat while true
    print("Big")
    x -= 1          # Update x each time
```

### Confusion 5: "Difference Between Break and Continue"

**The question:** When do I use each?

**The answer:**
- **break:** Stop loop completely
- **continue:** Skip current iteration, continue loop

```python
while True:
    val = input()
    if val == "quit":
        break      # Stop loop entirely
    if val == "skip":
        continue   # Skip to next iteration
    process(val)
```

---

## How While Loops Work Internally (Execution Model)

```
Step 1: INITIALIZE loop variable
Step 2: CHECK condition
Step 3: If False, EXIT loop
Step 4: If True, EXECUTE loop body
Step 5: UPDATE loop variable
Step 6: Go back to Step 2
```

**Example execution:**

```python
count = 0
while count < 3:
    print(count)
    count += 1

# Execution trace:
# Step 1: count = 0
# Step 2: Is 0 < 3? True
# Step 4: print(0)
# Step 5: count = 1
# Step 2: Is 1 < 3? True
# Step 4: print(1)
# Step 5: count = 2
# Step 2: Is 2 < 3? True
# Step 4: print(2)
# Step 5: count = 3
# Step 2: Is 3 < 3? False
# Step 3: Exit loop
```

---

## Real-World While Loops (Practical Applications)

**Input validation:**

```python
while True:
    password = input("Password (8+ chars): ")
    if len(password) >= 8:
        break
    print("Too short")
```

**Game loop:**

```python
game_running = True
while game_running:
    display_board()
    player_move = get_input()
    update_game(player_move)
    if check_win():
        game_running = False
```

**Data processing:**

```python
while True:
    line = file.readline()
    if not line:
        break
    process(line)
```

---

## Summary - The Big Picture

**What you learned:**
1. While loops repeat while condition is true
2. Three parts: initialize, condition, update
3. Infinite loops and how to prevent them
4. break and continue for loop control
5. Accumulation patterns
6. Nested loops
7. Input validation with loops
8. State tracking and simulation
9. Common patterns and best practices

**Why this matters:**
- Loops are fundamental to programming
- Most programs repeat actions
- Proper loop control prevents bugs
- Understanding patterns makes code clear

**What's next:**
Now you can repeat actions with conditions.

Topic 12 teaches **For Loops** - a different, powerful way to iterate.

---

## What You Should Be Able To Do Now

✅ Write while loops with proper initialization, condition, update
✅ Prevent infinite loops
✅ Use break to exit loops
✅ Use continue to skip iterations
✅ Accumulate results while looping
✅ Nest loops correctly
✅ Validate input with loops
✅ Simulate processes with loops
✅ Recognize and use loop patterns
✅ Debug loop logic

