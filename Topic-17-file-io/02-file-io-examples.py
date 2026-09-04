# Topic 17: File I/O - Elaborate Examples
# Comprehensive examples of reading and writing files

import os
import json
import csv
from datetime import datetime

# ============================================================================
# EXAMPLE 1: Create and Write to File
# ============================================================================
# Write text to file

print("Example 1: Write to File")
print("-" * 50)

# Write using with statement
with open("example1.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a file.\n")
    f.write("We're learning file I/O!\n")

print("File created: example1.txt")
print()

# ============================================================================
# EXAMPLE 2: Read Entire File
# ============================================================================
# Read all content at once

print("Example 2: Read Entire File")
print("-" * 50)

with open("example1.txt", "r") as f:
    content = f.read()

print("File content:")
print(content)
print()

# ============================================================================
# EXAMPLE 3: Read Lines One at a Time
# ============================================================================
# Process line by line

print("Example 3: Read Line by Line")
print("-" * 50)

with open("example1.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()

print(f"Line 1: {line1.strip()}")
print(f"Line 2: {line2.strip()}")
print()

# ============================================================================
# EXAMPLE 4: Read All Lines into List
# ============================================================================
# Read all lines at once

print("Example 4: Read All Lines")
print("-" * 50)

with open("example1.txt", "r") as f:
    lines = f.readlines()

print(f"Number of lines: {len(lines)}")
for i, line in enumerate(lines, 1):
    print(f"  {i}: {line.strip()}")
print()

# ============================================================================
# EXAMPLE 5: Loop Through Lines
# ============================================================================
# Iterate over file

print("Example 5: Loop Through File")
print("-" * 50)

with open("example1.txt", "r") as f:
    for line in f:
        print(f"  {line.strip()}")
print()

# ============================================================================
# EXAMPLE 6: Write List of Names
# ============================================================================
# Write multiple items

print("Example 6: Write List")
print("-" * 50)

names = ["Alice", "Bob", "Charlie", "Diana"]

with open("names.txt", "w") as f:
    for name in names:
        f.write(f"{name}\n")

print("Wrote names to names.txt")
print()

# ============================================================================
# EXAMPLE 7: Append to Existing File
# ============================================================================
# Add to end without overwriting

print("Example 7: Append to File")
print("-" * 50)

# File has: Alice, Bob, Charlie, Diana
with open("names.txt", "a") as f:
    f.write("Eve\n")
    f.write("Frank\n")

print("Appended 2 more names")

# Verify by reading
with open("names.txt", "r") as f:
    for line in f:
        print(f"  {line.strip()}")
print()

# ============================================================================
# EXAMPLE 8: Parse Delimited Data
# ============================================================================
# Read and split structured data

print("Example 8: Parse Delimited Data")
print("-" * 50)

# Create grades file
grades_data = "alice 85 92 78\nbob 90 88 95\ncharlie 77 81 79"
with open("grades.txt", "w") as f:
    f.write(grades_data)

# Read and parse
with open("grades.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        name = parts[0]
        scores = [int(x) for x in parts[1:]]
        average = sum(scores) / len(scores)
        print(f"  {name}: avg={average:.1f}")
print()

# ============================================================================
# EXAMPLE 9: Write Dictionaries as JSON
# ============================================================================
# Save structured data

print("Example 9: Write JSON")
print("-" * 50)

users = [
    {"name": "Alice", "age": 30, "city": "Boston"},
    {"name": "Bob", "age": 25, "city": "NYC"},
    {"name": "Charlie", "age": 28, "city": "LA"}
]

with open("users.json", "w") as f:
    json.dump(users, f, indent=2)

print("Wrote users.json")
print()

# ============================================================================
# EXAMPLE 10: Read JSON File
# ============================================================================
# Load and use JSON data

print("Example 10: Read JSON")
print("-" * 50)

with open("users.json", "r") as f:
    data = json.load(f)

print("Loaded users:")
for user in data:
    print(f"  {user['name']}: {user['age']}, {user['city']}")
print()

# ============================================================================
# EXAMPLE 11: Write CSV File
# ============================================================================
# Create CSV with csv module

print("Example 11: Write CSV")
print("-" * 50)

headers = ["Name", "Age", "City"]
rows = [
    ["Alice", "30", "Boston"],
    ["Bob", "25", "NYC"],
    ["Charlie", "28", "LA"]
]

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print("Wrote users.csv")
print()

# ============================================================================
# EXAMPLE 12: Read CSV File
# ============================================================================
# Read and process CSV

print("Example 12: Read CSV")
print("-" * 50)

with open("users.csv", "r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        print(f"  {row[0]}: {row[1]} years old")
print()

# ============================================================================
# EXAMPLE 13: Check if File Exists
# ============================================================================
# Safe file operations

print("Example 13: Check File Exists")
print("-" * 50)

if os.path.exists("users.json"):
    print("users.json exists")
else:
    print("users.json not found")

if os.path.exists("notfound.txt"):
    print("notfound.txt exists")
else:
    print("notfound.txt does not exist")
print()

# ============================================================================
# EXAMPLE 14: Get File Info
# ============================================================================
# File size and modification time

print("Example 14: File Information")
print("-" * 50)

if os.path.exists("users.json"):
    size = os.path.getsize("users.json")
    print(f"File size: {size} bytes")
    
    mod_time = os.path.getmtime("users.json")
    mod_date = datetime.fromtimestamp(mod_time)
    print(f"Modified: {mod_date}")
print()

# ============================================================================
# EXAMPLE 15: List Files in Directory
# ============================================================================
# Get files in current directory

print("Example 15: List Files")
print("-" * 50)

files = os.listdir(".")
txt_files = [f for f in files if f.endswith(".txt") or f.endswith(".json") or f.endswith(".csv")]
print(f"Created files in this demo: {txt_files[:5]}")  # Show first 5
print()

# ============================================================================
# EXAMPLE 16: Read File with Error Handling
# ============================================================================
# Handle file not found

print("Example 16: Error Handling")
print("-" * 50)

try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"Error reading file: {e}")
print()

# ============================================================================
# EXAMPLE 17: Process Large File Line by Line
# ============================================================================
# Efficient processing of large files

print("Example 17: Process Large File")
print("-" * 50)

# Create sample file with numbers
with open("numbers.txt", "w") as f:
    for i in range(100):
        f.write(f"{i * 10}\n")

# Process line by line (efficient)
total = 0
count = 0
with open("numbers.txt", "r") as f:
    for line in f:
        total += int(line.strip())
        count += 1

print(f"Read {count} numbers, total: {total}")
print()

# ============================================================================
# EXAMPLE 18: Read and Modify File
# ============================================================================
# Read, process, write back

print("Example 18: Read and Modify")
print("-" * 50)

# Create original file
with open("numbers.txt", "r") as f:
    lines = f.readlines()

# Double all numbers
with open("numbers_doubled.txt", "w") as f:
    for line in lines:
        num = int(line.strip())
        f.write(f"{num * 2}\n")

# Show first few
with open("numbers_doubled.txt", "r") as f:
    for i, line in enumerate(f):
        if i < 3:
            print(f"  {line.strip()}")
print()

# ============================================================================
# EXAMPLE 19: Append to Log File
# ============================================================================
# Common pattern for logging

print("Example 19: Logging to File")
print("-" * 50)

# Simulate logging events
events = [
    "User logged in",
    "User clicked button",
    "User downloaded file",
    "User logged out"
]

with open("app.log", "a") as f:
    for event in events:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {event}\n")

print("Events logged to app.log")

# Show log
with open("app.log", "r") as f:
    for line in f:
        print(f"  {line.strip()}")
print()

# ============================================================================
# EXAMPLE 20: Read Configuration File
# ============================================================================
# Parse simple config format

print("Example 20: Config File")
print("-" * 50)

# Create config file
config_content = """debug=True
host=localhost
port=8000
max_connections=100
"""

with open("config.txt", "w") as f:
    f.write(config_content)

# Parse config
config = {}
with open("config.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=")
            config[key.strip()] = value.strip()

print("Configuration loaded:")
for key, value in config.items():
    print(f"  {key}: {value}")
print()

# ============================================================================
# EXAMPLE 21: Write Multiple Formats
# ============================================================================
# Save same data in different formats

print("Example 21: Multiple Formats")
print("-" * 50)

data = {
    "students": [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92}
    ]
}

# Save as JSON
with open("data.json", "w") as f:
    json.dump(data, f)
print("Saved as JSON")

# Save as CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Grade"])
    for student in data["students"]:
        writer.writerow([student["name"], student["grade"]])
print("Saved as CSV")

# Save as text
with open("data.txt", "w") as f:
    for student in data["students"]:
        f.write(f"{student['name']}: {student['grade']}\n")
print("Saved as text")
print()

# ============================================================================
# EXAMPLE 22: Read Lines and Count
# ============================================================================
# Process and count

print("Example 22: Count and Process")
print("-" * 50)

with open("names.txt", "r") as f:
    names = [line.strip() for line in f]

print(f"Total names: {len(names)}")
print(f"Names starting with vowels: {sum(1 for n in names if n[0].lower() in 'aeiou')}")
print(f"Names starting with consonants: {sum(1 for n in names if n[0].lower() not in 'aeiou')}")
print()

# ============================================================================
# EXAMPLE 23: File Backup Pattern
# ============================================================================
# Backup before overwriting

print("Example 23: Backup Pattern")
print("-" * 50)

# Create original
with open("important.txt", "w") as f:
    f.write("Important data v1")

print("Created important.txt")

# Before overwriting, back up
if os.path.exists("important.txt"):
    os.rename("important.txt", "important.txt.bak")
    print("Backed up to important.txt.bak")

# Write new version
with open("important.txt", "w") as f:
    f.write("Important data v2")
print("Wrote new version")

# Show both exist
if os.path.exists("important.txt.bak"):
    print("Backup file exists")
print()

# ============================================================================
# EXAMPLE 24: Read JSON with Default
# ============================================================================
# Safe JSON loading

print("Example 24: Safe JSON Loading")
print("-" * 50)

def load_settings(filename, defaults):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found, using defaults")
        return defaults

defaults = {"theme": "light", "language": "en"}
settings = load_settings("settings.json", defaults)
print(f"Settings: {settings}")
print()

# ============================================================================
# EXAMPLE 25: Streaming Processing
# ============================================================================
# Process line by line without loading all

print("Example 25: Streaming Processing")
print("-" * 50)

# Create large-ish file
with open("large_data.txt", "w") as f:
    for i in range(1000):
        f.write(f"Line {i}: {i * 10}\n")

# Process streaming (doesn't load all into memory)
sum_values = 0
line_count = 0
with open("large_data.txt", "r") as f:
    for line in f:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            value = int(parts[1])
            sum_values += value
            line_count += 1

print(f"Processed {line_count} lines")
print(f"Sum of values: {sum_values}")

# Clean up example files
print("\nCleaning up example files...")
for filename in ["example1.txt", "names.txt", "grades.txt", "users.json", 
                  "users.csv", "numbers.txt", "numbers_doubled.txt", "app.log",
                  "config.txt", "data.json", "data.csv", "data.txt", 
                  "important.txt", "important.txt.bak", "large_data.txt"]:
    if os.path.exists(filename):
        os.remove(filename)
print("Cleanup complete")

