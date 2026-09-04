# Topic 14: Dictionaries - Exercises

## Overview

These exercises teach you to use dictionaries for storage and lookup. You'll progress from basic creation and access to complex data operations and transformations.

---

## Exercise 1: Create and Access

**Write a program that:**
- Creates dictionary with 5 key-value pairs
- Accesses values by key
- Displays key-value pairs

**Example output:**
```
Dictionary: {'name': 'Alice', 'age': 30, 'city': 'Boston', 'job': 'Engineer', 'salary': 100000}
name: Alice
age: 30
city: Boston
```

**Concepts:** Dictionary creation, key access

---

## Exercise 2: Safe Access with get()

**Write a program that:**
- Creates dictionary
- Uses get() to safely access keys
- Shows difference between direct access and get()
- Provides default values

**Example output:**
```
grades = {'Alice': 85, 'Bob': 92}
grades.get('Alice') = 85
grades.get('Unknown') = None
grades.get('Unknown', 0) = 0
```

**Concepts:** get() method, safe access, default values

---

## Exercise 3: Adding and Modifying

**Write a program that:**
- Starts with small dictionary
- Adds new key-value pairs
- Modifies existing values
- Shows dictionary after each operation

**Example output:**
```
Start: {'name': 'Alice'}
After adding age: {'name': 'Alice', 'age': 30}
After changing age to 31: {'name': 'Alice', 'age': 31}
```

**Concepts:** Adding entries, modifying values

---

## Exercise 4: Removing Entries

**Write a program that:**
- Creates dictionary
- Removes entries using del and pop()
- Shows results after removal
- Demonstrates pop() return value

**Example output:**
```
Start: {'a': 1, 'b': 2, 'c': 3}
After del dict['b']: {'a': 1, 'c': 3}
Popped 'c': 3
Final: {'a': 1}
```

**Concepts:** del statement, pop() method, removal

---

## Exercise 5: Dictionary Methods

**Write a program that:**
- Creates dictionary
- Demonstrates keys(), values(), items()
- Shows all key-value pairs
- Counts total entries

**Example output:**
```
Dictionary: {'Alice': 85, 'Bob': 92, 'Charlie': 78}
Keys: ['Alice', 'Bob', 'Charlie']
Values: [85, 92, 78]
Items: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
Length: 3
```

**Concepts:** keys(), values(), items(), len()

---

## Exercise 6: Looping Over Dictionary

**Write a program that:**
- Creates dictionary of student grades
- Loops over all key-value pairs
- Displays formatted output
- Calculates statistics

**Example output:**
```
Grades:
  Alice: 85
  Bob: 92
  Charlie: 78
Average: 85.0
```

**Concepts:** Iteration, items(), statistics

---

## Exercise 7: Counting Occurrences

**Write a program that:**
- Takes text input
- Counts each character/word
- Stores in dictionary
- Displays counts

**Example output:**
```
Text: "hello world"
Character counts:
  h: 1
  e: 1
  l: 3
  o: 2
  (etc.)
```

**Concepts:** Counting pattern, get(), dictionary building

---

## Exercise 8: Nested Dictionaries

**Write a program that:**
- Creates nested dictionary structure
- Accesses nested values
- Modifies nested data
- Displays formatted output

**Example output:**
```
Inventory:
  apple: price=$1.50, stock=100
  milk: price=$3.00, stock=50
Update apple stock to 90
Total value: $435.00
```

**Concepts:** Nested access, data structures

---

## Exercise 9: Dictionary Comprehension

**Write a program that:**
- Creates dictionaries using comprehension
- Transforms data
- Filters entries
- Shows original and result

**Example output:**
```
Numbers 1-5 squared: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Even squares only: {2: 4, 4: 16}
Doubled: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
```

**Concepts:** Dictionary comprehensions, filtering

---

## Exercise 10: Dictionary Transformation

**Write a program that:**
- Takes lists of paired data
- Converts to dictionary
- Transforms dictionary values
- Shows all stages

**Example output:**
```
Names: ['Alice', 'Bob', 'Charlie']
Scores: [85, 92, 78]
Grade dict: {'Alice': 85, 'Bob': 92, 'Charlie': 78}
Curved (+5): {'Alice': 90, 'Bob': 97, 'Charlie': 83}
```

**Concepts:** Creating dicts from lists, transformations

---

## Challenge Exercises (Optional)

### Challenge 1: Contact Manager
- Store contact records (name, phone, email, address)
- Add, remove, search contacts
- Display all contacts formatted
- Update contact information

### Challenge 2: Word Frequency Analysis
- Read text input
- Count word frequencies
- Find most common word
- Filter words by minimum count
- Display statistics

### Challenge 3: Product Inventory
- Store product data (price, quantity, category)
- Calculate total inventory value
- Find products below stock threshold
- Update prices by category
- Generate inventory report

### Challenge 4: Student Management System
- Store student records with grades for multiple courses
- Calculate GPA per student
- Find top students
- Calculate class statistics
- Group students by performance level

---

## Tips for Success

1. **Check before accessing:** Use `in` or `.get()` to avoid KeyError
2. **Understand mutability:** Dictionaries change in place like lists
3. **Use meaningful keys:** Make keys descriptive for readability
4. **Nested structures:** Organize complex data hierarchically
5. **Iteration patterns:** Use `.items()` for key-value pairs

---

## Key Takeaways

After these exercises, you should:
- ✅ Create dictionaries with literal syntax and dict()
- ✅ Access values safely by key
- ✅ Add, modify, and remove entries
- ✅ Use dictionary methods
- ✅ Iterate over keys, values, and items
- ✅ Work with nested dictionaries
- ✅ Use dictionary comprehensions
- ✅ Count and group data
- ✅ Transform and filter dictionaries
- ✅ Choose between lists and dictionaries

