# Topic 18: Error Handling - Writing Robust Programs

## Goal

**Learn to handle errors gracefully using try/except/finally blocks. Understand exception types, raising custom exceptions, and defensive programming practices. Master writing programs that recover from failures instead of crashing.**

---

## Why This Matters - The Real Problem

Without error handling, programs crash on unexpected input:

**Without error handling (crashes):**
```python
user_input = input("Enter a number: ")
number = int(user_input)  # Crashes if user enters "abc"!
# ValueError: invalid literal for int()
```

**With error handling (robust):**
```python
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("That's not a valid number!")
    number = 0
```

**Error handling enables:**
- Handle unexpected input gracefully
- Recover from file/network errors
- Provide helpful error messages
- Log errors for debugging
- Keep program running
- Professional error recovery

---

## Mental Model 1: What Is an Exception? (The Error Model)

An **exception** is an event that disrupts normal program flow.

```python
# Exception: division by zero
result = 10 / 0  # ZeroDivisionError

# Exception: file not found
f = open("nonexistent.txt")  # FileNotFoundError

# Exception: invalid conversion
x = int("abc")  # ValueError

# Exception: index out of range
lst = [1, 2, 3]
lst[10]  # IndexError
```

**Program flow without handling:**

```
Normal execution
    ↓
Exception occurs
    ↓
Program crashes ← BAD
```

**Program flow with handling:**

```
Normal execution
    ↓
Exception occurs
    ↓
Exception caught
    ↓
Recovery action ← GOOD
    ↓
Program continues
```

---

## Mental Model 2: Try/Except Blocks (The Catching Model)

**Try** contains code that might fail.
**Except** handles the failure.

```python
try:
    # Code that might raise exception
    number = int("123")  # OK
    number = int("abc")  # Raises ValueError
except ValueError:
    # Handle ValueError
    print("Not a valid number!")
```

**Execution flow:**

```
try:
    risky_code()  # If this fails...
except SomeError:  # ...jump to here
    recovery_code()  # ...and execute this
```

**Multiple except blocks:**

```python
try:
    file = open("data.txt")
    data = int(file.read())
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("File doesn't contain a number!")
```

---

## Mental Model 3: Exception Types (The Hierarchy Model)

Python has built-in exception types:

```
Exception (base class)
├── ValueError: Wrong type of value
├── TypeError: Wrong type of variable
├── KeyError: Dictionary key missing
├── IndexError: List index out of range
├── ZeroDivisionError: Division by zero
├── FileNotFoundError: File doesn't exist
├── IOError: Input/output problem
├── NameError: Variable not defined
├── AttributeError: Attribute doesn't exist
└── ... (many more)
```

**Common exceptions:**

```python
# ValueError: correct type, wrong value
int("abc")  # ValueError

# TypeError: wrong type
"string" + 5  # TypeError

# KeyError: key not in dict
d = {"a": 1}
d["b"]  # KeyError

# IndexError: index out of range
lst = [1, 2, 3]
lst[10]  # IndexError

# ZeroDivisionError: divide by zero
10 / 0  # ZeroDivisionError

# FileNotFoundError: file doesn't exist
open("notfound.txt")  # FileNotFoundError
```

---

## Mental Model 4: Finally Clause (The Cleanup Model)

**Finally** runs whether exception occurs or not - for cleanup.

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Always runs
```

**Use finally for:**
- Closing files
- Releasing resources
- Cleanup actions
- Logging completion

**Execution flow:**

```
try block:
    ↓
    No error → Continue
    Error → Jump to except

except block (if error):
    ↓
    Handle error

finally block:
    ↓
    ALWAYS runs (error or no error)
```

---

## Mental Model 5: Else Clause (The Success Model)

**Else** runs only if no exception occurred.

```python
try:
    number = int("123")  # OK
except ValueError:
    print("Not a number!")
else:
    print(f"Successfully converted: {number}")
```

**When to use:**

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found!")
else:
    # Only runs if file opened successfully
    data = file.read()
finally:
    # Always runs
    if file:
        file.close()
```

---

## Mental Model 6: Raising Exceptions (The Creation Model)

**Raise** creates and throws an exception.

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

validate_age(-5)  # Raises ValueError
```

**Why raise:**
- Enforce requirements
- Signal errors to caller
- Control error messages
- Stop invalid operations

**Raise with message:**

```python
if balance < amount:
    raise ValueError(f"Insufficient funds. Have {balance}, need {amount}")
```

**Re-raise exception:**

```python
try:
    risky_operation()
except ValueError as e:
    print(f"Caught error: {e}")
    raise  # Re-raise same exception
```

---

## Mental Model 7: Custom Exceptions (The Extension Model)

Create your own exception types.

```python
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Need {amount}, have {balance}")
    return balance - amount

try:
    withdraw(10, 20)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
```

**Why custom exceptions:**
- Clear error meaning
- Specific handling
- Better code organization
- Domain-specific errors

---

## Mental Model 8: Exception Context (The Information Model)

**As** captures exception object for details.

```python
try:
    int("abc")
except ValueError as e:
    print(f"Error message: {e}")
    print(f"Error type: {type(e)}")
```

**Exception information:**

```python
try:
    lst = [1, 2, 3]
    value = lst[10]
except IndexError as e:
    print(f"Message: {e}")  # list index out of range
    print(f"Type: {type(e).__name__}")  # IndexError
```

---

## Mental Model 9: Defensive Programming (The Prevention Model)

**Check before operating:**

```python
# Bad: assume it works
def process(lst):
    return lst[0]  # Crashes if empty

# Good: check first
def process(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    return lst[0]
```

**LBYL (Look Before You Leap):**

```python
# Check before accessing
if key in dictionary:
    value = dictionary[key]
```

**EAFP (Easier to Ask Forgiveness than Permission):**

```python
# Try and handle exceptions
try:
    value = dictionary[key]
except KeyError:
    value = None
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Which Exception to Catch?"

**The question:** Should I catch ValueError or Exception?

**The answer:** Catch the specific exception you expect.

```python
# Good: catch specific error
try:
    number = int(user_input)
except ValueError:
    print("Not a number!")

# Bad: catch everything
try:
    number = int(user_input)
except Exception:  # Hides bugs!
    print("Error!")
```

### Confusion 2: "Try/Except Slows Program"

**The question:** Is try/except slow?

**The answer:** No. It's only slow if exception actually occurs.

```python
# Normal execution (no exception): Fast
try:
    x = int("123")  # OK
except ValueError:
    pass

# Exception occurs: Slower, but correct
try:
    x = int("abc")  # Error
except ValueError:
    pass
```

### Confusion 3: "Multiple Except Order"

**The question:** What's the order of except blocks?

**The answer:** First matching block catches. Order specific to general.

```python
# Correct: specific before general
try:
    risky()
except ValueError:  # Specific
    pass
except Exception:  # General
    pass

# Wrong: general catches everything, specific never reached
try:
    risky()
except Exception:  # General catches first!
    pass
except ValueError:  # Never reached
    pass
```

### Confusion 4: "When to Use Finally"

**The question:** Do I always need finally?

**The answer:** Only for cleanup. Use `with` for files.

```python
# With statement (preferred for files)
with open("file.txt") as f:
    data = f.read()  # Auto-closes

# Try/finally (manual cleanup)
f = open("file.txt")
try:
    data = f.read()
finally:
    f.close()
```

### Confusion 5: "Exception Doesn't Stop Program"

**The question:** Why didn't the program crash?

**The answer:** Exception was caught and handled.

```python
try:
    int("abc")  # Raises ValueError
except ValueError:
    pass  # Caught and handled
# Program continues
print("Still running!")
```

---

## How Exception Handling Works Internally (Execution Model)

**Call stack unwinding:**

```python
def level3():
    int("abc")  # Raises ValueError

def level2():
    level3()

def level1():
    level2()

try:
    level1()
except ValueError:
    print("Caught!")
```

**Execution:**

```
level1() → level2() → level3() → Exception raised
↑         ↑         ↑
Return (unwind stack)
         ↓
    ValueError caught in try/except
```

---

## Real-World Error Handling (Practical Applications)

**File operations:**

```python
try:
    with open("data.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("Data file not found, using defaults")
    data = ""
```

**User input validation:**

```python
while True:
    try:
        age = int(input("Enter age: "))
        if age < 0 or age > 150:
            raise ValueError("Invalid age")
        break
    except ValueError:
        print("Please enter a valid age (0-150)")
```

**API/Network operations:**

```python
try:
    response = requests.get(url, timeout=5)
except requests.Timeout:
    print("Request timed out")
except requests.ConnectionError:
    print("Network connection failed")
```

---

## Summary - The Big Picture

**What you learned:**
1. What exceptions are
2. Try/except blocks
3. Exception types and hierarchy
4. Finally clauses
5. Else clauses
6. Raising exceptions
7. Custom exceptions
8. Exception context
9. Defensive programming

**Why this matters:**
- Programs don't crash on unexpected input
- Recover from errors gracefully
- Provide helpful messages
- Professional error handling
- Foundation for robust systems

**What's next:**
Now you handle errors.

Topic 19 teaches **OOP Basics** - organizing code into objects.

---

## What You Should Be Able To Do Now

✅ Use try/except blocks
✅ Handle specific exceptions
✅ Use multiple except blocks
✅ Understand exception hierarchy
✅ Use finally for cleanup
✅ Use else for success path
✅ Raise custom exceptions
✅ Catch and inspect exceptions
✅ Write defensive code
✅ Build robust error recovery

