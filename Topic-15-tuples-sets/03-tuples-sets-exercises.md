# Topic 15: Tuples and Sets - Exercises

## Overview

These exercises teach you to use tuples for immutable sequences and sets for unique unordered collections. You'll progress from basic creation and operations to solving real-world problems.

---

## Exercise 1: Creating and Using Tuples

**Write a program that:**
- Creates tuple with 5 items
- Accesses items by index
- Uses negative indexing
- Demonstrates immutability attempt

**Example output:**
```
Tuple: (10, 20, 30, 40, 50)
First: 10
Last: 50
Middle: 30
Attempting to change tuple[0] = 99 → ERROR!
```

**Concepts:** Tuple creation, indexing, immutability

---

## Exercise 2: Tuple Slicing

**Write a program that:**
- Creates tuple of numbers
- Demonstrates various slicing techniques
- Shows subsequences
- Shows reversal

**Example output:**
```
Tuple: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
First 3: (0, 1, 2)
Last 3: (7, 8, 9)
Every other: (0, 2, 4, 6, 8)
Reversed: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

**Concepts:** Slicing, subsequences, reversal

---

## Exercise 3: Tuple Unpacking

**Write a program that:**
- Creates tuples of various sizes
- Unpacks into variables
- Demonstrates unpacking in different contexts
- Shows swapping with unpacking

**Example output:**
```
Unpack (1, 2): x=1, y=2
Unpack (1, 2, 3): a=1, b=2, c=3
Before swap: a=10, b=20
After swap: a=20, b=10
```

**Concepts:** Unpacking, tuple assignment, swapping

---

## Exercise 4: Tuples in Loops

**Write a program that:**
- Creates list of tuples
- Unpacks tuples in for loop
- Processes data from tuples
- Collects results

**Example output:**
```
Points: [(1, 2), (3, 4), (5, 6)]
Unpacking:
  (1, 2)
  (3, 4)
  (5, 6)
```

**Concepts:** Iteration, unpacking, tuple processing

---

## Exercise 5: Tuples as Dictionary Keys

**Write a program that:**
- Creates dictionary with tuple keys
- Accesses values by tuple key
- Demonstrates why tuples work as keys
- Shows board/position example

**Example output:**
```
Board positions:
  (0, 0): start
  (1, 0): north
  (0, 1): east
Position (1, 0): north
```

**Concepts:** Hashability, dictionary keys, immutability

---

## Exercise 6: Creating Sets

**Write a program that:**
- Creates sets from literals
- Creates set from list
- Shows automatic duplicate removal
- Demonstrates empty set creation

**Example output:**
```
Set from literals: {1, 2, 3}
Set from list: {1, 2, 3, 4}
List had duplicates, set removed them
Empty set: set()
```

**Concepts:** Set creation, duplicate removal, set()

---

## Exercise 7: Set Operations - Union

**Write a program that:**
- Creates two sets
- Finds union (all items)
- Demonstrates both syntax (| and .union())
- Shows real-world example

**Example output:**
```
Set a: {1, 2, 3}
Set b: {2, 3, 4}
Union (a | b): {1, 2, 3, 4}
All items: {1, 2, 3, 4}
```

**Concepts:** Union, combining sets, all items

---

## Exercise 8: Set Operations - Intersection

**Write a program that:**
- Creates two sets
- Finds intersection (common items)
- Demonstrates both syntax (& and .intersection())
- Shows with word/skill example

**Example output:**
```
Set a: {1, 2, 3}
Set b: {2, 3, 4}
Intersection (a & b): {2, 3}
Common items only
```

**Concepts:** Intersection, common items, set operations

---

## Exercise 9: Set Operations - Difference

**Write a program that:**
- Creates two sets
- Finds difference (in a but not b)
- Shows symmetric difference
- Real-world application

**Example output:**
```
Set a: {1, 2, 3}
Set b: {2, 3, 4}
Difference (a - b): {1}
Items only in a: {1}
```

**Concepts:** Difference, symmetric difference, exclusion

---

## Exercise 10: Removing Duplicates

**Write a program that:**
- Takes list with duplicate items
- Converts to set (removes duplicates)
- Converts back to list
- Shows statistics

**Example output:**
```
List with duplicates: [1, 2, 2, 3, 3, 3, 4]
As set: {1, 2, 3, 4}
Unique count: 4
Removed: 3 duplicates
```

**Concepts:** Deduplication, set conversion, statistics

---

## Challenge Exercises (Optional)

### Challenge 1: Venn Diagram
- Create three sets (e.g., programming languages known by people)
- Calculate all intersections, unions, differences
- Visualize relationships
- Generate summary statistics

### Challenge 2: Word Analysis
- Read text and split into words
- Remove duplicates with set
- Find common words between texts
- Identify unique words per text
- Generate frequency report

### Challenge 3: Game Board Position Tracking
- Create game board with position tuples as keys
- Store game objects at positions
- Move objects (change position)
- Query nearby positions
- Track movement history as tuples

### Challenge 4: Student Skills Matcher
- Store students with skill sets
- Find students with common skills
- Recommend skill combinations
- Find skill gaps per student
- Generate matching suggestions

---

## Tips for Success

1. **Remember comma:** Single element tuples need comma: (42,)
2. **Immutability:** Tuples can't change - helps prevent bugs
3. **Set uniqueness:** Sets automatically remove duplicates
4. **Fast lookup:** Sets are much faster for membership checks
5. **Right tool:** Choose tuple, set, list, or dict based on need

---

## Key Takeaways

After these exercises, you should:
- ✅ Create and index tuples
- ✅ Understand immutability benefits
- ✅ Unpack tuples efficiently
- ✅ Use tuples as dictionary keys
- ✅ Create sets and remove duplicates
- ✅ Perform set operations (union, intersection, difference)
- ✅ Check set membership efficiently
- ✅ Choose between collections
- ✅ Solve real-world collection problems

