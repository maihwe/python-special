# Topic 16: Functions - Reusable Code Building Blocks

## Goal

**Learn to define and use functions - the foundation of organized programming. Understand parameters, return values, scope, and how to structure code into reusable, testable blocks. Master the organizational layer of programming.**

---

## Why This Matters - The Real Problem

Without functions, programs become unmaintainable:

**Without functions (repetitive):**
```python
# Calculate average for grades
grades1 = [85, 92, 78]
total1 = 0
for grade in grades1:
    total1 += grade
avg1 = total1 / len(grades1)

# Calculate average for scores
scores = [45, 67, 89]
total2 = 0
for score in scores:
    total2 += score
avg2 = total2 / len(scores)

# Calculate average for temperatures
temps = [72, 68, 75]
total3 = 0
for temp in temps:
    total3 += temp
avg3 = total3 / len(temps)
```

**With functions (elegant):**
```python
def average(items):
    return sum(items) / len(items)

avg1 = average(grades1)
avg2 = average(scores)
avg3 = average(temps)
```

**Functions enable:**
- Code reuse (DRY - Don't Repeat Yourself)
- Testing isolated logic
- Breaking complex problems into pieces
- Readable code organization
- Collaboration (each person writes functions)

---

## Mental Model 1: What Is a Function? (The Black Box Model)

A **function** is a reusable block of code with inputs and outputs.

```
Input(s) → [BLACK BOX: FUNCTION CODE] → Output
```

**Visual representation:**

```python
def add(a, b):
    return a + b

add(5, 3)  → [adds 5 + 3] → returns 8

Input: 5, 3
Function: Add them together
Output: 8
```

**Key properties:**

1. **Reusable:** Call many times
2. **Organized:** One thing per function
3. **Testable:** Test independently
4. **Maintainable:** Change in one place
5. **Readable:** Self-documenting with good names

**Parts of a function:**

```python
def function_name(parameters):
    """Docstring explaining what it does"""
    # Function body - the code
    return result  # Send value back to caller
```

---

## Mental Model 2: Defining and Calling Functions (The Definition Model)

**Define function once:**

```python
def greet(name):
    print(f"Hello, {name}!")
```

**Call it many times:**

```python
greet("Alice")   # Hello, Alice!
greet("Bob")     # Hello, Bob!
greet("Charlie") # Hello, Charlie!
```

**Execution flow:**

```python
def add(a, b):
    result = a + b
    return result

x = add(5, 3)  # Call function
# Inside function: result = 5 + 3 = 8
# Return 8 to caller
# x = 8
print(x)  # 8
```

**Function structure:**

```python
def function_name(param1, param2):
    # Code executes when function is called
    
    return value  # Return sends value back
```

---

## Mental Model 3: Parameters and Arguments (The Input Model)

**Parameters** are variables in function definition.
**Arguments** are actual values when calling.

```python
def add(a, b):  # a and b are PARAMETERS
    return a + b

add(5, 3)  # 5 and 3 are ARGUMENTS
```

**Parameter types:**

```python
# Positional parameters (order matters)
def greet(first, last):
    return f"{first} {last}"

greet("Alice", "Smith")  # Alice Smith
greet("Smith", "Alice")  # Smith Alice (wrong order!)

# Keyword parameters (use names)
greet(last="Smith", first="Alice")  # Alice Smith (correct!)

# Mix positional and keyword
greet("Alice", last="Smith")  # Alice Smith
```

**Multiple parameters:**

```python
def describe_person(name, age, city):
    print(f"{name} is {age} and lives in {city}")

describe_person("Alice", 30, "Boston")
```

**No parameters:**

```python
def get_random():
    import random
    return random.randint(1, 10)

value = get_random()
```

---

## Mental Model 4: Return Values (The Output Model)

**Return** sends value back to caller.

```python
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8
```

**Return stops execution:**

```python
def find_target(items, target):
    for item in items:
        if item == target:
            return True  # Stops immediately
    return False  # Only reached if not found
```

**Return multiple values (as tuple):**

```python
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()  # Unpack tuple

# Or return dict
def get_user():
    return {"name": "Alice", "age": 30}

user = get_user()
print(user["name"])  # Alice
```

**No explicit return (returns None):**

```python
def print_message(msg):
    print(msg)  # No return statement

result = print_message("Hello")
print(result)  # None
```

---

## Mental Model 5: Scope and Local Variables (The Namespace Model)

**Local scope:** Variables inside function only exist inside function.

```python
def greet(name):
    message = f"Hello, {name}!"  # Local variable
    print(message)

greet("Alice")  # Hello, Alice!
print(message)  # ERROR! message doesn't exist here
```

**Global scope:** Variables defined outside functions.

```python
greeting = "Hello"  # Global

def greet(name):
    print(f"{greeting}, {name}!")

greet("Alice")  # Hello, Alice!
print(greeting)  # Hello (accessible)
```

**Scope rules:**

```python
x = 10  # Global

def func():
    x = 20  # Local (shadows global)
    print(x)  # 20

func()      # 20
print(x)    # 10 (global unchanged)
```

**Using global keyword:**

```python
x = 10

def modify():
    global x  # Modify global x
    x = 20

modify()
print(x)  # 20 (changed!)
```

---

## Mental Model 6: Default Parameters (The Convenience Model)

**Default parameters** provide fallback values.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # Hello, Alice!
greet("Bob", "Hi")       # Hi, Bob!
greet("Charlie", "Hey")  # Hey, Charlie!
```

**Real-world example:**

```python
def create_account(username, email, age=None, active=True):
    return {
        "username": username,
        "email": email,
        "age": age,
        "active": active
    }

# With defaults
create_account("alice", "alice@example.com")
# With overrides
create_account("bob", "bob@example.com", 25, False)
```

**Default must be after required:**

```python
# Correct
def func(required, optional="default"):
    pass

# ERROR! Optional before required
def func(optional="default", required):
    pass
```

---

## Mental Model 7: *args and **kwargs (The Flexibility Model)

***args** accepts any number of positional arguments.

```python
def add(*numbers):
    return sum(numbers)

add(1, 2, 3)        # 6
add(1, 2, 3, 4, 5)  # 15
```

**How it works:**

```python
def print_all(*items):
    for item in items:
        print(item)

print_all(1, 2, 3)  # 1, 2, 3
print_all("a", "b")  # a, b
```

***kwargs** accepts any number of keyword arguments.

```python
def create_dict(**attributes):
    return attributes

person = create_dict(name="Alice", age=30, city="Boston")
# {"name": "Alice", "age": 30, "city": "Boston"}
```

**Real-world pattern:**

```python
def print_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

print_config(debug=True, host="localhost", port=8000)
# debug: True
# host: localhost
# port: 8000
```

**Combine all:**

```python
def flexible(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

flexible(1, 2, 3, 4, x=10, y=20)
# a=1, b=2
# args=(3, 4)
# kwargs={'x': 10, 'y': 20}
```

---

## Mental Model 8: Docstrings and Best Practices (The Documentation Model)

**Docstrings** explain what function does.

```python
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
    
    Returns:
        Float: The average value
    """
    return sum(numbers) / len(numbers)
```

**Access docstring:**

```python
help(calculate_average)
# Shows docstring

print(calculate_average.__doc__)
# Prints docstring
```

**Best practices:**

```python
# Good: Clear name, single purpose
def calculate_total_price(items):
    """Calculate total price of items including tax."""
    return sum(item["price"] for item in items) * 1.08

# Bad: Vague name, multiple purposes
def calc(x):
    # Does too much, unclear
    pass

# Good: Handle edge cases
def average(numbers):
    """Return average, or None if empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Bad: Crash on empty
def average(numbers):
    return sum(numbers) / len(numbers)  # Crashes!
```

---

## Mental Model 9: Common Patterns (The Pattern Model)

**Pattern 1: Process items**

```python
def process_all(items, operation):
    results = []
    for item in items:
        results.append(operation(item))
    return results

doubled = process_all([1, 2, 3], lambda x: x * 2)
```

**Pattern 2: Find first match**

```python
def find_first(items, condition):
    for item in items:
        if condition(item):
            return item
    return None

first_even = find_first([1, 3, 4, 5], lambda x: x % 2 == 0)
```

**Pattern 3: Filter items**

```python
def filter_items(items, condition):
    return [item for item in items if condition(item)]

evens = filter_items([1, 2, 3, 4], lambda x: x % 2 == 0)
```

**Pattern 4: Transform and collect**

```python
def transform(items, transform_func):
    return [transform_func(item) for item in items]

squared = transform([1, 2, 3], lambda x: x**2)
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Return vs Print"

**The question:** Should I return or print?

**The answer:** Return for reusability, print only for user output.

```python
# Good: Return, caller decides what to do
def calculate_total(items):
    return sum(items)

total = calculate_total([1, 2, 3])
print(total)  # Caller prints if needed

# Bad: Prints, can't reuse result
def calculate_total(items):
    print(sum(items))  # Can't capture value!
```

### Confusion 2: "Modifying Parameters"

**The question:** Does changing parameter affect original?

**The answer:** Only if parameter is mutable.

```python
# Immutable (int) - doesn't change original
def modify_int(x):
    x = 99
x = 10
modify_int(x)
print(x)  # 10 (unchanged)

# Mutable (list) - changes original
def modify_list(lst):
    lst.append(99)
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 99] (changed!)
```

### Confusion 3: "Local vs Global"

**The question:** Why can't I access variable defined in function?

**The answer:** Local variables only exist inside function.

```python
def func():
    x = 10  # Local

func()
print(x)  # ERROR! x only existed inside func
```

### Confusion 4: "Default Parameter Mutability"

**The question:** Why does default list change?

**The answer:** Default evaluated once, shared across calls.

```python
# DANGER: Shared list
def append_item(item, lst=[]):
    lst.append(item)
    return lst

append_item(1)      # [1]
append_item(2)      # [1, 2] - same list!
append_item(3)      # [1, 2, 3] - still same list!

# CORRECT: New list each time
def append_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

append_item(1)  # [1]
append_item(2)  # [2]
append_item(3)  # [3]
```

### Confusion 5: "Lambda Functions"

**The question:** What's a lambda?

**The answer:** Small unnamed function.

```python
# Normal function
def add(a, b):
    return a + b

# Lambda (same thing, inline)
add = lambda a, b: a + b

# Use in callbacks
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
```

---

## How Functions Work Internally (Execution Model)

**Call stack:**

```python
def outer(x):
    return inner(x)

def inner(x):
    return x * 2

result = outer(5)
```

**Call stack diagram:**

```
1. outer(5) called
   [Stack: outer]
   
2. inner(5) called
   [Stack: outer → inner]
   
3. inner returns 10
   [Stack: outer]
   
4. outer returns 10
   [Stack: empty]
```

---

## Real-World Functions (Practical Applications)

**Data processing:**

```python
def clean_data(raw_data):
    """Remove duplicates and sort."""
    return sorted(set(raw_data))

def analyze_data(data):
    """Calculate statistics."""
    return {
        "min": min(data),
        "max": max(data),
        "avg": sum(data) / len(data)
    }
```

**Game logic:**

```python
def move_player(player, direction):
    """Move player in direction."""
    x, y = player["pos"]
    if direction == "north":
        player["pos"] = (x, y - 1)
    elif direction == "south":
        player["pos"] = (x, y + 1)

def is_valid_move(player, new_pos):
    """Check if move is legal."""
    x, y = new_pos
    return 0 <= x < 10 and 0 <= y < 10
```

---

## Summary - The Big Picture

**What you learned:**
1. What functions are and why they matter
2. Defining and calling functions
3. Parameters and arguments
4. Return values and outputs
5. Local and global scope
6. Default parameters
7. *args and **kwargs
8. Docstrings and best practices
9. Common patterns

**Why this matters:**
- Functions are foundation of all software
- Enable code reuse and testing
- Make programs readable and maintainable
- Allow collaboration (divide work)
- Required for everything else (OOP, modules, etc.)

**What's next:**
Now you can organize code into functions.

Topic 17 teaches **File I/O** - how to save/load data persistently.

---

## What You Should Be Able To Do Now

✅ Define and call functions
✅ Use parameters and arguments
✅ Return values (single and multiple)
✅ Understand local and global scope
✅ Use default parameters
✅ Use *args and **kwargs
✅ Write docstrings
✅ Test functions independently
✅ Solve problems using functions
✅ Apply common function patterns

