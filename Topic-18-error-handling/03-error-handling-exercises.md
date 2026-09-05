# Topic 18: Error Handling - Exercises

## Overview

These exercises teach you to use try/except/finally blocks, handle different exception types, and write robust, defensive programs that recover from errors gracefully.

---

## Exercise 1: Basic Try/Except

**Write a program that:**
- Attempts to convert user input to integer
- Catches ValueError if conversion fails
- Displays error message and uses default value
- Shows converted number

**Example:**
```
Enter a number: abc
Error: Not a valid number!
Using default: 0
```

**Concepts:** Try/except, ValueError, error recovery

---

## Exercise 2: Multiple Exception Types

**Write a program that:**
- Attempts multiple operations
- Catches different exception types
- Handles each type differently
- Shows specific error messages

**Example:**
```
Accessing list[10]: IndexError caught
Accessing dict[key]: KeyError caught
Dividing by 0: ZeroDivisionError caught
```

**Concepts:** Multiple except blocks, specific exceptions

---

## Exercise 3: Finally Clause

**Write a program that:**
- Opens a file for reading
- Attempts to process content
- Uses finally to ensure file closes
- Shows execution flow

**Example:**
```
Opening file...
Processing content...
Closing file (in finally)
Done!
```

**Concepts:** Finally clause, resource cleanup

---

## Exercise 4: Else Clause

**Write a program that:**
- Attempts conversion
- Has except block (not triggered)
- Has else block (runs on success)
- Shows both paths

**Example:**
```
Try 1: Convert "123"
Success: Converted to 123
Squared: 15129

Try 2: Convert "abc"
Failed to convert
```

**Concepts:** Else clause, success path

---

## Exercise 5: Input Validation Loop

**Write a program that:**
- Repeatedly asks for input
- Validates input
- Catches ValueError on invalid input
- Continues until valid
- Shows final result

**Example:**
```
Enter age: abc
Invalid: Not a number!
Enter age: -5
Invalid: Age must be positive!
Enter age: 25
Valid: Age is 25
```

**Concepts:** Validation loops, exception recovery

---

## Exercise 6: Raising Custom Exceptions

**Write a program that:**
- Defines custom exception class
- Validates data with custom exception
- Catches and handles custom exception
- Shows error message

**Example:**
```
Creating account...
ValueError: Password too short!
Invalid registration data
```

**Concepts:** Custom exceptions, raising, validation

---

## Exercise 7: Defensive Programming

**Write a program that:**
- Implements defensive function
- Checks preconditions
- Raises appropriate exceptions
- Catches and handles errors

**Example:**
```
Process [1, 2, 3]: Success
Process []: ValueError: Empty list!
```

**Concepts:** Defensive programming, preconditions

---

## Exercise 8: Graceful Degradation

**Write a program that:**
- Attempts to load configuration from file
- Uses defaults if file missing
- Shows both paths
- Demonstrates fallback behavior

**Example:**
```
Loading config.json...
File not found!
Using default configuration
Config: {debug: True, port: 8000}
```

**Concepts:** Error handling, graceful fallbacks

---

## Exercise 9: Exception in Loop

**Write a program that:**
- Processes list of values
- Some valid, some invalid
- Catches exceptions per item
- Continues on error
- Shows results

**Example:**
```
Processing: ["10", "abc", "20", "xyz", "30"]
Skipped: abc
Skipped: xyz
Valid: [10, 20, 30]
```

**Concepts:** Loop error handling, continuation

---

## Exercise 10: Context Manager (With Statement)

**Write a program that:**
- Opens file with with statement
- Demonstrates automatic closing
- Shows that file closes even on error
- Explains advantage over try/finally

**Example:**
```
With statement opens file
Process content
File auto-closes
Versus manual close in finally
```

**Concepts:** With statement, resource management, context managers

---

## Challenge Exercises (Optional)

### Challenge 1: Robust Calculator
- Implement calculator with operations
- Validate inputs (type, range)
- Handle division by zero
- Raise custom exceptions for errors
- Keep running until user exits
- Handle all error types gracefully

### Challenge 2: Data Parser
- Read file with mixed valid/invalid data
- Parse each line (may fail)
- Log errors with line numbers
- Collect valid data only
- Generate report with success/failure counts
- Create error summary

### Challenge 3: Retry Mechanism
- Implement function with retry logic
- Attempt operation up to N times
- Log each attempt
- Use exponential backoff (wait longer each time)
- Give up after max retries
- Return result or None

### Challenge 4: Error Recovery System
- Create multi-level error handling
- Handle specific exceptions one way
- Handle generic exceptions differently
- Log all errors
- Provide user-friendly messages
- Continue operation where possible
- Maintain application state

---

## Tips for Success

1. **Catch specific, not generic:** Avoid bare `except:` or `except Exception:`
2. **Use finally for cleanup:** Always close resources
3. **Raise early:** Check preconditions at function start
4. **Custom exceptions:** Define for domain-specific errors
5. **Log errors:** Record what went wrong
6. **Provide recovery:** Don't just crash, handle gracefully
7. **Test error paths:** Test what happens when things fail

---

## Key Takeaways

After these exercises, you should:
- ✅ Use try/except/finally blocks
- ✅ Catch specific exception types
- ✅ Use else for success path
- ✅ Raise custom exceptions
- ✅ Implement defensive programming
- ✅ Write input validation loops
- ✅ Handle file operations safely
- ✅ Use with statement
- ✅ Implement graceful degradation
- ✅ Build robust error recovery

