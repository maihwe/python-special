# Topic 10: Logical Operators - Exercises

## Overview

These exercises teach you to combine conditions elegantly using logical operators. You'll progress from simple and/or/not to complex multi-factor decisions used in real applications.

---

## Exercise 1: Simple 'and' Usage

**Write a program that:**
- Asks for age and if they have a driver's license
- Uses 'and' to check both conditions
- Reports whether they can drive

**Example interaction:**
```
Age: 25
Have license (yes/no): yes
✓ Can drive

Age: 25
Have license (yes/no): no
✗ Cannot drive (missing license)
```

**Concepts:** and operator, multiple conditions

---

## Exercise 2: Simple 'or' Usage

**Write a program that:**
- Asks if it's weekend or if it's holiday
- Uses 'or' to check either condition
- Reports if user has day off

**Example interaction:**
```
Is weekend? yes
Is holiday? no
✓ Day off

Is weekend? no
Is holiday? no
✗ Regular work day
```

**Concepts:** or operator, alternative conditions

---

## Exercise 3: Using 'not'

**Write a program that:**
- Asks if it's raining
- Uses 'not' to invert the condition
- Reports appropriate activity

**Example interaction:**
```
Is it raining? yes
✗ Stay inside

Is it raining? no
✓ Go outside
```

**Concepts:** not operator, inversion

---

## Exercise 4: Combining 'and' and 'or'

**Write a program that:**
- Asks for income level, credit score, employment years
- Check eligibility with: (income >= 30000 or has_savings) and credit_score >= 650
- Reports loan eligibility

**Example interaction:**
```
Income: 50000
Credit score: 700
Employment years: 3
✓ APPROVED

Income: 20000
Credit score: 750
✗ DENIED
```

**Concepts:** Mixed logical operators, complex conditions

---

## Exercise 5: Operator Precedence

**Write a program that:**
- Demonstrates operator precedence
- Shows how 'and' is evaluated before 'or'
- Proves: A or B and C = A or (B and C)

**Example output:**
```
True or False and False
Result: True
(Because: True or (False and False) = True or False = True)

(True or False) and False
Result: False
(Different grouping gives different result)
```

**Concepts:** Precedence, parentheses, evaluation order

---

## Exercise 6: De Morgan's Laws

**Write a program that:**
- Demonstrates De Morgan's Laws
- Shows: not (A and B) = (not A) or (not B)
- Shows: not (A or B) = (not A) and (not B)

**Example output:**
```
Testing: not (x >= 5 and y <= 10)
With x=3, y=8:
Method 1: not (True and True) = False
Method 2: (not True) or (not True) = False
✓ Both methods equal
```

**Concepts:** De Morgan's Laws, simplification, equivalence

---

## Exercise 7: Real-World: Access Control

**Write a program that:**
- Simulates access control with multiple roles
- User can access if: is_admin OR (is_owner AND file_not_archived) OR is_manager
- Test with different role combinations

**Example interaction:**
```
Role: editor
Is owner: yes
Is archived: no
✓ Access granted

Role: viewer
Is owner: no
Is archived: no
✗ Access denied
```

**Concepts:** Multi-role permissions, complex logic

---

## Exercise 8: Data Validation

**Write a program that:**
- Validates a password with multiple requirements
- Must have: length >= 8 AND (uppercase OR digits) AND (lowercase OR special chars)
- Reports validation result and missing requirements

**Example interaction:**
```
Password: Pass123!
Length >= 8: ✓
Has uppercase: ✓
Has lowercase: ✓
Has digit or special: ✓
✓ VALID

Password: pass
✗ INVALID
  - Too short (< 8)
  - Missing uppercase
```

**Concepts:** Multiple conditions, validation logic

---

## Exercise 9: Discount Eligibility (Complex)

**Write a program that:**
- User gets discount if ANY of:
  - Purchase >= $100
  - Is member AND purchase >= $50
  - Has coupon AND not expired
- Multiple discount levels based on conditions

**Example interaction:**
```
Purchase: $150
Member: no
Has coupon: no
✓ Gets 10% discount (large purchase)

Purchase: $60
Member: yes
Has coupon: no
✓ Gets 5% discount (member)
```

**Concepts:** Multiple paths, conditional logic, real-world scenario

---

## Exercise 10: Short-Circuit Behavior

**Write a program that:**
- Demonstrates short-circuit evaluation
- Shows that second condition isn't always evaluated
- Includes functions with side effects to show the difference

**Example output:**
```
Test: x == 5 and expensive_function()
x = 3: expensive_function() was NOT called
       (Result known after first condition)

x = 5: expensive_function() WAS called
       (Had to evaluate second condition)
```

**Concepts:** Short-circuit evaluation, efficiency, function calls

---

## Challenge Exercises (Optional)

### Challenge 1: Access Control Matrix
- Create a system with multiple user types and resources
- Different permissions based on role AND resource type
- Test various user/resource combinations

### Challenge 2: Spam Detector
- Implement spam detection with multiple indicators
- Score based on: sender reputation, link count, message length, etc.
- Report likelihood (low/medium/high/definite spam)

### Challenge 3: Insurance Qualification
- Evaluate insurance qualification with multiple criteria
- Age range, health conditions, driving record, etc.
- Calculate eligibility and premium tier

### Challenge 4: Game NPC AI
- Create NPC behavior with complex conditions
- Different actions based on: health, enemy presence, resources, etc.
- Demonstrate priority of conditions

---

## Tips for Success

1. **Name your conditions:** `is_age_ok`, `is_income_ok` instead of inline logic
2. **Use parentheses liberally:** Makes precedence explicit
3. **Test edge cases:** What about exactly at boundaries?
4. **Break complex logic:** Use variables to store intermediate results
5. **Think in layers:** Check must-have conditions first (and), then nice-to-have (or)

---

## Key Takeaways

After these exercises, you should:
- ✅ Combine conditions with and, or, not
- ✅ Understand operator precedence
- ✅ Know when to use each operator
- ✅ Apply De Morgan's Laws
- ✅ Leverage short-circuit evaluation
- ✅ Write readable complex conditions
- ✅ Solve real-world multi-factor problems
- ✅ Debug logical expressions

