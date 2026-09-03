# Topic 13: Lists - Elaborate Examples
# Comprehensive examples of creating and manipulating lists

# ============================================================================
# EXAMPLE 1: Creating Lists
# ============================================================================
# Different ways to create lists

print("Example 1: Creating Lists")
print("-" * 50)

empty = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, None]
range_list = list(range(5))

print(f"Empty: {empty}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")
print(f"From range: {range_list}")
print()

# ============================================================================
# EXAMPLE 2: Indexing - Accessing Items
# ============================================================================
# Get items by position

print("Example 2: Indexing")
print("-" * 50)

fruits = ["apple", "banana", "cherry", "date"]
print(f"List: {fruits}")
print()

print(f"fruits[0] = {fruits[0]}")
print(f"fruits[1] = {fruits[1]}")
print(f"fruits[3] = {fruits[3]}")
print(f"fruits[-1] = {fruits[-1]}")
print(f"fruits[-2] = {fruits[-2]}")
print()

# ============================================================================
# EXAMPLE 3: Slicing - Getting Subsequences
# ============================================================================
# Extract portion of list

print("Example 3: Slicing")
print("-" * 50)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {numbers}")
print()

print(f"numbers[2:5] = {numbers[2:5]}")
print(f"numbers[:3] = {numbers[:3]}")
print(f"numbers[7:] = {numbers[7:]}")
print(f"numbers[::2] = {numbers[::2]}")
print(f"numbers[::-1] = {numbers[::-1]}")
print(f"numbers[1:8:2] = {numbers[1:8:2]}")
print()

# ============================================================================
# EXAMPLE 4: Length and Membership
# ============================================================================
# Check size and if item exists

print("Example 4: Length and Membership")
print("-" * 50)

items = ["apple", "banana", "cherry"]
print(f"List: {items}")
print()

print(f"len(items) = {len(items)}")
print(f"'banana' in items = {'banana' in items}")
print(f"'grape' in items = {'grape' in items}")
print(f"'apple' not in items = {'apple' not in items}")
print()

# ============================================================================
# EXAMPLE 5: Append - Add to End
# ============================================================================
# Add single item

print("Example 5: Append")
print("-" * 50)

items = [1, 2, 3]
print(f"Starting: {items}")

items.append(4)
print(f"After append(4): {items}")

items.append(5)
print(f"After append(5): {items}")
print()

# ============================================================================
# EXAMPLE 6: Extend - Add Multiple Items
# ============================================================================
# Add multiple items

print("Example 6: Extend")
print("-" * 50)

items = [1, 2, 3]
print(f"Starting: {items}")

items.extend([4, 5])
print(f"After extend([4, 5]): {items}")

items.extend([6, 7, 8])
print(f"After extend([6, 7, 8]): {items}")
print()

# ============================================================================
# EXAMPLE 7: Insert - Add at Position
# ============================================================================
# Add at specific index

print("Example 7: Insert")
print("-" * 50)

items = [1, 2, 4, 5]
print(f"Starting: {items}")

items.insert(2, 3)
print(f"After insert(2, 3): {items}")

items.insert(0, 0)
print(f"After insert(0, 0): {items}")
print()

# ============================================================================
# EXAMPLE 8: Remove - Remove by Value
# ============================================================================
# Remove first occurrence

print("Example 8: Remove")
print("-" * 50)

items = [1, 2, 3, 4, 5, 3]
print(f"Starting: {items}")

items.remove(3)
print(f"After remove(3): {items}")

items.remove(1)
print(f"After remove(1): {items}")
print()

# ============================================================================
# EXAMPLE 9: Pop - Remove and Return
# ============================================================================
# Remove from end (or position)

print("Example 9: Pop")
print("-" * 50)

items = [1, 2, 3, 4, 5]
print(f"Starting: {items}")

last = items.pop()
print(f"Popped {last}, list: {items}")

first = items.pop(0)
print(f"Popped {first}, list: {items}")
print()

# ============================================================================
# EXAMPLE 10: Clear - Remove All
# ============================================================================
# Delete all items

print("Example 10: Clear")
print("-" * 50)

items = [1, 2, 3, 4, 5]
print(f"Starting: {items}")

items.clear()
print(f"After clear(): {items}")
print()

# ============================================================================
# EXAMPLE 11: Sort - Arrange Items
# ============================================================================
# Sort in place

print("Example 11: Sort")
print("-" * 50)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Starting: {numbers}")

numbers.sort()
print(f"After sort(): {numbers}")

words = ["cherry", "apple", "banana"]
print(f"Starting: {words}")
words.sort()
print(f"After sort(): {words}")
print()

# ============================================================================
# EXAMPLE 12: Sort Reverse
# ============================================================================
# Sort in reverse order

print("Example 12: Sort Reverse")
print("-" * 50)

numbers = [3, 1, 4, 1, 5]
print(f"Starting: {numbers}")

numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")
print()

# ============================================================================
# EXAMPLE 13: Reverse - Flip Order
# ============================================================================
# Reverse in place

print("Example 13: Reverse")
print("-" * 50)

items = [1, 2, 3, 4, 5]
print(f"Starting: {items}")

items.reverse()
print(f"After reverse(): {items}")
print()

# ============================================================================
# EXAMPLE 14: Count - Occurrences
# ============================================================================
# Count how many times item appears

print("Example 14: Count")
print("-" * 50)

items = [1, 2, 3, 2, 4, 2, 5]
print(f"List: {items}")

count = items.count(2)
print(f"Count of 2: {count}")

count = items.count(5)
print(f"Count of 5: {count}")

count = items.count(99)
print(f"Count of 99: {count}")
print()

# ============================================================================
# EXAMPLE 15: Index - Find Position
# ============================================================================
# Find position of item

print("Example 15: Index")
print("-" * 50)

items = ["apple", "banana", "cherry", "date"]
print(f"List: {items}")

pos = items.index("cherry")
print(f"Index of 'cherry': {pos}")

pos = items.index("apple")
print(f"Index of 'apple': {pos}")
print()

# ============================================================================
# EXAMPLE 16: Copy - Independent List
# ============================================================================
# Create copy to avoid unintended changes

print("Example 16: Copy")
print("-" * 50)

original = [1, 2, 3]
reference = original  # Points to same list
copy = original.copy()  # New independent list

print(f"Original: {original}")
print(f"Reference: {reference}")
print(f"Copy: {copy}")
print()

reference.append(4)
copy.append(99)

print(f"After reference.append(4):")
print(f"  Original: {original}")
print(f"  Reference: {reference}")
print()

print(f"After copy.append(99):")
print(f"  Original: {original}")
print(f"  Copy: {copy}")
print()

# ============================================================================
# EXAMPLE 17: Slice Copy
# ============================================================================
# Copy using slice notation

print("Example 17: Slice Copy")
print("-" * 50)

original = [1, 2, 3, 4, 5]
copy = original[:]  # Full slice creates copy

print(f"Original: {original}")
print(f"Copy: {copy}")

copy[0] = 99
print(f"After copy[0] = 99:")
print(f"  Original: {original}")
print(f"  Copy: {copy}")
print()

# ============================================================================
# EXAMPLE 18: List Comprehension - Transform
# ============================================================================
# Create new list from existing one

print("Example 18: List Comprehension")
print("-" * 50)

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print()

# ============================================================================
# EXAMPLE 19: List Comprehension - Filter
# ============================================================================
# Create list with only matching items

print("Example 19: Comprehension with Filter")
print("-" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]

print(f"Original: {numbers}")
print(f"Even numbers: {evens}")
print()

# ============================================================================
# EXAMPLE 20: Nested Lists - 2D Array
# ============================================================================
# List of lists

print("Example 20: Nested Lists")
print("-" * 50)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print()
print(f"matrix[0] = {matrix[0]}")
print(f"matrix[1][2] = {matrix[1][2]}")
print(f"matrix[2][0] = {matrix[2][0]}")
print()

# ============================================================================
# EXAMPLE 21: Find Maximum and Minimum
# ============================================================================
# Using built-in functions

print("Example 21: Max and Min")
print("-" * 50)

numbers = [45, 23, 89, 12, 56, 34]
print(f"Numbers: {numbers}")

print(f"max() = {max(numbers)}")
print(f"min() = {min(numbers)}")
print(f"sum() = {sum(numbers)}")
print(f"len() = {len(numbers)}")
print()

# ============================================================================
# EXAMPLE 22: Sum and Average
# ============================================================================
# Calculate statistics

print("Example 22: Sum and Average")
print("-" * 50)

grades = [85, 92, 78, 95, 88]
total = sum(grades)
average = total / len(grades)

print(f"Grades: {grades}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
print()

# ============================================================================
# EXAMPLE 23: Swapping Elements
# ============================================================================
# Exchange two elements

print("Example 23: Swap")
print("-" * 50)

items = [1, 2, 3, 4, 5]
print(f"Starting: {items}")

items[0], items[4] = items[4], items[0]
print(f"After swap [0] and [4]: {items}")
print()

# ============================================================================
# EXAMPLE 24: Building List from Input
# ============================================================================
# Collect items into list

print("Example 24: Build from Input")
print("-" * 50)

items = []
print("Enter 3 numbers (or skip):")

for i in range(3):
    try:
        num = int(input(f"  Number {i+1}: "))
        items.append(num)
    except ValueError:
        print("  Skipped")

print(f"Collected: {items}")
if items:
    print(f"Sum: {sum(items)}")
print()

# ============================================================================
# EXAMPLE 25: Zip - Combine Lists
# ============================================================================
# Pair up items from multiple lists

print("Example 25: Zip Lists")
print("-" * 50)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"Names: {names}")
print(f"Scores: {scores}")
print()

print("Zipped together:")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

