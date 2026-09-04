# Topic 18: Error Handling - Elaborate Examples
# Comprehensive examples of try/except/finally and exception handling

# ============================================================================
# EXAMPLE 1: Basic Try/Except
# ============================================================================
# Catch an error and continue

print("Example 1: Basic Try/Except")
print("-" * 50)

try:
    number = int("abc")
except ValueError:
    print("Error: Not a valid number!")
    number = 0

print(f"Number: {number}")
print()

# ============================================================================
# EXAMPLE 2: Multiple Except Blocks
# ============================================================================
# Catch different error types differently

print("Example 2: Multiple Except Blocks")
print("-" * 50)

items = [1, 2, 3]

# Try accessing invalid index
try:
    print(items[10])
except IndexError:
    print("Error: Index out of range!")

# Try accessing invalid key
try:
    d = {"a": 1}
    print(d["b"])
except KeyError:
    print("Error: Key not found!")

# Try invalid arithmetic
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

print()

# ============================================================================
# EXAMPLE 3: Catching Exception Object
# ============================================================================
# Get error information

print("Example 3: Exception Information")
print("-" * 50)

try:
    lst = [1, 2, 3]
    value = lst[10]
except IndexError as e:
    print(f"Error occurred: {e}")
    print(f"Error type: {type(e).__name__}")

print()

# ============================================================================
# EXAMPLE 4: Finally Clause
# ============================================================================
# Code that always runs

print("Example 4: Finally Clause")
print("-" * 50)

try:
    f = open("temporary.txt", "w")
    f.write("test data")
except IOError as e:
    print(f"Error: {e}")
finally:
    print("Cleanup: Closing file")
    f.close()

print()

# ============================================================================
# EXAMPLE 5: Else Clause
# ============================================================================
# Code that runs only if no exception

print("Example 5: Else Clause")
print("-" * 50)

try:
    number = int("123")
except ValueError:
    print("Not a number!")
else:
    print(f"Successfully converted: {number}")
    print(f"Number squared: {number ** 2}")

print()

# ============================================================================
# EXAMPLE 6: Try/Except/Else/Finally Combined
# ============================================================================
# All four together

print("Example 6: Complete Try/Except/Else/Finally")
print("-" * 50)

try:
    user_input = "42"
    number = int(user_input)
except ValueError:
    print("Failed to convert")
else:
    print(f"Success: converted to {number}")
finally:
    print("Conversion attempt complete")

print()

# ============================================================================
# EXAMPLE 7: Raising Exceptions
# ============================================================================
# Throw exceptions intentionally

print("Example 7: Raising Exceptions")
print("-" * 50)

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

try:
    age = validate_age(25)
    print(f"Valid age: {age}")
except ValueError as e:
    print(f"Invalid: {e}")

try:
    age = validate_age(-5)
except ValueError as e:
    print(f"Invalid: {e}")

print()

# ============================================================================
# EXAMPLE 8: Custom Exceptions
# ============================================================================
# Define your own exception types

print("Example 8: Custom Exceptions")
print("-" * 50)

class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(f"Need {amount}, have {balance}")
    return balance - amount

try:
    balance = withdraw(100, 50)
    print(f"New balance: {balance}")
except InvalidAmountError as e:
    print(f"Invalid transaction: {e}")
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")

print()

# ============================================================================
# EXAMPLE 9: Exception Hierarchy
# ============================================================================
# Catching parent vs specific exceptions

print("Example 9: Exception Hierarchy")
print("-" * 50)

try:
    int("abc")
except ValueError as e:
    print(f"Caught ValueError: {e}")

try:
    "string" + 5
except TypeError as e:
    print(f"Caught TypeError: {e}")

# Both ValueError and TypeError are subclasses of Exception
try:
    int("xyz")
except Exception as e:
    print(f"Caught generic Exception: {e}")

print()

# ============================================================================
# EXAMPLE 10: User Input Validation Loop
# ============================================================================
# Keep asking until valid

print("Example 10: Input Validation Loop")
print("-" * 50)

while True:
    try:
        age_str = input("Enter your age (or type 'quit'): ")
        if age_str.lower() == "quit":
            break
        age = int(age_str)
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")
        print(f"Valid age: {age}")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

print()

# ============================================================================
# EXAMPLE 11: File Operations with Error Handling
# ============================================================================
# Safe file handling

print("Example 11: Safe File Operations")
print("-" * 50)

try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found")
    content = "default content"
except IOError as e:
    print(f"Error reading file: {e}")
    content = "error content"

print(f"Content: {content[:30]}...")
print()

# ============================================================================
# EXAMPLE 12: Converting with Fallback
# ============================================================================
# Convert or use default

print("Example 12: Conversion with Fallback")
print("-" * 50)

def to_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(f"to_int('123') = {to_int('123')}")
print(f"to_int('abc') = {to_int('abc')}")
print(f"to_int('xyz', -1) = {to_int('xyz', -1)}")
print()

# ============================================================================
# EXAMPLE 13: Catching Multiple Exception Types
# ============================================================================
# Handle different errors the same way

print("Example 13: Multiple Exception Types")
print("-" * 50)

def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        return None

print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")
print(f"safe_divide('x', 2) = {safe_divide('x', 2)}")
print()

# ============================================================================
# EXAMPLE 14: Try/Except in Function
# ============================================================================
# Error handling in functions

print("Example 14: Function Error Handling")
print("-" * 50)

def process_number(value):
    """Convert to int and return double, or None on error."""
    try:
        num = int(value)
        return num * 2
    except ValueError:
        print(f"Could not convert '{value}' to number")
        return None

result = process_number("42")
print(f"Result: {result}")

result = process_number("abc")
print(f"Result: {result}")
print()

# ============================================================================
# EXAMPLE 15: Defensive Programming
# ============================================================================
# Check before operating

print("Example 15: Defensive Programming")
print("-" * 50)

def get_first(lst):
    """Get first item, raise error if empty."""
    if not lst:
        raise ValueError("List cannot be empty")
    return lst[0]

try:
    print(get_first([1, 2, 3]))
except ValueError as e:
    print(f"Error: {e}")

try:
    print(get_first([]))
except ValueError as e:
    print(f"Error: {e}")
print()

# ============================================================================
# EXAMPLE 16: Graceful Degradation
# ============================================================================
# Provide fallback functionality

print("Example 16: Graceful Degradation")
print("-" * 50)

def get_config(filename, defaults):
    """Load config from file, use defaults if file missing."""
    try:
        with open(filename) as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found, using defaults")
        return defaults

config = get_config("config.json", {"debug": False, "port": 8000})
print(f"Config: {config}")
print()

# ============================================================================
# EXAMPLE 17: Chained Exceptions
# ============================================================================
# Exception that caused another exception

print("Example 17: Exception Context")
print("-" * 50)

try:
    try:
        data = int("invalid")
    except ValueError as e:
        raise RuntimeError("Failed to parse data") from e
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    print(f"Caused by: {e.__cause__}")

print()

# ============================================================================
# EXAMPLE 18: Logging Errors
# ============================================================================
# Record errors for debugging

print("Example 18: Error Logging")
print("-" * 50)

def log_error(error, context=""):
    """Log error with context."""
    error_msg = f"[ERROR] {type(error).__name__}: {error}"
    if context:
        error_msg += f" (Context: {context})"
    print(error_msg)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    log_error(e, "division operation")

try:
    lst[100]
except Exception as e:
    log_error(e, "list access")

print()

# ============================================================================
# EXAMPLE 19: Retry Logic
# ============================================================================
# Retry failed operations

print("Example 19: Retry Logic")
print("-" * 50)

def try_convert(value, max_retries=3):
    """Try to convert, retrying on failure."""
    for attempt in range(max_retries):
        try:
            return int(value)
        except ValueError:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed, retrying...")
            else:
                print(f"All {max_retries} attempts failed")
                return None

result = try_convert("not a number")
print(f"Result: {result}")
print()

# ============================================================================
# EXAMPLE 20: Context Manager Pattern
# ============================================================================
# With statement for safe resource management

print("Example 20: With Statement")
print("-" * 50)

# Writing
with open("demo.txt", "w") as f:
    f.write("test data")

# Reading
with open("demo.txt", "r") as f:
    content = f.read()

print(f"File content: {content}")

# File automatically closed even if error occurs
try:
    with open("demo.txt", "r") as f:
        # If error here, file still closes
        content = f.read()
        print(f"Read successfully")
except Exception as e:
    print(f"Error: {e}")

print()

# ============================================================================
# EXAMPLE 21: Nested Try/Except
# ============================================================================
# Try blocks inside try blocks

print("Example 21: Nested Try/Except")
print("-" * 50)

try:
    with open("demo.txt", "r") as f:
        try:
            data = int(f.read())
        except ValueError:
            print("File doesn't contain a number")
            data = 0
except FileNotFoundError:
    print("File not found")
    data = 0

print(f"Data: {data}")
print()

# ============================================================================
# EXAMPLE 22: Exception in Loop
# ============================================================================
# Continue loop despite error

print("Example 22: Exception in Loop")
print("-" * 50)

numbers_str = ["10", "20", "abc", "30", "xyz", "40"]

results = []
for num_str in numbers_str:
    try:
        num = int(num_str)
        results.append(num)
    except ValueError:
        print(f"Skipping invalid: {num_str}")

print(f"Valid numbers: {results}")
print()

# ============================================================================
# EXAMPLE 23: Type Checking
# ============================================================================
# Validate types

print("Example 23: Type Validation")
print("-" * 50)

def process_list(items):
    """Process list, raise error if not list."""
    if not isinstance(items, list):
        raise TypeError(f"Expected list, got {type(items).__name__}")
    return len(items)

try:
    print(process_list([1, 2, 3]))
except TypeError as e:
    print(f"Error: {e}")

try:
    print(process_list("not a list"))
except TypeError as e:
    print(f"Error: {e}")

print()

# ============================================================================
# EXAMPLE 24: Re-raising Exceptions
# ============================================================================
# Catch and re-raise

print("Example 24: Re-raising")
print("-" * 50)

def process_and_log(value):
    try:
        return int(value)
    except ValueError as e:
        print(f"Processing error: {e}")
        raise  # Re-raise same exception

try:
    process_and_log("invalid")
except ValueError as e:
    print(f"Caught re-raised error: {e}")

print()

# ============================================================================
# EXAMPLE 25: Finally with Return
# ============================================================================
# Finally runs even with return

print("Example 25: Finally with Return")
print("-" * 50)

def example_finally():
    try:
        print("  In try block")
        return "result"
    finally:
        print("  In finally block (always runs)")

result = example_finally()
print(f"Returned: {result}")

print()

# Clean up demo file
import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
if os.path.exists("temporary.txt"):
    os.remove("temporary.txt")

