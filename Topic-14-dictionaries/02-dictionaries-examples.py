# Topic 14: Dictionaries - Elaborate Examples
# Comprehensive examples of creating and using dictionaries

# ============================================================================
# EXAMPLE 1: Creating Dictionaries - Literal Syntax
# ============================================================================
# Create dictionaries using curly braces

print("Example 1: Creating Dictionaries")
print("-" * 50)

person = {"name": "Alice", "age": 30, "city": "Boston"}
print(f"Person: {person}")

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(f"Grades: {grades}")

empty = {}
print(f"Empty: {empty}")
print()

# ============================================================================
# EXAMPLE 2: Creating with dict() Constructor
# ============================================================================
# Alternative way using dict()

print("Example 2: dict() Constructor")
print("-" * 50)

person = dict(name="Alice", age=30, city="Boston")
print(f"Person: {person}")

person2 = dict([("name", "Bob"), ("age", 25)])
print(f"Person2: {person2}")
print()

# ============================================================================
# EXAMPLE 3: Accessing Values by Key
# ============================================================================
# Get values using key

print("Example 3: Accessing Values")
print("-" * 50)

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(f"Dictionary: {grades}")
print()

print(f"grades['Alice'] = {grades['Alice']}")
print(f"grades['Bob'] = {grades['Bob']}")
print(f"grades['Charlie'] = {grades['Charlie']}")
print()

# ============================================================================
# EXAMPLE 4: Safe Access with get()
# ============================================================================
# Avoid KeyError with get()

print("Example 4: Safe Access with get()")
print("-" * 50)

grades = {"Alice": 85, "Bob": 92}
print(f"Dictionary: {grades}")
print()

# Direct access (risky)
try:
    print(f"grades['Unknown'] = {grades['Unknown']}")
except KeyError:
    print("KeyError: Key doesn't exist!")

print()

# Safe access
print(f"grades.get('Alice') = {grades.get('Alice')}")
print(f"grades.get('Unknown') = {grades.get('Unknown')}")
print(f"grades.get('Unknown', 0) = {grades.get('Unknown', 0)}")
print()

# ============================================================================
# EXAMPLE 5: Adding and Modifying Entries
# ============================================================================
# Add or change values

print("Example 5: Adding and Modifying")
print("-" * 50)

person = {"name": "Alice", "age": 30}
print(f"Start: {person}")

person["city"] = "Boston"
print(f"After adding city: {person}")

person["age"] = 31
print(f"After changing age: {person}")

person["job"] = "Engineer"
print(f"After adding job: {person}")
print()

# ============================================================================
# EXAMPLE 6: Removing Entries - del
# ============================================================================
# Delete entries with del

print("Example 6: Removing with del")
print("-" * 50)

person = {"name": "Alice", "age": 30, "city": "Boston"}
print(f"Start: {person}")

del person["city"]
print(f"After del person['city']: {person}")

del person["age"]
print(f"After del person['age']: {person}")
print()

# ============================================================================
# EXAMPLE 7: Removing with pop()
# ============================================================================
# Remove and get value

print("Example 7: Removing with pop()")
print("-" * 50)

person = {"name": "Alice", "age": 30, "city": "Boston"}
print(f"Start: {person}")

city = person.pop("city")
print(f"Popped city: {city}")
print(f"Dictionary now: {person}")

age = person.pop("age")
print(f"Popped age: {age}")
print(f"Dictionary now: {person}")
print()

# ============================================================================
# EXAMPLE 8: Clear - Remove All
# ============================================================================
# Delete all entries

print("Example 8: Clear All")
print("-" * 50)

person = {"name": "Alice", "age": 30, "city": "Boston"}
print(f"Start: {person}")

person.clear()
print(f"After clear(): {person}")
print()

# ============================================================================
# EXAMPLE 9: Check Membership
# ============================================================================
# Check if key exists

print("Example 9: Membership Check")
print("-" * 50)

person = {"name": "Alice", "age": 30, "city": "Boston"}
print(f"Dictionary: {person}")
print()

print(f"'name' in person = {'name' in person}")
print(f"'job' in person = {'job' in person}")
print(f"'age' not in person = {'age' not in person}")
print()

# ============================================================================
# EXAMPLE 10: Dictionary Keys
# ============================================================================
# Get all keys

print("Example 10: Keys")
print("-" * 50)

person = {"name": "Alice", "age": 30, "city": "Boston"}
print(f"Dictionary: {person}")
print()

keys = person.keys()
print(f"person.keys() = {keys}")
print(f"list(person.keys()) = {list(person.keys())}")
print()

# ============================================================================
# EXAMPLE 11: Dictionary Values
# ============================================================================
# Get all values

print("Example 11: Values")
print("-" * 50)

person = {"name": "Alice", "age": 30, "city": "Boston"}
print(f"Dictionary: {person}")
print()

values = person.values()
print(f"person.values() = {values}")
print(f"list(person.values()) = {list(person.values())}")
print()

# ============================================================================
# EXAMPLE 12: Dictionary Items
# ============================================================================
# Get key-value pairs

print("Example 12: Items")
print("-" * 50)

person = {"name": "Alice", "age": 30, "city": "Boston"}
print(f"Dictionary: {person}")
print()

items = person.items()
print(f"person.items() = {items}")
print(f"list(person.items()) = {list(person.items())}")
print()

# ============================================================================
# EXAMPLE 13: Loop Over Keys
# ============================================================================
# Iterate over keys

print("Example 13: Loop Over Keys")
print("-" * 50)

person = {"name": "Alice", "age": 30, "city": "Boston"}
print(f"Dictionary: {person}")
print()

print("Looping over keys:")
for key in person:
    print(f"  {key}")
print()

# ============================================================================
# EXAMPLE 14: Loop Over Values
# ============================================================================
# Iterate over values

print("Example 14: Loop Over Values")
print("-" * 50)

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(f"Dictionary: {grades}")
print()

print("Looping over values:")
for value in grades.values():
    print(f"  {value}")
print()

# ============================================================================
# EXAMPLE 15: Loop Over Items
# ============================================================================
# Iterate over key-value pairs

print("Example 15: Loop Over Items")
print("-" * 50)

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(f"Dictionary: {grades}")
print()

print("Looping over items:")
for name, grade in grades.items():
    print(f"  {name}: {grade}")
print()

# ============================================================================
# EXAMPLE 16: Update Dictionary
# ============================================================================
# Update multiple entries at once

print("Example 16: Update")
print("-" * 50)

person = {"name": "Alice", "age": 30}
print(f"Start: {person}")

person.update({"age": 31, "city": "Boston"})
print(f"After update: {person}")

person.update({"job": "Engineer", "salary": 100000})
print(f"After another update: {person}")
print()

# ============================================================================
# EXAMPLE 17: Nested Dictionaries
# ============================================================================
# Dictionary containing dictionaries

print("Example 17: Nested Dictionaries")
print("-" * 50)

students = {
    "Alice": {"age": 18, "gpa": 3.9},
    "Bob": {"age": 19, "gpa": 3.7},
    "Charlie": {"age": 18, "gpa": 3.5}
}

print(f"students['Alice'] = {students['Alice']}")
print(f"students['Alice']['gpa'] = {students['Alice']['gpa']}")
print(f"students['Bob']['age'] = {students['Bob']['age']}")
print()

# ============================================================================
# EXAMPLE 18: Nested Dictionary Operations
# ============================================================================
# Modify nested values

print("Example 18: Modify Nested")
print("-" * 50)

inventory = {
    "apple": {"price": 1.50, "stock": 100},
    "milk": {"price": 3.00, "stock": 50}
}

print(f"Start: {inventory}")
print()

inventory["apple"]["stock"] -= 10
print(f"After selling 10 apples: {inventory}")

inventory["apple"]["price"] = 1.75
print(f"After price increase: {inventory}")
print()

# ============================================================================
# EXAMPLE 19: Dictionary Comprehension
# ============================================================================
# Create dictionary concisely

print("Example 19: Dictionary Comprehension")
print("-" * 50)

# Square numbers
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Even numbers only
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {evens}")

# Transform existing dictionary
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v*2 for k, v in original.items()}
print(f"Doubled: {doubled}")
print()

# ============================================================================
# EXAMPLE 20: Counting with Dictionary
# ============================================================================
# Count occurrences pattern

print("Example 20: Counting")
print("-" * 50)

text = "mississippi"
counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

print(f"Text: {text}")
print(f"Counts: {counts}")
print()

# ============================================================================
# EXAMPLE 21: Dictionary from Lists
# ============================================================================
# Create dict from paired lists

print("Example 21: From Lists")
print("-" * 50)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

grades = {}
for name, score in zip(names, scores):
    grades[name] = score

print(f"Names: {names}")
print(f"Scores: {scores}")
print(f"Grades dict: {grades}")
print()

# ============================================================================
# EXAMPLE 22: Length of Dictionary
# ============================================================================
# Number of key-value pairs

print("Example 22: Length")
print("-" * 50)

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(f"Dictionary: {grades}")
print(f"len(grades) = {len(grades)}")

grades["Diana"] = 95
print(f"After adding Diana: {grades}")
print(f"len(grades) = {len(grades)}")
print()

# ============================================================================
# EXAMPLE 23: Dictionary Sorting
# ============================================================================
# Sort dictionary by keys or values

print("Example 23: Sorting")
print("-" * 50)

grades = {"Charlie": 78, "Alice": 85, "Bob": 92}
print(f"Original: {grades}")
print()

# Sort by keys
sorted_keys = sorted(grades.keys())
print(f"Sorted by keys: {sorted_keys}")

# Sort by values
sorted_by_values = sorted(grades.items(), key=lambda x: x[1])
print(f"Sorted by values: {sorted_by_values}")
print()

# ============================================================================
# EXAMPLE 24: Grouping Items
# ============================================================================
# Group items by category

print("Example 24: Grouping")
print("-" * 50)

students = [
    {"name": "Alice", "grade": 9},
    {"name": "Bob", "grade": 10},
    {"name": "Charlie", "grade": 9},
    {"name": "Diana", "grade": 10}
]

by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

print("By grade:")
for grade, names in sorted(by_grade.items()):
    print(f"  Grade {grade}: {names}")
print()

# ============================================================================
# EXAMPLE 25: Configuration Dictionary
# ============================================================================
# Real-world config pattern

print("Example 25: Configuration")
print("-" * 50)

config = {
    "debug": True,
    "host": "localhost",
    "port": 8000,
    "database": "app.db",
    "max_connections": 100,
    "timeout": 30
}

print("Configuration:")
for key, value in config.items():
    print(f"  {key}: {value}")

# Access and use
print(f"\nServer: {config['host']}:{config['port']}")
print(f"Database: {config['database']}")
if config["debug"]:
    print("Debug mode enabled")

