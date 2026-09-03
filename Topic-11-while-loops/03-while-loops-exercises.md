# Topic 11: While Loops - Exercises

## Overview

These exercises teach you to use while loops for repetition. You'll progress from simple counting loops to complex simulations and input validation.

---

## Exercise 1: Counting Loop

**Write a program that:**
- Counts from 1 to 10
- Uses a while loop
- Displays each number

**Example output:**
```
1
2
3
...
10
Finished
```

**Concepts:** Loop initialization, condition, update

---

## Exercise 2: Countdown

**Write a program that:**
- Counts down from 10 to 1
- Uses while loop
- Prints "Blastoff!" at the end

**Example output:**
```
10
9
8
...
1
Blastoff!
```

**Concepts:** Decrementing loop variable, loop termination

---

## Exercise 3: Sum Calculator

**Write a program that:**
- Sums numbers 1 through 10
- Uses while loop with accumulation
- Displays the final sum

**Example output:**
```
Sum of 1 to 10: 55
```

**Concepts:** Accumulation pattern, loop variable increment

---

## Exercise 4: Continue Practice

**Write a program that:**
- Prints numbers 1 to 10
- Skips even numbers using continue
- Shows odd numbers only

**Example output:**
```
1
3
5
7
9
```

**Concepts:** continue statement, conditional skipping

---

## Exercise 5: Input Validation

**Write a program that:**
- Asks user for age
- Validates it's between 0-150
- Keeps asking until valid
- Shows success message

**Example interaction:**
```
Enter age: 200
Invalid! Must be 0-150
Enter age: -5
Invalid! Must be 0-150
Enter age: 25
✓ Valid age: 25
```

**Concepts:** Input validation, loop control with break

---

## Exercise 6: User Menu

**Write a program that:**
- Shows a simple menu (Add, Subtract, Quit)
- Takes user input
- Processes commands until user quits
- Uses break to exit

**Example interaction:**
```
What would you like to do?
1. Add
2. Subtract
3. Quit
Choice: 1
Enter two numbers: 5 3
Result: 8
What would you like to do?
...
Choice: 3
Goodbye!
```

**Concepts:** Infinite loop, break, menu processing

---

## Exercise 7: Nested Loops - Square Pattern

**Write a program that:**
- Uses nested while loops
- Creates a 4x4 pattern of asterisks
- Each row on new line

**Example output:**
```
* * * *
* * * *
* * * *
* * * *
```

**Concepts:** Nested loops, loop variables, pattern output

---

## Exercise 8: Number Guessing Game

**Write a program that:**
- Computer "thinks" of a number (1-10)
- User keeps guessing
- Gives hints (too high/low)
- Counts attempts
- Stops when correct

**Example interaction:**
```
Guess a number (1-10): 5
Too low
Guess a number (1-10): 8
Too high
Guess a number (1-10): 6
Correct! It took 3 guesses
```

**Concepts:** Loops with conditions, hints, counting iterations

---

## Exercise 9: Accumulation - Sum List

**Write a program that:**
- Asks user to enter numbers
- User enters 0 to finish
- Uses while loop to sum
- Displays total and count

**Example interaction:**
```
Enter numbers (0 to finish):
Enter number: 10
Running total: 10
Enter number: 20
Running total: 30
Enter number: 5
Running total: 35
Enter number: 0
Final sum: 35, Count: 3
```

**Concepts:** Input loop, accumulation, break condition

---

## Exercise 10: Complex Validation - Password Retry

**Write a program that:**
- Asks for password (hardcoded)
- Allows 3 attempts
- Validates each attempt
- Shows attempts remaining
- Locks after 3 failures

**Example interaction:**
```
Enter password (attempt 1/3): wrong
Wrong! 2 attempts remaining
Enter password (attempt 2/3): bad
Wrong! 1 attempt remaining
Enter password (attempt 3/3): nope
Too many attempts. Access denied.
```

**Concepts:** Attempt counter, max limit, loop exit conditions

---

## Challenge Exercises (Optional)

### Challenge 1: Higher/Lower Game
- Computer picks number 1-100
- User guesses with feedback
- Track number of guesses
- Calculate efficiency rating

### Challenge 2: Multiplication Tables
- Display custom sized multiplication table
- User specifies size (e.g., 5x5)
- Use nested loops
- Proper formatting with columns

### Challenge 3: Loan Payoff Calculator
- Loan amount, interest rate, monthly payment
- Loop until loan paid off
- Track total paid, total interest
- Display month-by-month breakdown

### Challenge 4: Text Processing
- User enters lines of text (empty line to finish)
- Count lines, words, characters
- Find longest/shortest line
- Display statistics

---

## Tips for Success

1. **Initialize properly:** Set loop variable before loop
2. **Update in loop:** Change loop variable each iteration
3. **Test condition:** Will loop eventually exit?
4. **Use break wisely:** Exit when needed, not in wrong places
5. **Trace execution:** Walk through loop mentally

---

## Key Takeaways

After these exercises, you should:
- ✅ Write while loops with proper structure
- ✅ Initialize, check, and update loop variables
- ✅ Use break to exit loops
- ✅ Use continue to skip iterations
- ✅ Accumulate results while looping
- ✅ Validate user input with loops
- ✅ Nest loops for complex patterns
- ✅ Build games and simulations with loops

