# Topic 5: Type Conversion - Exercises

## Overview

These exercises build from simple conversions to complex validation and calculation workflows. Each exercise reinforces the importance of converting between types at the right time.

---

## Exercise 1: Simple String to Integer

**Write a program that:**
- Asks the user for a number (as text)
- Converts it to an integer
- Displays the number squared

**Example interaction:**
```
Enter a number: 7
The square is: 49
```

**Concepts:** `int()` conversion, math operations

---

## Exercise 2: String to Float - Price Calculation

**Write a program that:**
- Asks for a price (as text)
- Converts to float
- Adds 10% to the price
- Displays original and new price

**Example interaction:**
```
Enter price: 19.99
Original price: $19.99
New price (+10%): $21.99
```

**Concepts:** `float()` conversion, percentage calculation, f-string formatting

---

## Exercise 3: Number to String - Concatenation

**Write a program that:**
- Asks for the user's age
- Converts to integer
- Converts back to string and concatenates with other text
- Displays the message

**Example interaction:**
```
Enter age: 25
Message: You are 25 years old
```

**Concepts:** `int()` then `str()` conversion, concatenation

---

## Exercise 4: Multiple Type Conversions

**Write a program that:**
- Asks for quantity and price (both text)
- Converts both to numbers
- Calculates total
- Displays formatted result

**Example interaction:**
```
Quantity: 3
Price per item: 9.99
Total: $29.97
```

**Concepts:** Multiple conversions, formatting

---

## Exercise 5: Boolean Logic from User Input

**Write a program that:**
- Asks yes/no questions (3 times)
- Converts responses to boolean
- Counts how many "yes" answers
- Displays the count

**Example interaction:**
```
Question 1: Like Python? (yes/no): yes
Question 2: Like coding? (yes/no): yes
Question 3: Like learning? (yes/no): no
You answered yes to 2 questions
```

**Concepts:** String comparison, boolean conversion, counting

---

## Exercise 6: Type Checking - Validate Integer Input

**Write a program that:**
- Asks for an integer
- Validates it can be converted
- If valid: display the number and its type
- If invalid: display error and ask again (loop)

**Example interaction:**
```
Enter integer: abc
✗ Not a valid integer
Enter integer: 42
✓ Number: 42 (type: <class 'int'>)
```

**Concepts:** `try/except`, `type()`, input validation

---

## Exercise 7: Convert and Compare

**Write a program that:**
- Asks user for a number (text)
- Converts to integer
- Compares with 100
- Displays "greater", "less", or "equal"

**Example interaction:**
```
Enter a number: 150
150 is greater than 100
```

**Concepts:** Conversion, comparison, conditional logic

---

## Exercise 8: Temperature Scale Conversion

**Write a program that:**
- Asks for temperature in Celsius
- Converts to float
- Calculates Fahrenheit (F = C × 9/5 + 32)
- Displays both with proper formatting

**Example interaction:**
```
Celsius: 25
25.0°C = 77.0°F
```

**Concepts:** Float conversion, formula, formatting

---

## Exercise 9: CSV Parser with Type Conversion

**Write a program that:**
- Asks for a CSV line (Name,Age,Score)
- Splits by comma
- Converts Age to int, Score to float
- Displays each field with its type

**Example interaction:**
```
Enter CSV (Name,Age,Score): Alice,25,92.5
Name: Alice (type: str)
Age: 25 (type: int)
Score: 92.5 (type: float)
```

**Concepts:** String splitting, selective conversion, type verification

---

## Exercise 10: Complex Calculation with Multiple Conversions

**Write a comprehensive program that:**
- Gets user inputs (all as text):
  - Item price
  - Quantity
  - Tax rate (percent)
- Converts appropriately
- Calculates subtotal, tax, total
- Displays formatted receipt

**Example interaction:**
```
Item price: 19.99
Quantity: 3
Tax rate (%): 8.5
RECEIPT
------
Subtotal: $59.97
Tax (8.5%): $5.10
Total: $65.07
```

**Concepts:** Multiple conversions, complex calculations, formatted output

---

## Challenge Exercises (Optional)

### Challenge 1: Input Validation Loop
Write a program that keeps asking for an age until a valid integer (0-150) is entered.

### Challenge 2: Percentage Grade Calculator
Ask for test score and total possible points (both text). Calculate percentage and assign letter grade.

### Challenge 3: Multi-Currency Converter
Ask for amount and conversion rate. Convert between currencies with proper formatting.

### Challenge 4: Time Calculator
Ask for hours and minutes (text). Convert to seconds, display in various formats.

---

## Tips for Success

1. **Always remember:** `input()` returns strings
2. **Convert early:** Convert right after getting input
3. **Check types:** Use `type()` to verify conversions worked
4. **Handle errors:** Use `try/except` for user input conversion
5. **Format output:** Use f-strings with formatting for display

---

## Key Takeaways

After these exercises, you should understand:
- ✅ When and why to convert types
- ✅ How to use int(), float(), str(), bool()
- ✅ How to handle conversion errors
- ✅ How to chain conversions together
- ✅ How to work with mixed data types

