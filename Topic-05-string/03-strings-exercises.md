# Topic 4: Strings - Exercises

## Overview

These exercises build from simple character access to complex string manipulation. Each exercise uses real-world scenarios where text processing is essential.

---

## Exercise 1: Character Access and Slicing

**Write a program that:**
- Asks the user for a word
- Displays the first character
- Displays the last character
- Displays the entire word reversed

**Example interaction:**
```
Enter a word: Python
First character: P
Last character: n
Reversed: nohtyP
```

**Concepts:** Indexing, negative indexing, slicing with step

---

## Exercise 2: Name Formatting

**Write a program that:**
- Asks for the user's first and last name (separately)
- Converts names to title case (first letter uppercase)
- Creates and displays a formatted full name

**Example interaction:**
```
Enter first name: john
Enter last name: smith
Formatted name: John Smith
```

**Concepts:** `capitalize()`, string concatenation, `.title()`

---

## Exercise 3: Email Validation

**Write a program that:**
- Asks the user for an email address
- Checks if it contains "@" and "."
- Extracts username and domain
- Displays validation result

**Example interaction:**
```
Enter email: alice@example.com
✓ Valid email format
Username: alice
Domain: example.com
```

**Concepts:** Substring search (`in`), `find()`, string slicing

---

## Exercise 4: Text Cleaning

**Write a program that:**
- Asks for a sentence (may have extra spaces)
- Removes leading/trailing spaces
- Converts to lowercase
- Counts the number of words

**Example interaction:**
```
Enter sentence:    Hello World Python   
Cleaned: hello world python
Number of words: 3
```

**Concepts:** `.strip()`, `.lower()`, `.split()`, `len()`

---

## Exercise 5: Word Replacement

**Write a program that:**
- Asks for a sentence
- Asks for a word to replace
- Asks for the replacement word
- Displays the modified sentence

**Example interaction:**
```
Enter sentence: The quick brown fox
Word to replace: brown
Replacement word: red
Result: The quick red fox
```

**Concepts:** `.replace()`, string manipulation

---

## Exercise 6: Character Counter

**Write a program that:**
- Asks for a sentence
- Asks for a character to count
- Counts occurrences (case-insensitive)
- Displays the count

**Example interaction:**
```
Enter text: Hello World
Character to count: l
Count: 3
```

**Concepts:** `.lower()`, `.count()`, string methods

---

## Exercise 7: CSV Parser

**Write a program that:**
- Asks for a comma-separated line (like: Alice,25,Engineer)
- Splits it into fields
- Displays each field separately

**Example interaction:**
```
Enter CSV line: Alice,25,Engineer,Boston
Name: Alice
Age: 25
Job: Engineer
City: Boston
```

**Concepts:** `.split()`, indexing lists, string parsing

---

## Exercise 8: Password Strength Checker

**Write a program that:**
- Asks for a password
- Checks:
  - Length >= 8 characters
  - Contains at least one digit
  - Contains at least one uppercase letter
- Displays overall strength

**Example interaction:**
```
Enter password: MyPass123
✓ Length OK (9 characters)
✓ Contains digits
✓ Contains uppercase
Password Strength: STRONG
```

**Concepts:** `.isdigit()`, `.isupper()`, `len()`, multiple conditions

---

## Exercise 9: Text Statistics

**Write a program that:**
- Asks the user for a sentence
- Calculates and displays:
  - Total characters
  - Number of words
  - Average word length
  - Most common letter (count)

**Example interaction:**
```
Enter text: hello world
Total characters: 11
Number of words: 2
Average word length: 5.0
Letter 'l' appears: 3 times
```

**Concepts:** `.split()`, `.count()`, len(), loops

---

## Exercise 10: Email Address Parser (Advanced)

**Write a comprehensive program that:**
- Asks for an email address
- Validates basic format (has @ and .)
- Extracts username, domain name, and TLD
- Creates a formatted display

**Example interaction:**
```
Enter email: john.doe@example.com
Analysis:
  Username: john.doe
  Domain: example.com
  Domain name: example
  TLD: com
  ✓ Valid format (has @ and .)
```

**Concepts:** `.find()`, `.split()`, string slicing, method chaining

---

## Challenge Exercises (Optional)

### Challenge 1: Sentence Reversal
Ask for a sentence. Reverse the order of words (not characters).
```
Input: Hello World Python
Output: Python World Hello
```

### Challenge 2: Acronym Generator
Ask for a sentence. Generate an acronym from first letters.
```
Input: Python Is Great
Output: PIG
```

### Challenge 3: Text Cipher
Ask for text. Create a simple cipher by replacing each letter with the next in alphabet.
```
Input: abc
Output: bcd
```

### Challenge 4: Username Generator
Ask for first and last name. Create usernames (variations with different formats).

---

## Tips for Success

1. **Remember immutability:** String methods don't change the original; they return new strings
2. **Use f-strings:** They make output clearer: `f"The answer is {value}"`
3. **Test edge cases:** What if string is empty? What if no match found?
4. **Chain methods:** You can use `.split().lower().replace(...)` etc.
5. **Use online resources:** String documentation is your friend

---

## Key Takeaways

After these exercises, you should understand:
- ✅ How to access and extract parts of strings
- ✅ How to use common string methods effectively
- ✅ How to parse and clean user input
- ✅ How to validate text data
- ✅ How to manipulate text for real-world tasks

