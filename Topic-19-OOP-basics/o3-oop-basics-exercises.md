# Topic 19: OOP Basics - Exercises

## Overview

These exercises teach you to define classes, create objects, use inheritance, and organize programs with object-oriented design.

---

## Exercise 1: Simple Class Definition

**Write a class that:**
- Defines a `Book` class with attributes: title, author, pages
- Implements `__init__` constructor
- Creates and prints 3 different book objects
- Accesses attributes

**Example:**
```
Book: 1984
Author: George Orwell
Pages: 328

Book: Dune
Author: Frank Herbert
Pages: 682
```

**Concepts:** Classes, constructors, attributes

---

## Exercise 2: Methods and Behavior

**Write a class that:**
- Defines a `Calculator` class
- Implements methods: add(), subtract(), multiply(), divide()
- Each method takes two numbers and returns result
- Calls each method and prints results

**Example:**
```
Add 10 + 5: 15
Subtract 10 - 5: 5
Multiply 10 * 5: 50
Divide 10 / 5: 2.0
```

**Concepts:** Methods, self reference, function behavior

---

## Exercise 3: State Management

**Write a class that:**
- Defines a `BankAccount` class with balance attribute
- Implements deposit() and withdraw() methods
- Track balance changes
- Shows balance after each operation
- Prevents overdrafts

**Example:**
```
Initial balance: 1000
After deposit 500: 1500
After withdrawal 200: 1300
Insufficient funds for 2000
Final balance: 1300
```

**Concepts:** State management, validation, instance attributes

---

## Exercise 4: Multiple Instances

**Write a class that:**
- Defines a `Student` class with name and grades
- Stores multiple students in a list
- Adds grades to each student
- Calculates average for each
- Compares grades between students

**Example:**
```
Alice average: 88.3
Bob average: 85.7
Charlie average: 92.0
Highest: Charlie (92.0)
```

**Concepts:** Multiple instances, data separation, comparison

---

## Exercise 5: Inheritance

**Write classes that:**
- Define parent `Vehicle` class with attributes: brand, model
- Define child classes: `Car`, `Motorcycle`, `Truck`
- Each child has unique method (drive, wheelie, load)
- Create instances and call methods

**Example:**
```
Car: Toyota Camry - Driving smoothly
Motorcycle: Harley - Popping wheelies!
Truck: Ford - Loading cargo
```

**Concepts:** Inheritance, child classes, method definition

---

## Exercise 6: Method Overriding

**Write classes that:**
- Define `Animal` base class with speak() method
- Create `Dog`, `Cat`, `Bird` subclasses
- Each overrides speak() differently
- Create list of animals and call speak()
- Show polymorphic behavior

**Example:**
```
Rex: Woof!
Whiskers: Meow!
Tweety: Tweet!
```

**Concepts:** Inheritance, method overriding, polymorphism

---

## Exercise 7: Encapsulation

**Write a class that:**
- Defines `SecurePassword` with private attribute
- Implements setter with validation
- Implements getter
- Shows can't change password directly
- Shows setter validates requirements

**Example:**
```
Setting valid password: Success
Setting weak password: Failed (too short)
Password length valid: True
```

**Concepts:** Encapsulation, private attributes, validation

---

## Exercise 8: Special Methods

**Write a class that:**
- Defines `Person` class with name, age
- Implements __str__() for print()
- Implements __repr__() for representation
- Implements __eq__() for comparison
- Creates and compares persons

**Example:**
```
print(person): Alice (30 years)
repr(person): Person('Alice', 30)
person1 == person2: True
```

**Concepts:** Special methods, dunder methods, representation

---

## Exercise 9: Composition

**Write classes that:**
- Define `Engine` class with type, horsepower
- Define `Car` class containing Engine
- Car.start() uses engine.start()
- Shows object containing other objects
- Demonstrates "has-a" relationship

**Example:**
```
Car: Ferrari
Engine: V12 (800hp)
Action: Starting V12 engine
Ferrari is driving fast!
```

**Concepts:** Composition, object relationships, "has-a"

---

## Exercise 10: Class vs Instance Attributes

**Write a class that:**
- Defines `Counter` class with class attribute (count)
- Defines instance attribute (value)
- Tracks total instances created
- Shows each counter independent
- Shows class attribute shared

**Example:**
```
Created Counter 1
Created Counter 2
Created Counter 3
Total counters created: 3
Counter 1 value: 10
Counter 2 value: 20
Each unique, but count is shared
```

**Concepts:** Class vs instance attributes, class variables

---

## Challenge Exercises (Optional)

### Challenge 1: Game Character System
- Create `Character` base class with: name, health, level, experience
- Create subclasses: `Warrior`, `Mage`, `Archer` with unique abilities
- Implement combat system: take_damage(), attack(), special_ability()
- Implement leveling: gain_experience(), level_up()
- Create party of characters and simulate combat
- Display character status before/after battle

### Challenge 2: Library Management System
- Create `Book` class: title, author, isbn, available
- Create `Library` class that stores books
- Implement: add_book(), remove_book(), borrow_book(), return_book()
- Track book availability
- Show all books and their status
- Show borrowed books per person
- Implement search_by_title(), search_by_author()

### Challenge 3: Banking System
- Create `Account` class: owner, account_number, balance
- Create `SavingsAccount` and `CheckingAccount` subclasses
- Each type has different fee structure
- Implement: deposit(), withdraw(), apply_fees()
- Create `Bank` class managing multiple accounts
- Implement account lookup, transfers between accounts
- Generate transaction history and statements

### Challenge 4: Shape Hierarchy
- Create `Shape` base class with area() and perimeter()
- Create subclasses: `Circle`, `Rectangle`, `Triangle`
- Each calculates area and perimeter correctly
- Create list of shapes and calculate total area
- Sort shapes by area
- Display shape information with special formatting
- Implement validation (no negative dimensions)

---

## Tips for Success

1. **Start simple:** Define class, add constructor, add methods
2. **Use self:** Remember self refers to object being worked on
3. **Inheritance hierarchy:** Parent → Child relationship
4. **Polymorphism:** Same method name, different behavior
5. **Encapsulation:** Hide internal details, provide interface
6. **Special methods:** Make objects feel like built-ins
7. **Test extensively:** Create multiple instances, test edge cases

---

## Key Takeaways

After these exercises, you should:
- ✅ Define classes with attributes and methods
- ✅ Create objects and access their data
- ✅ Implement constructors
- ✅ Use inheritance for code reuse
- ✅ Override methods in subclasses
- ✅ Implement polymorphism
- ✅ Use encapsulation for data hiding
- ✅ Implement special methods
- ✅ Use composition
- ✅ Organize complex systems with OOP

