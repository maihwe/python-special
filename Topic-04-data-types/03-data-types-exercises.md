# Topic 4: Data Types - Exercises

## Overview

These exercises build understanding of Python's type system. You'll identify types, understand why types matter, convert between them, and choose appropriate types for problems.

---

## Exercise 1: Identify the Type

**Write a program that:**
- Creates variables of different types
- Uses `type()` to display each type
- Prints a summary of all types found

**Example output:**
```
Variable 'age' = 25
Type: <class 'int'>

Variable 'price' = 19.99
Type: <class 'float'>

Variable 'name' = Alice
Type: <class 'str'>

(and so on)
```

**Concepts:** type() function, basic types identification

---

## Exercise 2: Predict Type Results

**Write a program that:**
- Performs various operations
- Predicts the result type before running
- Displays whether prediction was correct

**Example:**
```
Operation: 5 + 3
Prediction: int
Actual: <class 'int'>
✓ Correct!

Operation: 5.0 + 3
Prediction: float
Actual: <class 'float'>
✓ Correct!
```

**Concepts:** Type promotion, operation results

---

## Exercise 3: Type Conversion Chain

**Write a program that:**
- Starts with a string
- Converts through multiple types
- Displays each step and type

**Example:**
```
Start: "42" (type: str)
After int(): 42 (type: int)
After float(): 42.0 (type: float)
After str(): "42.0" (type: str)
After bool(): True (type: bool)
```

**Concepts:** Sequential conversions, type() verification

---

## Exercise 4: Boolean Truthiness

**Write a program that:**
- Tests various values with bool()
- Categorizes them as truthy or falsy
- Displays the pattern

**Example:**
```
Testing truthiness:
0 → False (Falsy: zero)
1 → True (Truthy: non-zero)
"" → False (Falsy: empty string)
"text" → True (Truthy: non-empty)

Pattern: Empty and zero are False, rest are True
```

**Concepts:** Boolean conversion, truthiness rules

---

## Exercise 5: Type Mismatch - Understanding Errors

**Write a program that:**
- Shows operations that work (same type)
- Shows operations that fail (different types)
- Suggests solutions with conversion

**Example:**
```
VALID:
5 + 3 = 8 ✓ (int + int)

INVALID:
"5" + 3 = Error ✗ (str + int)
SOLUTION: int("5") + 3 = 8 ✓
```

**Concepts:** Type compatibility, error prevention

---

## Exercise 6: Choosing Data Types

**Write a program that:**
- Displays real-world data examples
- Recommends the best type for each
- Explains why

**Example:**
```
Age: 25
Best type: int
Reason: whole number, no decimals

Price: $19.99
Best type: float
Reason: has decimal places

Is student: true
Best type: bool
Reason: yes/no value
```

**Concepts:** Type selection, design decisions

---

## Exercise 7: Type Checking with isinstance()

**Write a program that:**
- Checks if values are specific types
- Uses isinstance() instead of type()
- Demonstrates both methods

**Example:**
```
value = 42

Using type():
type(value) == int → True

Using isinstance():
isinstance(value, int) → True

(isinstance is preferred)
```

**Concepts:** isinstance(), type checking

---

## Exercise 8: Conversion and Validation

**Write a program that:**
- Attempts to convert user input
- Handles conversion failures gracefully
- Suggests what went wrong

**Example:**
```
Enter a number: abc
✗ Cannot convert "abc" to integer
Reason: not a valid number

Try: Enter a number: 42
✓ Successfully converted to 42
```

**Concepts:** try/except, error messages

---

## Exercise 9: Real-World Data Types

**Write a program that:**
- Models a real object with multiple data types
- Shows each property and its type
- Demonstrates operations on each type

**Example: Student Record**
```
Name: Alice (str)
Age: 20 (int)
GPA: 3.8 (float)
Active: True (bool)
Graduation: None (NoneType)

Operations:
- Concatenate name: "Student: " + "Alice"
- Calculate age next year: 20 + 1
- Increase GPA: 3.8 + 0.1
```

**Concepts:** Multiple types in one program

---

## Exercise 10: Type Flow Diagram

**Write a program that:**
- Shows how types flow through a calculation
- Displays type at each step
- Explains conversions

**Example: E-commerce**
```
price_text = "19.99" (str)
↓ float()
price = 19.99 (float)
↓ * 3 (quantity)
total = 59.97 (float)
↓ str() + formatting
display = "$59.97" (str)
↓ print()
Output: $59.97
```

**Concepts:** Type transformation pipeline

---

## Challenge Exercises (Optional)

### Challenge 1: Type Converter
Build a program that converts between any basic types with proper error handling.

### Challenge 2: Type Statistics
Analyze a list of values and report how many of each type.

### Challenge 3: Smart Conversion
Automatically detect whether a string represents an int, float, or text.

### Challenge 4: Type Safety Checker
Review code and identify potential type errors before running.

---

## Tips for Success

1. **Use type():** Always verify what type a value is
2. **Understand operations:** Each type supports different operations
3. **Plan conversions:** Convert early, before using data
4. **Handle errors:** Use try/except for uncertain conversions
5. **Choose wisely:** Pick the right type for the job

---

## Key Takeaways

After these exercises, you should understand:
- ✅ Python's basic types (int, float, str, bool, None)
- ✅ How to identify types with type()
- ✅ Why types matter for operations
- ✅ How to convert between types
- ✅ What types are appropriate for different data
- ✅ How to handle type mismatches

