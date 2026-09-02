# Topic 4: Strings - Elaborate Examples
# Each example demonstrates real string operations and methods

# ============================================================================
# EXAMPLE 1: String Indexing - Accessing Individual Characters
# ============================================================================
# Strings are sequences, so you can access characters by position
# Remember: indexing starts at 0

print("Example 1: String Indexing")
print("-" * 50)

text = "Python"
print(f"Text: '{text}'")
print(f"Length: {len(text)} characters")
print()
print("Forward indexing:")
print(f"  Position 0: '{text[0]}'  (1st character)")
print(f"  Position 1: '{text[1]}'  (2nd character)")
print(f"  Position 2: '{text[2]}'  (3rd character)")
print(f"  Position 5: '{text[5]}'  (last character)")
print()
print("Negative indexing (counting from end):")
print(f"  Position -1: '{text[-1]}'  (last character)")
print(f"  Position -2: '{text[-2]}'  (2nd to last)")
print(f"  Position -6: '{text[-6]}'  (first character)")
print()

# ============================================================================
# EXAMPLE 2: String Slicing - Extracting Substrings
# ============================================================================
# Slicing extracts a portion of a string

print("Example 2: String Slicing")
print("-" * 50)

text = "Hello World"
print(f"Text: '{text}'")
print()
print("Various slices:")
print(f"  text[0:5]   = '{text[0:5]}'   (characters at positions 0-4)")
print(f"  text[6:11]  = '{text[6:11]}'  (characters at positions 6-10)")
print(f"  text[:5]    = '{text[:5]}'    (start to position 4)")
print(f"  text[6:]    = '{text[6:]}'    (position 6 to end)")
print(f"  text[:]     = '{text[:]}'     (entire string)")
print(f"  text[::2]   = '{text[::2]}'   (every 2nd character)")
print(f"  text[::-1]  = '{text[::-1]}'  (reversed)")
print()

# ============================================================================
# EXAMPLE 3: String Upper and Lower Methods
# ============================================================================
# Convert strings to different cases

print("Example 3: Case Conversion Methods")
print("-" * 50)

text = "Hello World"
print(f"Original: '{text}'")
print(f"Upper:    '{text.upper()}'")
print(f"Lower:    '{text.lower()}'")
print(f"Capitalize: '{text.capitalize()}'")
print(f"Title:    '{text.title()}'")
print()

# Real-world use: case-insensitive comparison
user_input = "HELLO"
if user_input.lower() == "hello":
    print(f"✓ User entered 'hello' (matching case-insensitive)")
print()

# ============================================================================
# EXAMPLE 4: String Replace Method
# ============================================================================
# Replace parts of strings

print("Example 4: String Replace Method")
print("-" * 50)

text = "Hello World"
print(f"Original: '{text}'")
print(f"Replace 'World' with 'Python': '{text.replace('World', 'Python')}'")
print(f"Replace 'l' with 'L': '{text.replace('l', 'L')}'")
print(f"Replace all 'l' (not just first): '{text.replace('l', 'L')}'")
print()

# Real-world: sanitize user input
email = "User@EXAMPLE.COM"
clean_email = email.lower().strip()  # Lowercase and remove spaces
print(f"Cleaned email: '{clean_email}'")
print()

# ============================================================================
# EXAMPLE 5: String Strip Method - Remove Spaces
# ============================================================================
# Remove leading and trailing whitespace

print("Example 5: String Strip Method")
print("-" * 50)

text_with_spaces = "   Hello World   "
print(f"Original: '{text_with_spaces}'")
print(f"strip():  '{text_with_spaces.strip()}'")
print(f"lstrip(): '{text_with_spaces.lstrip()}'  (remove left only)")
print(f"rstrip(): '{text_with_spaces.rstrip()}'  (remove right only)")
print()

# Real-world: clean user input
user_input = "   John Doe   "
cleaned = user_input.strip()
print(f"User input: '{user_input}'")
print(f"Cleaned: '{cleaned}'")
print()

# ============================================================================
# EXAMPLE 6: String Split Method - Break Into Words
# ============================================================================
# Split a string into a list of substrings

print("Example 6: String Split Method")
print("-" * 50)

text = "apple banana cherry"
words = text.split()
print(f"Text: '{text}'")
print(f"Split result: {words}")
print(f"First word: '{words[0]}'")
print(f"Second word: '{words[1]}'")
print()

# Split with specific delimiter
csv_data = "Alice,25,Engineer"
fields = csv_data.split(",")
print(f"CSV: '{csv_data}'")
print(f"Split by comma: {fields}")
print(f"Name: {fields[0]}, Age: {fields[1]}, Job: {fields[2]}")
print()

# ============================================================================
# EXAMPLE 7: String Join Method - Combine Into String
# ============================================================================
# Join a list of strings into one string

print("Example 7: String Join Method")
print("-" * 50)

words = ["apple", "banana", "cherry"]
print(f"Words list: {words}")
print()
print(f"With space: '{' '.join(words)}'")
print(f"With dash: '{'-'.join(words)}'")
print(f"With comma+space: '{', '.join(words)}'")
print(f"No separator: '{'' .join(words)}'")
print()

# Real-world: create CSV output
data = ["Alice", "25", "Engineer", "New York"]
csv_line = ",".join(data)
print(f"Data: {data}")
print(f"CSV: {csv_line}")
print()

# ============================================================================
# EXAMPLE 8: Substring Search - In Operator
# ============================================================================
# Check if substring exists in string

print("Example 8: Substring Search (In Operator)")
print("-" * 50)

email = "john@example.com"
print(f"Email: {email}")
print(f"Contains '@'? {'@' in email}")
print(f"Contains '.'? {'.' in email}")
print(f"Contains 'example'? {'example' in email}")
print()

# Real-world: validate email
if "@" in email and "." in email:
    print("✓ Email format looks valid (contains @ and .)")
else:
    print("✗ Email format invalid")
print()

# ============================================================================
# EXAMPLE 9: String Find Method - Locate Substring Position
# ============================================================================
# Find where a substring starts

print("Example 9: String Find Method")
print("-" * 50)

text = "Hello World Hello"
print(f"Text: '{text}'")
print(f"Find 'World': position {text.find('World')}")
print(f"Find 'Hello': position {text.find('Hello')}  (first occurrence)")
print(f"Find 'xyz': position {text.find('xyz')}  (not found returns -1)")
print()

# Real-world: extract domain from email
email = "john@example.com"
at_pos = email.find("@")
domain = email[at_pos+1:]
print(f"Email: {email}")
print(f"@ position: {at_pos}")
print(f"Domain: {domain}")
print()

# ============================================================================
# EXAMPLE 10: String Startswith and Endswith
# ============================================================================
# Check beginning and ending of strings

print("Example 10: Startswith and Endswith Methods")
print("-" * 50)

filename = "document.txt"
print(f"Filename: {filename}")
print(f"Starts with 'document'? {filename.startswith('document')}")
print(f"Ends with '.txt'? {filename.endswith('.txt')}")
print(f"Ends with '.pdf'? {filename.endswith('.pdf')}")
print()

# Real-world: file validation
image_formats = [".jpg", ".png", ".gif"]
file_to_check = "photo.jpg"
is_image = any(file_to_check.endswith(fmt) for fmt in image_formats)
print(f"File: {file_to_check}")
print(f"Is image format? {is_image}")
print()

# ============================================================================
# EXAMPLE 11: String Concatenation with +
# ============================================================================
# Join strings together

print("Example 11: String Concatenation")
print("-" * 50)

first = "John"
middle = "Robert"
last = "Smith"

full_name = first + " " + middle + " " + last
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")
print(f"Full name: {full_name}")
print()

# Building sentences
greeting = "Hello, " + first + "!"
print(f"Greeting: {greeting}")
print()

# ============================================================================
# EXAMPLE 12: F-String Formatting (Modern Python)
# ============================================================================
# Embed variables in strings

print("Example 12: F-String Formatting")
print("-" * 50)

name = "Alice"
age = 28
city = "Boston"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Profile: {name} is {age} years old and lives in {city}")
print()

# With expressions
price = 19.99
quantity = 3
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${price * quantity}")
print()

# With formatting
pi = 3.14159265
print(f"Pi: {pi}")
print(f"Pi rounded: {pi:.2f}")  # Two decimal places
print()

# ============================================================================
# EXAMPLE 13: Multiple Replace Operations
# ============================================================================
# Chain multiple replacements

print("Example 13: Multiple Replacements")
print("-" * 50)

text = "Hello World Hello Python"
print(f"Original: '{text}'")

# Replace one at a time
step1 = text.replace("Hello", "Hi")
print(f"Step 1: '{step1}'")

step2 = step1.replace("World", "Universe")
print(f"Step 2: '{step2}'")

step3 = step2.replace("Python", "Code")
print(f"Step 3: '{step3}'")
print()

# ============================================================================
# EXAMPLE 14: String Length - len() Function
# ============================================================================
# Get the number of characters in a string

print("Example 14: String Length")
print("-" * 50)

texts = ["a", "hello", "hello world", ""]
for text in texts:
    print(f"'{text}' has {len(text)} characters")
print()

# Real-world: password strength
password = "MySecurePass123"
print(f"Password: {password}")
print(f"Length: {len(password)}")
if len(password) >= 8:
    print("✓ Password length is sufficient")
else:
    print("✗ Password too short")
print()

# ============================================================================
# EXAMPLE 15: Character Presence Check - Count Method
# ============================================================================
# Count how many times a character appears

print("Example 15: String Count Method")
print("-" * 50)

text = "mississippi"
print(f"Text: '{text}'")
print(f"Letter 's' appears: {text.count('s')} times")
print(f"Letter 'i' appears: {text.count('i')} times")
print(f"Letter 'p' appears: {text.count('p')} times")
print()

# Real-world: validate word in text
word_to_find = "he"
text_to_search = "the theater"
occurrences = text_to_search.count(word_to_find)
print(f"'{word_to_find}' appears {occurrences} times in '{text_to_search}'")
print()

# ============================================================================
# EXAMPLE 16: Case-Insensitive String Comparison
# ============================================================================
# Compare strings ignoring case

print("Example 16: Case-Insensitive Comparison")
print("-" * 50)

user_input = "HELLO"
expected = "hello"
print(f"User input: '{user_input}'")
print(f"Expected: '{expected}'")
print(f"Are they equal? {user_input == expected}")
print(f"Equal (case-insensitive)? {user_input.lower() == expected.lower()}")
print()

# ============================================================================
# EXAMPLE 17: String Index Out of Range
# ============================================================================
# Accessing invalid indices

print("Example 17: Index Out of Range Behavior")
print("-" * 50)

text = "Hello"
print(f"Text: '{text}' (length: {len(text)})")
print(f"Valid indices: 0, 1, 2, 3, 4 (and -1, -2, -3, -4, -5)")
print(f"text[0] = '{text[0]}'")
print(f"text[4] = '{text[4]}'")
print(f"text[-1] = '{text[-1]}'")
print()

# Slicing is forgiving (doesn't raise error)
print("Slicing beyond limits (safe):")
print(f"text[0:100] = '{text[0:100]}'  (Returns what exists)")
print(f"text[50:60] = '{text[50:60]}'   (Returns empty string)")
print()

# ============================================================================
# EXAMPLE 18: Title Case and Other Methods
# ============================================================================
# Various string formatting methods

print("Example 18: Title Case and Other Methods")
print("-" * 50)

text = "the quick brown fox"
print(f"Original: '{text}'")
print(f"title(): '{text.title()}'  (Each word capitalized)")
print(f"upper(): '{text.upper()}'  (All uppercase)")
print(f"lower(): '{text.lower()}'  (All lowercase)")
print(f"capitalize(): '{text.capitalize()}'  (First letter only)")
print()

# ============================================================================
# EXAMPLE 19: Escape Sequences - Special Characters
# ============================================================================
# How to include special characters in strings

print("Example 19: Escape Sequences")
print("-" * 50)

print("Newline (\\n):")
print("Line 1\nLine 2\nLine 3")
print()

print("Tab (\\t):")
print("Name\tAge\tCity")
print("Alice\t25\tBoston")
print("Bob\t30\tNew York")
print()

print("Backslash (\\\\):")
path = "C:\\Users\\Documents\\file.txt"
print(f"Path: {path}")
print()

print("Quotes:")
print("She said \"Hello\"")
print('He said "Hello"')
print()

# ============================================================================
# EXAMPLE 20: isdigit, isalpha, isalnum Methods
# ============================================================================
# Check character types

print("Example 20: Character Type Checking")
print("-" * 50)

test_strings = ["123", "abc", "abc123", "12.5", "password!", ""]
print("Testing various strings:")
for s in test_strings:
    print(f"  '{s}':")
    print(f"    isdigit(): {s.isdigit()}  (all digits?)")
    print(f"    isalpha(): {s.isalpha()}  (all letters?)")
    print(f"    isalnum(): {s.isalnum()}  (letters/digits only?)")
print()

# Real-world: password validation
password = "pass123"
print(f"Password: '{password}'")
if password.isalnum():
    print("✓ No special characters")
else:
    print("Has special characters")
print()

# ============================================================================
# EXAMPLE 21: String Iteration (Loop Through Characters)
# ============================================================================
# Process each character

print("Example 21: String Iteration")
print("-" * 50)

text = "Hello"
print(f"Text: '{text}'")
print("Characters:")
for char in text:
    print(f"  '{char}'")
print()

# Build new string character by character
result = ""
for char in "abc":
    result = result + char.upper()
print(f"Uppercase: '{result}'")
print()

# ============================================================================
# EXAMPLE 22: String Splitting and Processing
# ============================================================================
# Common pattern: split, process, rejoin

print("Example 22: Split, Process, Rejoin")
print("-" * 50)

sentence = "hello world python code"
words = sentence.split()
print(f"Original: '{sentence}'")
print(f"Words: {words}")

# Capitalize each word
capitalized_words = [word.capitalize() for word in words]
print(f"Capitalized: {capitalized_words}")

result = " ".join(capitalized_words)
print(f"Result: '{result}'")
print()

# ============================================================================
# EXAMPLE 23: Email Parsing
# ============================================================================
# Extract parts from email address

print("Example 23: Email Parsing")
print("-" * 50)

email = "john.doe@example.com"
print(f"Email: {email}")

# Split on @
parts = email.split("@")
username = parts[0]
domain = parts[1]

print(f"Username: {username}")
print(f"Domain: {domain}")

# Further split domain
domain_parts = domain.split(".")
print(f"Domain name: {domain_parts[0]}")
print(f"TLD: {domain_parts[1]}")
print()

# ============================================================================
# EXAMPLE 24: Text Censoring
# ============================================================================
# Replace unwanted words

print("Example 24: Text Censoring")
print("-" * 50)

text = "This is a bad word in a bad context"
print(f"Original: '{text}'")

censored = text.replace("bad", "[CENSORED]")
print(f"Censored: '{censored}'")
print()

# ============================================================================
# EXAMPLE 25: String Padding and Alignment
# ============================================================================
# Format strings with fixed width

print("Example 25: String Padding and Alignment")
print("-" * 50)

text = "Hello"
print(f"Original: '{text}'")
print(f"ljust(10): '{text.ljust(10)}'  (pad right)")
print(f"rjust(10): '{text.rjust(10)}'  (pad left)")
print(f"center(10): '{text.center(10)}'  (center)")
print()

# Real-world: formatted output table
print("Product Pricing Table:")
print("-" * 40)
products = [("Apple", 0.99), ("Banana", 0.59), ("Orange", 1.29)]
for name, price in products:
    print(f"{name.ljust(15)} ${price:>6.2f}")
print()

