# Topic 11: While Loops - Elaborate Examples
# Comprehensive examples of using while loops to repeat actions

# ============================================================================
# EXAMPLE 1: Basic While Loop
# ============================================================================
# Simple counting loop

print("Example 1: Basic While Loop")
print("-" * 50)

count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

print("Loop finished")
print()

# ============================================================================
# EXAMPLE 2: Counting Down
# ============================================================================
# Decreasing loop variable

print("Example 2: Counting Down")
print("-" * 50)

count = 5
while count > 0:
    print(count)
    count -= 1

print("Blastoff!")
print()

# ============================================================================
# EXAMPLE 3: Loop with String Building
# ============================================================================
# Accumulating a string in a loop

print("Example 3: Building a String")
print("-" * 50)

result = ""
i = 0
while i < 5:
    result += str(i)
    i += 1

print(f"Built string: {result}")
print()

# ============================================================================
# EXAMPLE 4: Summing Numbers
# ============================================================================
# Accumulating a sum

print("Example 4: Sum Accumulation")
print("-" * 50)

total = 0
i = 1
while i <= 5:
    total += i
    i += 1

print(f"Sum of 1 to 5: {total}")
print()

# ============================================================================
# EXAMPLE 5: Infinite Loop with Break
# ============================================================================
# Loop exits when condition met

print("Example 5: Infinite Loop with Break")
print("-" * 50)

count = 0
while True:
    print(f"Iteration {count}")
    count += 1
    if count >= 3:
        print("Breaking out...")
        break

print("Loop exited")
print()

# ============================================================================
# EXAMPLE 6: Using Continue
# ============================================================================
# Skip iterations that meet condition

print("Example 6: Continue Statement")
print("-" * 50)

count = 0
while count < 5:
    count += 1
    if count == 3:
        print(f"  Skipping {count}")
        continue
    print(f"Processing {count}")

print()

# ============================================================================
# EXAMPLE 7: Input Validation
# ============================================================================
# Keep asking until valid input

print("Example 7: Input Validation")
print("-" * 50)

age = None
while age is None:
    try:
        user_input = input("Enter age (0-150): ")
        age = int(user_input)
        if age < 0 or age > 150:
            print("  Invalid! Must be 0-150")
            age = None
        else:
            print(f"  ✓ Valid age: {age}")
    except ValueError:
        print("  Invalid! Please enter a number")

print()

# ============================================================================
# EXAMPLE 8: User Input Until Quit
# ============================================================================
# Process input until user says quit

print("Example 8: Repeat Until Quit")
print("-" * 50)

while True:
    response = input("Enter command (or 'quit' to exit): ")
    if response == "quit":
        print("Goodbye!")
        break
    print(f"  You entered: {response}")

print()

# ============================================================================
# EXAMPLE 9: Nested While Loops
# ============================================================================
# Loop within a loop

print("Example 9: Nested Loops")
print("-" * 50)

i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()  # New line after inner loop
    i += 1

print()

# ============================================================================
# EXAMPLE 10: Drawing a Pattern
# ============================================================================
# Using nested loops to create pattern

print("Example 10: Pattern Drawing")
print("-" * 50)

size = 3
row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end=" ")
        col += 1
    print()  # New line
    row += 1

print()

# ============================================================================
# EXAMPLE 11: Factorial Calculation
# ============================================================================
# Multiply numbers counting down

print("Example 11: Factorial")
print("-" * 50)

n = 5
result = 1
i = n
while i > 1:
    result *= i
    i -= 1

print(f"Factorial of {n}: {result}")
print()

# ============================================================================
# EXAMPLE 12: Counting String Occurrences
# ============================================================================
# Count how many times character appears

print("Example 12: Character Count")
print("-" * 50)

text = "hello world"
target = "l"
count = 0
i = 0

while i < len(text):
    if text[i] == target:
        count += 1
    i += 1

print(f"'{target}' appears {count} times in '{text}'")
print()

# ============================================================================
# EXAMPLE 13: Reversing a String
# ============================================================================
# Build string in reverse order

print("Example 13: String Reversal")
print("-" * 50)

original = "hello"
reversed_str = ""
i = len(original) - 1

while i >= 0:
    reversed_str += original[i]
    i -= 1

print(f"Original: {original}")
print(f"Reversed: {reversed_str}")
print()

# ============================================================================
# EXAMPLE 14: Powers of 2
# ============================================================================
# Generate powers of 2 up to limit

print("Example 14: Powers of 2")
print("-" * 50)

power = 1
limit = 100

print("Powers of 2 up to 100:")
while power <= limit:
    print(power, end=" ")
    power *= 2

print()
print()

# ============================================================================
# EXAMPLE 15: Simulating Dice Rolls
# ============================================================================
# Roll until certain number

print("Example 15: Dice Roll Simulation")
print("-" * 50)

import random

rolls = 0
while True:
    roll = random.randint(1, 6)
    rolls += 1
    print(f"Roll {rolls}: {roll}")
    if roll == 6:
        print("Got a 6! Stopping.")
        break

print()

# ============================================================================
# EXAMPLE 16: Game of Guess the Number
# ============================================================================
# Keep guessing until correct

print("Example 16: Guess Number Game")
print("-" * 50)

secret = 5  # In real game, would be random
guess = None
tries = 0

while guess != secret:
    try:
        guess = int(input("Guess a number (1-10): "))
        tries += 1
        if guess < secret:
            print("  Too low")
        elif guess > secret:
            print("  Too high")
        else:
            print(f"  Correct! It took {tries} tries")
    except ValueError:
        print("  Please enter a number")

print()

# ============================================================================
# EXAMPLE 17: Temperature Check Loop
# ============================================================================
# Monitor temperature until stable

print("Example 17: Temperature Monitoring")
print("-" * 50)

temperature = 95
target = 70

print(f"Current temp: {temperature}°F, Target: {target}°F")
time_step = 0

while temperature > target:
    temperature -= 5  # Cool down 5 degrees per step
    time_step += 1
    print(f"  Step {time_step}: {temperature}°F")

print(f"Reached target temperature after {time_step} steps")
print()

# ============================================================================
# EXAMPLE 18: Bank Account Simulation
# ============================================================================
# Track balance over time

print("Example 18: Bank Account")
print("-" * 50)

balance = 1000
monthly_deposit = 100
months = 0

print(f"Starting balance: ${balance}")
print("Depositing $100/month until $2000:")

while balance < 2000:
    balance += monthly_deposit
    months += 1
    print(f"  Month {months}: ${balance}")

print(f"Goal reached in {months} months!")
print()

# ============================================================================
# EXAMPLE 19: Reading and Summing
# ============================================================================
# Keep summing until 0

print("Example 19: Sum Until Zero")
print("-" * 50)

total = 0
while True:
    try:
        num = int(input("Enter a number (0 to finish): "))
        if num == 0:
            break
        total += num
        print(f"  Running total: {total}")
    except ValueError:
        print("  Please enter a valid number")

print(f"Final sum: {total}")
print()

# ============================================================================
# EXAMPLE 20: Password Entry
# ============================================================================
# Retry password until correct

print("Example 20: Password Retry")
print("-" * 50)

correct_password = "secret"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input(f"Enter password (attempt {attempts + 1}/{max_attempts}): ")
    attempts += 1
    
    if password == correct_password:
        print("✓ Access granted!")
        break
    else:
        if attempts < max_attempts:
            print(f"  Wrong! {max_attempts - attempts} attempts remaining")
        else:
            print("✗ Too many attempts. Access denied.")

print()

# ============================================================================
# EXAMPLE 21: Countdown Timer
# ============================================================================
# Simple timer

print("Example 21: Countdown")
print("-" * 50)

seconds = 5
print(f"Starting countdown from {seconds}...")

while seconds > 0:
    print(seconds)
    seconds -= 1

print("Time's up!")
print()

# ============================================================================
# EXAMPLE 22: Doubling Until Threshold
# ============================================================================
# Keep doubling value until limit

print("Example 22: Doubling")
print("-" * 50)

value = 1
limit = 1000
steps = 0

print(f"Starting at {value}, doubling until >= {limit}:")

while value < limit:
    steps += 1
    value *= 2
    print(f"  Step {steps}: {value}")

print(f"Reached {value} in {steps} steps")
print()

# ============================================================================
# EXAMPLE 23: Validate Multiple Inputs
# ============================================================================
# Get and validate multiple values

print("Example 23: Validate Multiple Values")
print("-" * 50)

numbers = []
count = 0
max_numbers = 3

while count < max_numbers:
    try:
        num = int(input(f"Enter number {count + 1}/{max_numbers}: "))
        if 0 <= num <= 100:
            numbers.append(num)
            count += 1
        else:
            print("  Must be 0-100")
    except ValueError:
        print("  Please enter a valid number")

print(f"You entered: {numbers}")
print()

# ============================================================================
# EXAMPLE 24: Simulating Ball Bounce
# ============================================================================
# Simple physics simulation

print("Example 24: Ball Bounce Simulation")
print("-" * 50)

height = 100
velocity = 0
gravity = 10

print("Ball bouncing (height tracking):")
print(f"Initial height: {height}")

bounce_count = 0
while height > 0 or velocity > 0:
    height -= velocity
    velocity += gravity
    
    if height <= 0:
        bounce_count += 1
        height = 0
        velocity = -velocity * 0.7  # Lose 30% energy
        
        if velocity < 2:  # Stop if velocity too low
            break
        print(f"  Bounce {bounce_count}: peak would be ~{-velocity**2 / (2*gravity):.0f}")

print(f"Ball stopped after {bounce_count} bounces")
print()

# ============================================================================
# EXAMPLE 25: Nested Loop - Times Table
# ============================================================================
# Display multiplication table

print("Example 25: Times Table (3x3)")
print("-" * 50)

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        product = i * j
        print(f"{product:2} ", end="")
        j += 1
    print()  # New line after each row
    i += 1

