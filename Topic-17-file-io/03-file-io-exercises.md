# Topic 17: File I/O - Exercises

## Overview

These exercises teach you to read and write files, persist data, and work with structured formats like CSV and JSON. You'll progress from basic file operations to complex data processing pipelines.

---

## Exercise 1: Create and Write File

**Write a program that:**
- Creates a new file
- Writes multiple lines
- Closes file properly
- Reads back content to verify

**Example:**
```
Created output.txt
Content:
  Hello, World!
  This is line 2
  Final line
```

**Concepts:** File creation, writing, reading back

---

## Exercise 2: Read Entire File

**Write a program that:**
- Reads entire file at once
- Displays content
- Shows file size
- Counts lines

**Example:**
```
File: names.txt
Content: Alice, Bob, Charlie, Diana
Lines: 4
Size: 42 bytes
```

**Concepts:** read(), file size, line counting

---

## Exercise 3: Read Line by Line

**Write a program that:**
- Opens file
- Reads line by line
- Strips whitespace
- Processes each line
- Shows results

**Example:**
```
Line 1: Alice
Line 2: Bob
Line 3: Charlie
Total: 3 lines
```

**Concepts:** readline(), readlines(), line processing

---

## Exercise 4: Append to File

**Write a program that:**
- Creates initial file
- Appends new content
- Verifies both parts exist
- Shows final content

**Example:**
```
Initial: Alice, Bob
Appended: Charlie, Diana
Final: Alice, Bob, Charlie, Diana
```

**Concepts:** Write mode vs append mode, file preservation

---

## Exercise 5: Write List to File

**Write a program that:**
- Takes list of items
- Writes each to file (one per line)
- Reads back to verify
- Displays with line numbers

**Example:**
```
Items: apple, banana, cherry
File content:
  1: apple
  2: banana
  3: cherry
```

**Concepts:** Writing collections, formatting output

---

## Exercise 6: Parse Delimited Data

**Write a program that:**
- Creates file with delimited data
- Reads and parses
- Extracts fields
- Performs calculations

**Example:**
```
File: name age city
Alice 30 Boston
Bob 25 NYC
Processing: Extract cities, calculate average age
```

**Concepts:** String splitting, parsing, data extraction

---

## Exercise 7: Write and Read JSON

**Write a program that:**
- Creates data structure
- Saves as JSON
- Loads back from JSON
- Verifies data integrity

**Example:**
```
Original: {name: Alice, age: 30, hobbies: [reading, coding]}
Saved to JSON
Loaded: Same structure restored
```

**Concepts:** JSON serialization, JSON deserialization

---

## Exercise 8: Process CSV File

**Write a program that:**
- Reads CSV file
- Processes rows
- Calculates statistics
- Generates report

**Example:**
```
CSV: name, score
Alice, 85
Bob, 92
Report: Average: 88.5, Highest: 92
```

**Concepts:** CSV reading, row processing, statistics

---

## Exercise 9: Error Handling

**Write a program that:**
- Attempts to read nonexistent file
- Catches FileNotFoundError
- Provides fallback
- Handles gracefully

**Example:**
```
Trying to read: nonexistent.txt
File not found!
Using default data instead
```

**Concepts:** Try/except, file error handling

---

## Exercise 10: Data Persistence

**Write a program that:**
- Implements simple data persistence
- Save data to file
- Load data from file
- Verify data survives program restart

**Example:**
```
Session 1: Add Alice (score: 95)
Saved to file
Session 2: Load data
Alice's score: 95 (restored!)
```

**Concepts:** Data persistence, application state

---

## Challenge Exercises (Optional)

### Challenge 1: Log File Analyzer
- Create log file with entries
- Read and parse timestamps
- Filter by date range
- Generate summary statistics
- Create report with trends

### Challenge 2: Data Conversion Tool
- Read CSV file
- Convert to JSON
- Save as JSON
- Verify conversion
- Support bidirectional conversion

### Challenge 3: Configuration Manager
- Read configuration file
- Parse settings
- Support updates
- Save changes back
- Validate configuration values

### Challenge 4: Database Simulator
- Store records in CSV
- Implement add/delete/update
- Search by field
- Sort results
- Generate reports
- Back up data

---

## Tips for Success

1. **Always use with statement:** Ensures files close properly
2. **Handle errors:** Files may not exist or become unavailable
3. **Close before reopening:** Don't open same file twice
4. **Strip whitespace:** Newlines and spaces matter
5. **Backup important files:** Before overwriting, back up originals
6. **Use appropriate formats:** CSV for tables, JSON for nested, text for logs

---

## Key Takeaways

After these exercises, you should:
- ✅ Create, read, and write text files
- ✅ Append to existing files
- ✅ Use with statement for safety
- ✅ Parse and process file data
- ✅ Work with CSV files
- ✅ Work with JSON files
- ✅ Handle file errors gracefully
- ✅ Persist data between runs
- ✅ Process large files efficiently
- ✅ Build data pipelines

