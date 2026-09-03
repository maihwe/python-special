# Topic 9: If/Else - Exercises

## Overview

These exercises teach decision-making in programs. You'll progress from simple if statements to complex nested conditions with multiple criteria.

---

## Exercise 1: Simple If Statement

**Write a program that:**
- Asks user for age
- Checks if they can vote (>= 18)
- Displays appropriate message

**Example interaction:**
```
Age: 20
✓ You can vote

Age: 16
✗ You cannot vote yet
```

**Concepts:** if/else, comparison operators

---

## Exercise 2: Two-Branch Decision

**Write a program that:**
- Asks for test score
- Determines pass/fail (>= 70 is pass)
- Shows if they passed or failed

**Example interaction:**
```
Score: 75
✓ PASS

Score: 65
✗ FAIL
```

**Concepts:** if/else structure, comparisons

---

## Exercise 3: Multiple Branches with Elif

**Write a program that:**
- Asks for a number
- Categorizes it:
  - Positive (> 0)
  - Negative (< 0)
  - Zero (== 0)

**Example interaction:**
```
Number: 5
Positive

Number: -3
Negative

Number: 0
Zero
```

**Concepts:** elif, multiple conditions

---

## Exercise 4: Nested If Statements

**Write a program that:**
- Asks for username and password
- Checks if credentials are correct
- If both correct, ask for additional verification
- Grant access only if all checks pass

**Example interaction:**
```
Username: alice
Password: secret123
Username: ✓ correct
Password: ✓ correct
2FA code: 123456
✓ ACCESS GRANTED
```

**Concepts:** Nested if statements, multiple levels

---

## Exercise 5: Logical 'and' Operator

**Write a program that:**
- Asks for age and if they have a license
- Determines if they can rent a car
- Requires BOTH age >= 21 AND license = yes

**Example interaction:**
```
Age: 25
License (yes/no): yes
✓ Can rent a car

Age: 25
License (yes/no): no
✗ Cannot rent (no license)
```

**Concepts:** Logical 'and' operator

---

## Exercise 6: Logical 'or' Operator

**Write a program that:**
- Asks if it's a weekend
- Asks if it's a holiday
- Determines if they have the day off
- Day off if EITHER is true

**Example interaction:**
```
Is it weekend? yes
Is it holiday? no
✓ You have the day off

Is it weekend? no
Is it holiday? no
✗ Regular work day
```

**Concepts:** Logical 'or' operator

---

## Exercise 7: Grade Assignment with Elif

**Write a program that:**
- Asks for test score
- Assigns letter grade:
  - A: 90-100
  - B: 80-89
  - C: 70-79
  - D: 60-69
  - F: below 60

**Example interaction:**
```
Score: 85
Grade: B

Score: 92
Grade: A

Score: 55
Grade: F
```

**Concepts:** elif chains, comparison ranges

---

## Exercise 8: Multiple Conditions with 'and'

**Write a program that:**
- Asks for username, password, and 2FA code
- Checks all three
- Login only succeeds if ALL are correct

**Example interaction:**
```
Username: alice
Password: secret
2FA: 123456
✓ Login successful

Username: alice
Password: wrong
2FA: 123456
✗ Login failed
```

**Concepts:** Multiple 'and' conditions, validation

---

## Exercise 9: Real-World: Loan Eligibility

**Write a comprehensive program that:**
- Asks for age, income, and credit score
- Checks multiple eligibility criteria:
  - Age >= 18
  - Income >= $30,000
  - Credit score >= 700
- Reports approved/denied
- If denied, shows which requirements failed

**Example interaction:**
```
Age: 25
Income: 50000
Credit score: 750
✓ APPROVED

Age: 25
Income: 20000
Credit score: 750
✗ DENIED
  - Income requirement not met ($30,000 minimum)
```

**Concepts:** Complex conditions, detailed feedback

---

## Exercise 10: Inventory Management System

**Write a program that:**
- Asks for item name, current stock, and minimum level
- Categorizes stock status:
  - "REORDER" if stock < minimum
  - "LOW" if minimum <= stock < minimum × 1.5
  - "OK" if stock >= minimum × 1.5
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

**Concepts:** Nested conditions, ranges, categorization

---

## Challenge Exercises (Optional)

### Challenge 1: Discount Calculator
- Calculate discounts based on multiple criteria
- Amount purchased, customer loyalty level, current promotions
- Compound multiple discount conditions

### Challenge 2: Time-Based Access Control
- Grant access based on current time
- Different permissions for different hours
- Handle edge cases (midnight, etc.)

### Challenge 3: Number Classification
- Classify numbers as prime, even, odd, perfect square, etc.
- Multiple overlapping categories
- Show all applicable classifications

### Challenge 4: Nested Decision Tree
- Create a complex decision tree (like a quiz)
- Multiple branching paths
- Different outcomes based on cumulative answers

---

## Tips for Success

1. **Use meaningful variable names:** `age`, `has_license`, `is_valid`
2. **Break down complex conditions:** Name them separately for clarity
3. **Test edge cases:** What about exact boundaries?
4. **Use indentation:** Python requires it; use 4 spaces
5. **Trace your logic:** Walk through different inputs mentally

---

## Key Takeaways

After these exercises, you should:
- ✅ Write if/else statements correctly
- ✅ Use elif for multiple branches
- ✅ Nest conditions properly
- ✅ Combine conditions with 'and', 'or', 'not'
- ✅ Handle real-world decision scenarios
- ✅ Debug conditional logic
- ✅ Make code readable and maintainable
- ✅ Validate user input properly

