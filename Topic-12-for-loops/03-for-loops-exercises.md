# Topic 12: For Loops - Exercises

## Overview

These exercises teach you to iterate over sequences with for loops. You'll progress from simple iteration to transforming data and using list comprehensions.

---

## Exercise 1: Simple Iteration

**Write a program that:**
- Creates list of 5 numbers
- Loops through with for loop
- Prints each number

**Example output:**
```
10
20
30
40
50
```

**Concepts:** Basic for loop, list iteration

---

## Exercise 2: Loop Over String

**Write a program that:**
- Takes a word as input
- Loops through each character
- Prints each character on separate line

**Example output:**
```
h
e
l
l
o
```

**Concepts:** String iteration, character access

---

## Exercise 3: Using Range

**Write a program that:**
- Uses for loop with range()
- Counts from 1 to 10
- Displays each number

**Example output:**
```
1
2
3
...
10
```

**Concepts:** range() function, numeric loops

---

## Exercise 4: Sum All Items

**Write a program that:**
- Creates list of numbers
- Uses for loop to sum them
- Displays total

**Example interaction:**
```
Numbers: [10, 20, 30, 40, 50]
Sum: 150
```

**Concepts:** Accumulation pattern, for loop arithmetic

---

## Exercise 5: Find Maximum

**Write a program that:**
- Creates list of numbers
- Finds maximum using for loop
- Displays max value

**Example output:**
```
Numbers: [45, 23, 89, 12, 56]
Maximum: 89
```

**Concepts:** Comparison in loops, tracking maximum

---

## Exercise 6: Using Enumerate

**Write a program that:**
- Creates list of items
- Uses enumerate() to get index and item
- Displays both

**Example output:**
```
0: apple
1: banana
2: cherry
```

**Concepts:** enumerate(), index tracking, tuple unpacking

---

## Exercise 7: Filter Items

**Write a program that:**
- Creates list of numbers
- Filters even numbers using for loop
- Displays filtered list

**Example output:**
```
Original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers: [2, 4, 6, 8, 10]
```

**Concepts:** Conditional in loops, filtering, append()

---

## Exercise 8: Transform Data

**Write a program that:**
- Creates list of numbers
- Squares each number in loop
- Displays transformed list

**Example output:**
```
Original: [1, 2, 3, 4, 5]
Squared: [1, 4, 9, 16, 25]
```

**Concepts:** Data transformation, building new lists

---

## Exercise 9: Nested Loops - Grid

**Write a program that:**
- Uses nested for loops
- Creates 3x3 grid of asterisks
- Each row on new line

**Example output:**
```
* * *
* * *
* * *
```

**Concepts:** Nested loops, pattern output, print formatting

---

## Exercise 10: List Comprehension

**Write a program that:**
- Creates list using list comprehension
- Filters items in one line
- Demonstrates efficiency

**Example:**
```
# Traditional way (10 lines)
result = []
for x in [1, 2, 3, 4, 5]:
    if x > 2:
        result.append(x * 2)

# Comprehension way (1 line)
result = [x * 2 for x in [1, 2, 3, 4, 5] if x > 2]
# Result: [6, 8, 10]
```

**Concepts:** List comprehensions, one-line filtering/transformation

---

## Challenge Exercises (Optional)

### Challenge 1: Two-List Processing
- Take two lists of same length
- Use zip() to iterate both together
- Perform operation on pairs
- Example: combine first names and last names

### Challenge 2: Matrix Operations
- Create 3x3 matrix (list of lists)
- Use nested loops to process all elements
- Calculate row sums, column sums, or diagonal
- Display results formatted

### Challenge 3: Data Analyzer
- Process list of numbers
- Calculate: sum, average, min, max, count
- Find values above/below average
- Display statistics report

### Challenge 4: Text Processor
- Process input text line by line
- Count words, characters, sentences
- Find longest word
- Display analysis

---

## Tips for Success

1. **Choose right approach:** for vs while, direct iteration vs range
2. **Use enumerate:** When you need both index and item
3. **List comprehension:** When transforming small lists
4. **Break/continue:** Exit or skip efficiently
5. **Test with small data:** Debug logic with manageable lists

---

## Key Takeaways

After these exercises, you should:
- ✅ Iterate over sequences with for loops
- ✅ Use range() for numeric sequences
- ✅ Loop over strings and lists
- ✅ Use enumerate() for indices
- ✅ Filter and transform data
- ✅ Use nested loops
- ✅ Apply list comprehensions
- ✅ Choose between for and while

