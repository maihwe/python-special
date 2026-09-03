# Topic 13: Lists - Exercises

## Overview

These exercises teach you to create and manipulate lists. You'll progress from basic creation and access to complex data operations and transformations.

---

## Exercise 1: Create and Access

**Write a program that:**
- Creates list of 5 numbers
- Accesses first, last, and middle items
- Displays each with index

**Example output:**
```
List: [10, 20, 30, 40, 50]
First (index 0): 10
Middle (index 2): 30
Last (index -1): 50
```

**Concepts:** List creation, indexing, positive/negative indices

---

## Exercise 2: Slicing

**Write a program that:**
- Creates list of 10 numbers
- Demonstrates different slices
- Shows first 3, last 3, every other, reversed

**Example output:**
```
List: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
First 3: [0, 1, 2]
Last 3: [7, 8, 9]
Every other: [0, 2, 4, 6, 8]
Reversed: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

**Concepts:** Slice notation, start:stop:step

---

## Exercise 3: Append and Extend

**Write a program that:**
- Starts with empty list
- Appends single items
- Extends with multiple items
- Shows list after each operation

**Example output:**
```
Start: []
Append 1: [1]
Append 2: [1, 2]
Extend [3, 4, 5]: [1, 2, 3, 4, 5]
```

**Concepts:** append(), extend(), list building

---

## Exercise 4: Remove and Pop

**Write a program that:**
- Creates list of items
- Removes items by value
- Pops items by index
- Shows operations

**Example interaction:**
```
List: [1, 2, 3, 4, 5]
Remove 3: [1, 2, 4, 5]
Pop first: 1 [2, 4, 5]
Pop last: 5 [2, 4]
```

**Concepts:** remove(), pop(), list modification

---

## Exercise 5: Sort and Reverse

**Write a program that:**
- Creates list of numbers in random order
- Sorts ascending
- Shows sorted version
- Shows reversed version

**Example output:**
```
Original: [3, 1, 4, 1, 5, 9, 2, 6]
Sorted: [1, 1, 2, 3, 4, 5, 6, 9]
Reversed: [9, 6, 5, 4, 3, 2, 1, 1]
```

**Concepts:** sort(), reverse(), in-place modification

---

## Exercise 6: List Methods - Count and Index

**Write a program that:**
- Creates list with some duplicate values
- Uses count() to find occurrences
- Uses index() to find positions
- Handles items that don't exist

**Example output:**
```
List: [1, 2, 3, 2, 4, 2, 5]
Count of 2: 3
Count of 99: 0
Index of 3: 2
Index of 2: 1 (first occurrence)
```

**Concepts:** count(), index(), searching lists

---

## Exercise 7: List Copy - References vs Copies

**Write a program that:**
- Shows difference between reference and copy
- Modifies copy and reference separately
- Demonstrates how changes affect each

**Example output:**
```
Original: [1, 2, 3]
After modifying copy: Original stays [1, 2, 3]
After modifying reference: Original becomes [1, 2, 3, 99]
```

**Concepts:** Mutability, references, copy(), shallow copy

---

## Exercise 8: Statistics - Sum, Average, Max, Min

**Write a program that:**
- Reads list of grades
- Calculates sum, average, maximum, minimum
- Displays all statistics

**Example output:**
```
Grades: [85, 92, 78, 95, 88]
Sum: 438
Average: 87.6
Maximum: 95
Minimum: 78
```

**Concepts:** sum(), len(), max(), min(), statistics

---

## Exercise 9: List Comprehension

**Write a program that:**
- Demonstrates list comprehensions
- Transform numbers (square)
- Filter numbers (even only)
- Transform strings (uppercase)

**Example output:**
```
Squares: [1, 4, 9, 16, 25]
Evens: [2, 4, 6, 8, 10]
Uppercase: ["HELLO", "WORLD"]
```

**Concepts:** List comprehensions, filtering, transformation

---

## Exercise 10: Nested Lists - 2D Operations

**Write a program that:**
- Creates 3x3 matrix (list of lists)
- Displays matrix
- Accesses specific elements
- Calculates row and column sums

**Example output:**
```
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Element at [1][2]: 6
Row 0 sum: 6
Column 0 sum: 12
```

**Concepts:** Nested lists, 2D indexing, matrix operations

---

## Challenge Exercises (Optional)

### Challenge 1: Grade Analyzer
- Read list of grades
- Calculate average, highest, lowest
- Count how many pass (>=70), fail (<70)
- Show grade distribution (A, B, C, D, F)

### Challenge 2: Duplicate Finder
- Given list with duplicates
- Find all items that appear more than once
- Show count for each duplicate
- Remove duplicates and show unique list

### Challenge 3: List Operations Lab
- Implement custom operations without methods
- Find max without max() function
- Reverse without reverse() function
- Sort bubble sort implementation

### Challenge 4: Data Processing
- Create list of dictionaries (student records)
- Sort by grade
- Filter by criteria
- Calculate class statistics

---

## Tips for Success

1. **Test methods:** Try each list method to understand what it does
2. **Watch out for mutations:** Remember lists change in place
3. **Use copies carefully:** Know when you need copy() vs slice
4. **Comprehensions are powerful:** But keep them readable
5. **Nested lists:** Use clear indexing with bracket notation

---

## Key Takeaways

After these exercises, you should:
- ✅ Create lists and access elements
- ✅ Slice lists to get subsequences
- ✅ Add, remove, and modify items
- ✅ Sort and reverse lists
- ✅ Search for items (count, index)
- ✅ Understand references and copies
- ✅ Calculate statistics (sum, avg, max, min)
- ✅ Use list comprehensions
- ✅ Work with nested lists

