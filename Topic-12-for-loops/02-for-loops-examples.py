# Topic 12: For Loops - Elaborate Examples
# Comprehensive examples of iterating over sequences with for loops

# ============================================================================
# EXAMPLE 1: Basic For Loop - Iterating Over List
# ============================================================================
# Loop through each item in a list

print("Example 1: Basic For Loop")
print("-" * 50)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print()

# ============================================================================
# EXAMPLE 2: For Loop Over String
# ============================================================================
# Each character is an item

print("Example 2: Loop Over String")
print("-" * 50)

word = "hello"
for char in word:
    print(char, end=" ")
print()
print()

# ============================================================================
# EXAMPLE 3: Using Range - Count Up
# ============================================================================
# Generate sequence of numbers

print("Example 3: Range - Count Up")
print("-" * 50)

for i in range(5):
    print(i, end=" ")
print()
print()

# ============================================================================
# EXAMPLE 4: Range - Start and Stop
# ============================================================================
# Start from specific number

print("Example 4: Range with Start and Stop")
print("-" * 50)

for i in range(2, 6):
    print(i, end=" ")
print()
print()

# ============================================================================
# EXAMPLE 5: Range - Step
# ============================================================================
# Skip by specified amount

print("Example 5: Range with Step")
print("-" * 50)

for i in range(0, 10, 2):
    print(i, end=" ")
print()
print()

# ============================================================================
# EXAMPLE 6: Range - Countdown
# ============================================================================
# Count down using negative step

print("Example 6: Countdown with Range")
print("-" * 50)

for i in range(5, 0, -1):
    print(i, end=" ")
print()
print("Blastoff!")
print()

# ============================================================================
# EXAMPLE 7: Sum Using For Loop
# ============================================================================
# Accumulate total while looping

print("Example 7: Sum Accumulation")
print("-" * 50)

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num

print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print()

# ============================================================================
# EXAMPLE 8: Finding Maximum
# ============================================================================
# Find largest value in list

print("Example 8: Find Maximum")
print("-" * 50)

scores = [85, 92, 78, 95, 88]
max_score = scores[0]

for score in scores:
    if score > max_score:
        max_score = score

print(f"Scores: {scores}")
print(f"Maximum: {max_score}")
print()

# ============================================================================
# EXAMPLE 9: Counting Occurrences
# ============================================================================
# Count how many times item appears

print("Example 9: Count Occurrences")
print("-" * 50)

letters = "mississippi"
count = 0
target = "s"

for char in letters:
    if char == target:
        count += 1

print(f"Text: {letters}")
print(f"'{target}' appears {count} times")
print()

# ============================================================================
# EXAMPLE 10: Using Enumerate
# ============================================================================
# Get both index and item

print("Example 10: Enumerate")
print("-" * 50)

colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

print()

# ============================================================================
# EXAMPLE 11: Enumerate with Start
# ============================================================================
# Start indexing from 1 instead of 0

print("Example 11: Enumerate Starting at 1")
print("-" * 50)

items = ["apple", "banana", "cherry"]
for num, item in enumerate(items, 1):
    print(f"{num}. {item}")

print()

# ============================================================================
# EXAMPLE 12: Build String from Loop
# ============================================================================
# Concatenate in loop

print("Example 12: Building String")
print("-" * 50)

result = ""
for i in range(1, 6):
    result += str(i)

print(f"Built: {result}")
print()

# ============================================================================
# EXAMPLE 13: Nested For Loops - Grid
# ============================================================================
# Loop within loop for 2D pattern

print("Example 13: Nested Loops - Grid")
print("-" * 50)

for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()

print()

# ============================================================================
# EXAMPLE 14: Times Table with Nested Loop
# ============================================================================
# Multiplication table

print("Example 14: Times Table")
print("-" * 50)

for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"{product:2}", end=" ")
    print()

print()

# ============================================================================
# EXAMPLE 15: Break in For Loop
# ============================================================================
# Exit loop when condition met

print("Example 15: Break Statement")
print("-" * 50)

for num in [1, 2, 3, 4, 5]:
    if num == 3:
        print("Found 3, breaking!")
        break
    print(num)

print()

# ============================================================================
# EXAMPLE 16: Continue in For Loop
# ============================================================================
# Skip current iteration

print("Example 16: Continue Statement")
print("-" * 50)

for num in [1, 2, 3, 4, 5]:
    if num == 3:
        print(f"Skipping {num}")
        continue
    print(num)

print()

# ============================================================================
# EXAMPLE 17: Search for Item
# ============================================================================
# Find and report location

print("Example 17: Search in List")
print("-" * 50)

names = ["Alice", "Bob", "Charlie", "Diana"]
target = "Charlie"
found = False

for name in names:
    if name == target:
        print(f"Found: {target}")
        found = True
        break

if not found:
    print(f"Not found: {target}")

print()

# ============================================================================
# EXAMPLE 18: Filter Items
# ============================================================================
# Keep only items that match condition

print("Example 18: Filter Items")
print("-" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f"Original: {numbers}")
print(f"Even numbers: {evens}")
print()

# ============================================================================
# EXAMPLE 19: Transform Items
# ============================================================================
# Apply operation to each item

print("Example 19: Transform Items")
print("-" * 50)

numbers = [1, 2, 3, 4, 5]
squared = []

for num in numbers:
    squared.append(num ** 2)

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print()

# ============================================================================
# EXAMPLE 20: List Comprehension - Squares
# ============================================================================
# Create list in one line

print("Example 20: List Comprehension")
print("-" * 50)

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print()

# ============================================================================
# EXAMPLE 21: List Comprehension with Filter
# ============================================================================
# Filter while creating list

print("Example 21: Comprehension with Filter")
print("-" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]

print(f"Original: {numbers}")
print(f"Even numbers: {evens}")
print()

# ============================================================================
# EXAMPLE 22: Looping Over Numbers with Reverse
# ============================================================================
# Process numbers in reverse

print("Example 22: Reverse Iteration")
print("-" * 50)

numbers = [10, 20, 30, 40, 50]
for num in reversed(numbers):
    print(num)

print()

# ============================================================================
# EXAMPLE 23: Looping Over Sorted List
# ============================================================================
# Sort and then loop

print("Example 23: Sorted Iteration")
print("-" * 50)

scores = [85, 92, 78, 95, 88]
for score in sorted(scores):
    print(score)

print()

# ============================================================================
# EXAMPLE 24: Double Loop - Matrix Operations
# ============================================================================
# Process 2D list

print("Example 24: Matrix Processing")
print("-" * 50)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Matrix:")
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

print()

# ============================================================================
# EXAMPLE 25: Zip - Iterate Over Multiple Lists
# ============================================================================
# Loop over lists together

print("Example 25: Zip - Multiple Lists")
print("-" * 50)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

