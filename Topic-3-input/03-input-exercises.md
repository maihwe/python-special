# Topic 3: Input - Exercises

## Overview

These exercises build from simple input to realistic programs. Each exercise reinforces the key concepts: `input()` returns strings, you must convert for math, and users can type anything.

---

## Exercise 1: Simple Greeting

**Write a program that:**
- Asks the user for their name
- Displays a personalized greeting

**Example interaction:**
```
Enter your name: Alice
Hello, Alice! It's nice to meet you.
```

**Concepts:** Basic input, displaying results

---

## Exercise 2: Age Calculation

**Write a program that:**
- Asks the user for their birth year
- Calculates their age (assume current year is 2024)
- Displays their age

**Example interaction:**
```
What year were you born? 2000
You are 24 years old.
```

**Concepts:** String to integer conversion, basic math

---

## Exercise 3: Rectangle Area

**Write a program that:**
- Asks the user for the length and width of a rectangle
- Calculates the area
- Displays the result

**Example interaction:**
```
Length (meters): 5
Width (meters): 3
Area: 15 square meters
```

**Concepts:** Multiple numeric inputs, multiplication

---

## Exercise 4: Temperature Conversion

**Write a program that:**
- Asks the user for temperature in Celsius
- Converts to Fahrenheit using: F = (C × 9/5) + 32
- Displays both values

**Example interaction:**
```
Temperature in Celsius: 0
0°C = 32°F

Temperature in Celsius: 25
25°C = 77°F
```

**Concepts:** Float conversion, formula application

---

## Exercise 5: Currency Converter

**Write a program that:**
- Asks the user for an amount in dollars
- Asks for exchange rate (dollars to another currency)
- Calculates the converted amount
- Displays the result

**Example interaction:**
```
Amount in USD: 100
Exchange rate (USD to EUR): 0.92
100 USD = 92 EUR
```

**Concepts:** Multiple float inputs, exchange rate calculation

---

## Exercise 6: Grade Letter Assignment

**Write a program that:**
- Asks the user for a numeric score (0-100)
- Assigns a letter grade:
  - 90-100: A
  - 80-89: B
  - 70-79: C
  - 60-69: D
  - Below 60: F
- Displays the letter grade

**Example interaction:**
```
Enter your score: 85
Your grade: B
```

**Concepts:** Conversion, conditional logic, comparisons

---

## Exercise 7: Three Test Average

**Write a program that:**
- Asks the user for three test scores
- Calculates the average
- Determines if the average is passing (>= 70)
- Displays the average and pass/fail status

**Example interaction:**
```
Test 1 score: 85
Test 2 score: 92
Test 3 score: 78
Average: 85.00
Status: PASS
```

**Concepts:** Multiple inputs, averaging, Boolean output

---

## Exercise 8: Simple Shopping Cart

**Write a program that:**
- Asks for the price of an item
- Asks for the quantity
- Asks for tax rate (as percentage)
- Calculates total with tax
- Displays itemized breakdown

**Example interaction:**
```
Item price: 19.99
Quantity: 3
Tax rate (%): 8.5
Subtotal: 59.97
Tax: 5.10
Total: 65.07
```

**Concepts:** Multiple calculations, formatting currency

---

## Exercise 9: Distance and Speed Calculator

**Write a program that:**
- Asks for distance traveled (km)
- Asks for time taken (hours)
- Calculates average speed
- Interprets speed:
  - < 50 km/h: Slow
  - 50-100 km/h: Normal
  - > 100 km/h: Fast

**Example interaction:**
```
Distance (km): 150
Time (hours): 2.5
Average speed: 60.0 km/h
Classification: Normal
```

**Concepts:** Division, conditional categories

---

## Exercise 10: Personal Info Summary

**Write a comprehensive program that:**
- Asks for: name, age, city, favorite color, is student (yes/no)
- Processes all inputs appropriately
- Displays a formatted summary with all information

**Example interaction:**
```
Enter your name: Bob
Enter your age: 28
Enter your city: Boston
Enter your favorite color: blue
Are you a student? (yes/no): no
================================
PERSONAL INFORMATION SUMMARY
================================
Name: Bob
Age: 28
City: Boston
Favorite Color: blue
Student: No
Next year you'll be: 29 years old
================================
```

**Concepts:** Multiple input types, text and numeric conversion, Boolean conversion, string formatting

---

## Challenge Exercises (Optional)

### Challenge 1: Loan Payment Calculator
Ask for loan amount, interest rate, and years. Calculate monthly payment.

### Challenge 2: Menu-Driven Calculator
Ask user for two numbers and an operation (+, -, *, /). Perform calculation.

### Challenge 3: BMI Calculator
Ask for weight (kg) and height (m). Calculate BMI and determine category.

### Challenge 4: Time Zone Converter
Ask for current hour and destination time difference. Calculate destination time.

---

## Tips for Success

1. **Remember:** `input()` always returns strings
2. **Convert:** Use `int()` and `float()` when you need numbers
3. **Test:** Try different inputs to see how your program responds
4. **Format:** Make your output clear and easy to read
5. **Think ahead:** What could go wrong? (User enters wrong type?)

---

## Key Takeaways

After these exercises, you should understand:
- ✅ How to get user input and store it
- ✅ When and how to convert strings to numbers
- ✅ How to combine multiple inputs in one program
- ✅ How to use input in calculations
- ✅ How to make programs interactive and responsive

