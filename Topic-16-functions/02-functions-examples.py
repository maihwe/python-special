# Topic 16: Functions - Elaborate Examples
# Comprehensive examples of defining and using functions

# ============================================================================
# EXAMPLE 1: Simple Function Definition and Call
# ============================================================================
# Define once, call multiple times

print("Example 1: Simple Function")
print("-" * 50)

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")
print()

# ============================================================================
# EXAMPLE 2: Function with Return Value
# ============================================================================
# Return and use result

print("Example 2: Return Values")
print("-" * 50)

def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

x = add(10, 20)
y = add(x, 5)
print(f"Result: {y}")
print()

# ============================================================================
# EXAMPLE 3: Function with Multiple Parameters
# ============================================================================
# Functions accept multiple inputs

print("Example 3: Multiple Parameters")
print("-" * 50)

def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

describe_person("Alice", 30, "Boston")
describe_person("Bob", 25, "NYC")
describe_person("Charlie", 28, "LA")
print()

# ============================================================================
# EXAMPLE 4: Positional and Keyword Arguments
# ============================================================================
# Call functions different ways

print("Example 4: Argument Types")
print("-" * 50)

def greet_full(first, last):
    return f"{first} {last}"

# Positional
result = greet_full("Alice", "Smith")
print(f"Positional: {result}")

# Keyword
result = greet_full(first="Bob", last="Jones")
print(f"Keyword: {result}")

# Mixed
result = greet_full("Charlie", last="Brown")
print(f"Mixed: {result}")
print()

# ============================================================================
# EXAMPLE 5: Multiple Return Values
# ============================================================================
# Return multiple values as tuple

print("Example 5: Multiple Returns")
print("-" * 50)

def get_user():
    return ("Alice", 30, "Boston")

name, age, city = get_user()
print(f"User: {name}, age {age}, from {city}")

def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")
print()

# ============================================================================
# EXAMPLE 6: Return Dictionary
# ============================================================================
# Return structured data

print("Example 6: Return Dictionary")
print("-" * 50)

def get_stats(numbers):
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

stats = get_stats([10, 20, 30, 40, 50])
print(f"Stats: {stats}")
print(f"Average: {stats['avg']}")
print()

# ============================================================================
# EXAMPLE 7: Default Parameters
# ============================================================================
# Parameters with default values

print("Example 7: Default Parameters")
print("-" * 50)

def greet_with_greeting(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_with_greeting("Alice")
greet_with_greeting("Bob", "Hi")
greet_with_greeting("Charlie", "Hey")
print()

# ============================================================================
# EXAMPLE 8: No Parameters
# ============================================================================
# Function that takes nothing

print("Example 8: No Parameters")
print("-" * 50)

def get_version():
    return "1.0.0"

def show_menu():
    print("1. Play")
    print("2. Settings")
    print("3. Quit")

version = get_version()
print(f"Version: {version}")
show_menu()
print()

# ============================================================================
# EXAMPLE 9: No Return Value
# ============================================================================
# Function that just performs action

print("Example 9: No Return (None)")
print("-" * 50)

def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

print_numbers(5)

result = print_numbers(3)
print(f"Result is: {result}")
print()

# ============================================================================
# EXAMPLE 10: Conditional Returns
# ============================================================================
# Return different values based on logic

print("Example 10: Conditional Returns")
print("-" * 50)

def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print(f"Score 95: {check_grade(95)}")
print(f"Score 85: {check_grade(85)}")
print(f"Score 65: {check_grade(65)}")
print()

# ============================================================================
# EXAMPLE 11: Early Return
# ============================================================================
# Return when condition met

print("Example 11: Early Return")
print("-" * 50)

def find_in_list(items, target):
    for item in items:
        if item == target:
            return True
    return False

result = find_in_list([1, 2, 3, 4, 5], 3)
print(f"Found 3: {result}")

result = find_in_list([1, 2, 3, 4, 5], 99)
print(f"Found 99: {result}")
print()

# ============================================================================
# EXAMPLE 12: Local vs Global Scope
# ============================================================================
# Variables inside and outside functions

print("Example 12: Scope")
print("-" * 50)

x = 10  # Global

def show_x():
    print(f"Inside function, x = {x}")

show_x()
print(f"Outside function, x = {x}")

def modify_x():
    x = 20  # Local (doesn't change global)
    print(f"Inside function, x = {x}")

modify_x()
print(f"After function, x = {x}")  # Still 10!
print()

# ============================================================================
# EXAMPLE 13: Modify Global with global keyword
# ============================================================================
# Change global variable from inside function

print("Example 13: Global Keyword")
print("-" * 50)

counter = 0

def increment():
    global counter
    counter += 1

print(f"Start: {counter}")
increment()
print(f"After increment(): {counter}")
increment()
print(f"After increment(): {counter}")
print()

# ============================================================================
# EXAMPLE 14: *args (Variable Arguments)
# ============================================================================
# Accept any number of positional arguments

print("Example 14: *args")
print("-" * 50)

def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"add_all(1, 2, 3) = {add_all(1, 2, 3)}")
print(f"add_all(1, 2, 3, 4, 5) = {add_all(1, 2, 3, 4, 5)}")
print(f"add_all(10) = {add_all(10)}")
print()

# ============================================================================
# EXAMPLE 15: **kwargs (Variable Keyword Arguments)
# ============================================================================
# Accept any number of keyword arguments

print("Example 15: **kwargs")
print("-" * 50)

def print_attributes(**attrs):
    for key, value in attrs.items():
        print(f"  {key}: {value}")

print("Person:")
print_attributes(name="Alice", age=30, city="Boston")

print("Config:")
print_attributes(debug=True, host="localhost", port=8000)
print()

# ============================================================================
# EXAMPLE 16: *args and **kwargs Combined
# ============================================================================
# Use both together

print("Example 16: *args and **kwargs")
print("-" * 50)

def flexible(a, b, *args, **kwargs):
    print(f"Required: a={a}, b={b}")
    print(f"Extra positional: {args}")
    print(f"Extra keyword: {kwargs}")

flexible(1, 2, 3, 4, x=10, y=20)
print()

# ============================================================================
# EXAMPLE 17: Docstrings
# ============================================================================
# Document what function does

print("Example 17: Docstrings")
print("-" * 50)

def calculate_area(width, height):
    """
    Calculate area of rectangle.
    
    Args:
        width: Rectangle width
        height: Rectangle height
    
    Returns:
        Area as float
    """
    return width * height

print(f"Area: {calculate_area(5, 3)}")
print(f"Docstring: {calculate_area.__doc__}")
print()

# ============================================================================
# EXAMPLE 18: Function Processing Lists
# ============================================================================
# Process and transform lists

print("Example 18: List Processing")
print("-" * 50)

def double_all(numbers):
    return [x * 2 for x in numbers]

def filter_evens(numbers):
    return [x for x in numbers if x % 2 == 0]

numbers = [1, 2, 3, 4, 5]
doubled = double_all(numbers)
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

evens = filter_evens(numbers)
print(f"Even numbers: {evens}")
print()

# ============================================================================
# EXAMPLE 19: Function as Parameter
# ============================================================================
# Pass functions to other functions

print("Example 19: Function Parameters")
print("-" * 50)

def apply_operation(a, b, operation):
    return operation(a, b)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

result = apply_operation(5, 3, add)
print(f"apply_operation(5, 3, add) = {result}")

result = apply_operation(5, 3, multiply)
print(f"apply_operation(5, 3, multiply) = {result}")
print()

# ============================================================================
# EXAMPLE 20: Lambda Functions
# ============================================================================
# Small unnamed functions

print("Example 20: Lambda Functions")
print("-" * 50)

# Traditional function
def add_func(a, b):
    return a + b

# Lambda (same thing)
add_lambda = lambda a, b: a + b

print(f"add_func(5, 3) = {add_func(5, 3)}")
print(f"add_lambda(5, 3) = {add_lambda(5, 3)}")

# Lambda in callbacks
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")
print()

# ============================================================================
# EXAMPLE 21: Higher-Order Functions with map()
# ============================================================================
# Apply function to each item

print("Example 21: map()")
print("-" * 50)

def to_uppercase(word):
    return word.upper()

words = ["hello", "world", "python"]
uppercase = list(map(to_uppercase, words))
print(f"Original: {words}")
print(f"Uppercase: {uppercase}")

# With lambda
doubled = list(map(lambda x: x * 2, [1, 2, 3]))
print(f"Doubled: {doubled}")
print()

# ============================================================================
# EXAMPLE 22: Higher-Order Functions with filter()
# ============================================================================
# Keep only items that match condition

print("Example 22: filter()")
print("-" * 50)

def is_positive(x):
    return x > 0

numbers = [-2, -1, 0, 1, 2, 3]
positive = list(filter(is_positive, numbers))
print(f"Original: {numbers}")
print(f"Positive: {positive}")

# With lambda
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even: {even}")
print()

# ============================================================================
# EXAMPLE 23: Nested Functions
# ============================================================================
# Functions inside functions

print("Example 23: Nested Functions")
print("-" * 50)

def outer(x):
    def inner(y):
        return x + y
    
    return inner

add_5 = outer(5)
print(f"add_5(3) = {add_5(3)}")
print(f"add_5(7) = {add_5(7)}")

add_10 = outer(10)
print(f"add_10(3) = {add_10(3)}")
print()

# ============================================================================
# EXAMPLE 24: Recursion
# ============================================================================
# Function calling itself

print("Example 24: Recursion")
print("-" * 50)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")
print(f"factorial(3) = {factorial(3)}")

def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(3)
print()

# ============================================================================
# EXAMPLE 25: Function Composition
# ============================================================================
# Combine functions

print("Example 25: Function Composition")
print("-" * 50)

def add_10(x):
    return x + 10

def multiply_2(x):
    return x * 2

def compose(f, g):
    return lambda x: f(g(x))

# First multiply by 2, then add 10
combined = compose(add_10, multiply_2)
result = combined(5)  # (5 * 2) + 10 = 20
print(f"(5 * 2) + 10 = {result}")

# Apply operations step by step
x = 5
x = multiply_2(x)
x = add_10(x)
print(f"Step by step: {x}")

