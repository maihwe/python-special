# Topic 16: Functions - Exercises

## Overview

These exercises teach you to define and use functions for code reusability and organization. You'll progress from simple functions to higher-order functions and complex patterns.

---

## Exercise 1: Simple Function Definition

**Write a program that:**
- Defines function that takes one parameter
- Returns calculated value
- Calls function multiple times
- Displays results

**Example:**
```
Function: square(x)
square(5) = 25
square(10) = 100
square(3) = 9
```

**Concepts:** Function definition, parameters, return values

---

## Exercise 2: Multiple Parameters

**Write a program that:**
- Defines function with 3 parameters
- Performs calculation with all parameters
- Calls function with different arguments
- Shows results

**Example:**
```
Function: calculate_total(price, quantity, tax_rate)
calculate_total(10, 5, 0.08) = 54.0
calculate_total(25, 2, 0.08) = 54.0
```

**Concepts:** Multiple parameters, calculations

---

## Exercise 3: Multiple Return Values

**Write a program that:**
- Defines function that returns multiple values
- Unpacks returned values
- Uses returned values in calculations
- Displays all results

**Example:**
```
Function returns: (min, max, average)
min=1, max=5, average=3.0
```

**Concepts:** Tuple returns, unpacking

---

## Exercise 4: Default Parameters

**Write a program that:**
- Defines function with default parameters
- Calls with and without defaults
- Shows difference in behavior
- Handles various cases

**Example:**
```
greet(name) with default greeting="Hello"
greet("Alice") → Hello, Alice!
greet("Bob", "Hi") → Hi, Bob!
```

**Concepts:** Default parameters, optional arguments

---

## Exercise 5: Scope and Local Variables

**Write a program that:**
- Demonstrates local vs global variables
- Shows variable shadowing
- Explains scope rules
- Modifies and tracks variables

**Example:**
```
Global x = 10
Inside function: x = 20
After function: x = 10 (unchanged)
```

**Concepts:** Local scope, global scope, shadowing

---

## Exercise 6: *args - Variable Arguments

**Write a program that:**
- Defines function using *args
- Accepts any number of arguments
- Processes variable number of inputs
- Shows flexibility

**Example:**
```
sum_all(1, 2, 3) = 6
sum_all(1, 2, 3, 4, 5) = 15
```

**Concepts:** *args, variable arguments, flexibility

---

## Exercise 7: **kwargs - Keyword Arguments

**Write a program that:**
- Defines function using **kwargs
- Accepts keyword arguments
- Processes as dictionary
- Displays key-value pairs

**Example:**
```
print_config(debug=True, host="localhost", port=8000)
debug: True
host: localhost
port: 8000
```

**Concepts:** **kwargs, keyword arguments, dictionaries

---

## Exercise 8: Function Processing Lists

**Write a program that:**
- Defines functions to process lists
- Doubles all values
- Filters by condition
- Transforms data

**Example:**
```
Original: [1, 2, 3, 4, 5]
Doubled: [2, 4, 6, 8, 10]
Evens: [2, 4]
```

**Concepts:** List processing, filtering, transformations

---

## Exercise 9: Higher-Order Functions

**Write a program that:**
- Defines function that takes function as parameter
- Applies function to items
- Uses map/filter/sort
- Composes operations

**Example:**
```
apply(add, 5, 3) = 8
apply(multiply, 5, 3) = 15
map(square, [1, 2, 3]) = [1, 4, 9]
```

**Concepts:** Higher-order functions, callbacks, functional programming

---

## Exercise 10: Recursion

**Write a program that:**
- Defines recursive function
- Handles base case and recursive case
- Calculates factorial or similar
- Shows recursive calls

**Example:**
```
factorial(5) = 120
fibonacci(6) = 8
countdown(3): 3, 2, 1, Done!
```

**Concepts:** Recursion, base case, recursive case

---

## Challenge Exercises (Optional)

### Challenge 1: Data Processing Pipeline
- Create functions to:
  - Load data (from list)
  - Clean data (remove invalid)
  - Transform data (apply operations)
  - Analyze data (calculate statistics)
- Chain functions together
- Show input and output at each stage

### Challenge 2: Calculator with Functions
- Create functions for:
  - Each operation (add, subtract, multiply, divide)
  - Memory storage
  - Command parsing
- Build interactive calculator
- Handle edge cases (division by zero, etc.)

### Challenge 3: Game Logic Functions
- Create functions for:
  - Player movement
  - Collision detection
  - Score calculation
  - Win/lose conditions
- Simulate game loop
- Track game state

### Challenge 4: Text Processing Suite
- Create functions for:
  - Word frequency analysis
  - Text statistics (length, unique words)
  - Text transformation (uppercase, reverse)
  - Pattern matching
- Combine functions into pipeline
- Generate text report

---

## Tips for Success

1. **Single responsibility:** Each function does one thing
2. **Clear names:** Name clearly shows what function does
3. **Docstrings:** Document what function does
4. **Handle edge cases:** Empty lists, None values, etc.
5. **Return vs print:** Return for reusability, print for output

---

## Key Takeaways

After these exercises, you should:
- ✅ Define functions with parameters
- ✅ Return single and multiple values
- ✅ Use default and optional parameters
- ✅ Understand scope and local variables
- ✅ Use *args and **kwargs
- ✅ Process lists with functions
- ✅ Create higher-order functions
- ✅ Write recursive functions
- ✅ Compose functions together
- ✅ Organize code into reusable functions

