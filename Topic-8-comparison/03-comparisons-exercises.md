# Topic 8: Comparisons - Exercises

## Overview

These exercises teach you to use comparisons for decision-making. You'll progress from simple equality checks to complex multi-condition scenarios.

---

## Exercise 1: Simple Equality Check

**Write a program that:**
- Asks user for two numbers
- Compares if they're equal
- Displays whether they match

**Example interaction:**
```
First number: 5
Second number: 5
Are they equal? True

First number: 5
Second number: 3
Are they equal? False
```

**Concepts:** Equality operator (==)

---

## Exercise 2: Ordering Comparisons

**Write a program that:**
- Asks user for two numbers
- Tests all ordering relationships
- Displays which is larger, smaller, or equal

**Example output:**
```
First: 10, Second: 7
10 > 7: True
10 < 7: False
10 == 7: False
10 >= 7: True
10 <= 7: False
```

**Concepts:** <, >, <=, >= operators

---

## Exercise 3: String Comparison

**Write a program that:**
- Asks for two words
- Compares them alphabetically
- Shows which comes first

**Example interaction:**
```
Word 1: apple
Word 2: banana
"apple" comes before "banana"

Word 1: zebra
Word 2: apple
"zebra" comes after "apple"
```

**Concepts:** String comparison, alphabetical order

---

## Exercise 4: Age Eligibility

**Write a program that:**
- Asks for age
- Checks eligibility for different activities
- Voting (>= 18)
- Buying alcohol (>= 21)
- Senior discount (>= 65)

**Example interaction:**
```
Age: 25
✓ Can vote
✓ Can buy alcohol
✗ Not senior age
```

**Concepts:** Comparison operators, multiple checks

---

## Exercise 5: Grade Assignment

**Write a program that:**
- Asks for a test score
- Assigns grade based on ranges
- A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60

**Example interaction:**
```
Score: 85
Grade: B

Score: 93
Grade: A

Score: 55
Grade: F
```

**Concepts:** Comparison chains (80 <= score < 90)

---

## Exercise 6: Password Validation

**Write a program that:**
- Asks for a password
- Checks if it meets requirements:
  - At least 8 characters long
  - Not a common password
- Reports each check

**Example interaction:**
```
Password: hello
Length >= 8: False ✗
Valid: NO (too short)

Password: mypassword123
Length >= 8: True ✓
Not forbidden: True ✓
Valid: YES
```

**Concepts:** Multiple conditions, membership testing (in)

---

## Exercise 7: Range Validation

**Write a program that:**
- Asks for a value
- Checks if it's within acceptable range
- Range: 0-100 (e.g., percentage, score)
- Reports valid or out of range

**Example interaction:**
```
Enter percentage: 85
Valid: True ✓

Enter percentage: 150
Valid: False ✗ (exceeds 100)

Enter percentage: -5
Valid: False ✗ (below 0)
```

**Concepts:** Comparison chains (0 <= value <= 100)

---

## Exercise 8: Login System

**Write a program that:**
- Stores correct username and password
- Asks user for credentials
- Compares with stored values (case-sensitive)
- Reports login success or failure

**Example interaction:**
```
Username: alice
Password: secret123
✓ Login successful

Username: Alice
Password: secret123
✗ Invalid username (case matters)
```

**Concepts:** String equality, case sensitivity

---

## Exercise 9: Multiple Conditions (Loan Approval)

**Write a program that:**
- Asks for age, income, and credit score
- Checks eligibility (all must be true):
  - Age >= 18
  - Income >= 30000
  - Credit score >= 650
- Reports approved or denied

**Example interaction:**
```
Age: 25
Income: 50000
Credit score: 720
✓ APPROVED

Age: 25
Income: 20000
Credit score: 720
✗ DENIED (income too low)
```

**Concepts:** Multiple conditions with AND logic

---

## Exercise 10: Inventory Status

**Write a program that:**
- Asks for item stock level and minimum threshold
- Reports status:
  - "REORDER" if stock < minimum
  - "LOW" if minimum <= stock < minimum * 1.5
  - "OK" if stock >= minimum * 1.5
- Test with multiple items

**Example interaction:**
```
Item: Widget
Stock: 5
Minimum: 10
Status: REORDER

Item: Gadget
Stock: 15
Minimum: 10
Status: OK
```

**Concepts:** Comparison chains, categorization logic

---

## Challenge Exercises (Optional)

### Challenge 1: Temperature Scale Conversion and Checking
- Convert between Celsius and Fahrenheit
- Compare with safety thresholds
- Report if freezing, normal, hot, or critical

### Challenge 2: Overtime Pay Calculator
- Ask for hours worked and hourly rate
- Check if hours > 40 (overtime)
- Calculate overtime pay (1.5x rate)
- Compare regular vs overtime earnings

### Challenge 3: Eligibility Checker
- Create a system with multiple overlapping criteria
- Example: Movie ratings (G, PG, PG-13, R)
- Based on age, report which movies are appropriate

### Challenge 4: Data Validation Pipeline
- Create a program that validates multiple data fields
- Each field has different comparison rules
- Report which fields pass/fail validation
- Show specific reason for each failure

---

## Tips for Success

1. **Use clear variable names:** `score`, `minimum`, `age` are clearer than `x`, `y`, `z`
2. **Test edge cases:** What happens at exact boundaries?
3. **Case sensitivity matters:** "Alice" ≠ "alice"
4. **Comparison chains are elegant:** Use `0 <= x <= 100` instead of `x >= 0 and x <= 100`
5. **Store results:** `is_valid = value >= minimum` makes code readable

---

## Key Takeaways

After these exercises, you should:
- ✅ Use all comparison operators correctly
- ✅ Compare different data types
- ✅ Understand equality vs inequality
- ✅ Test ordering relationships
- ✅ Use comparison chains
- ✅ Combine multiple conditions
- ✅ Validate real-world data
- ✅ Debug comparison logic

