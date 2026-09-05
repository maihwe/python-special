# Topic 19: OOP Basics - Object-Oriented Programming Fundamentals

## Goal

**Learn to organize code using classes and objects. Understand attributes, methods, inheritance, and how objects enable modeling real-world concepts. Master the structural layer for building large, maintainable programs.**

---

## Why This Matters - The Real Problem

Without OOP, programs become hard to organize:

**Without OOP (scattered data and functions):**
```python
# Player data scattered everywhere
player_name = "Alice"
player_health = 100
player_level = 5

# Functions operating on player data
def take_damage(amount):
    global player_health
    player_health -= amount

def level_up():
    global player_level
    player_level += 1

# Enemy data separate from player
enemy_name = "Goblin"
enemy_health = 30

# Different functions for enemy
def enemy_take_damage(amount):
    global enemy_health
    enemy_health -= amount
```

**With OOP (organized into classes):**
```python
class Player:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
    
    def take_damage(self, amount):
        self.health -= amount
    
    def level_up(self):
        self.level += 1

player = Player("Alice", 100, 5)
player.take_damage(10)
player.level_up()
```

**OOP enables:**
- Organize related data and functions
- Model real-world concepts
- Reuse code through inheritance
- Scale to large systems
- Team collaboration
- Professional architecture

---

## Mental Model 1: What Is a Class? (The Blueprint Model)

A **class** is a blueprint for creating objects.

```
Class: "Car" (blueprint)
  Attributes: brand, model, speed
  Methods: accelerate(), brake(), honk()

        ↓ (create instance)

Object: my_car
  brand = "Toyota"
  model = "Camry"
  speed = 0
  Methods: accelerate(), brake(), honk()
```

**Class vs Object:**

```python
class Dog:  # Blueprint
    pass

my_dog = Dog()  # Instance (object)
your_dog = Dog()  # Different instance
```

**Real analogy:**

```
Class = Cookie cutter (blueprint)
Object = Each cookie made from cutter

Class = Car design
Object = Specific car you drive

Class = Person type
Object = Specific person
```

---

## Mental Model 2: Attributes and Methods (The Data and Behavior Model)

**Attributes** store data. **Methods** perform actions.

```python
class Player:
    # Attributes (data)
    def __init__(self, name, health):
        self.name = name  # Attribute
        self.health = health  # Attribute
    
    # Methods (behavior)
    def take_damage(self, amount):
        self.health -= amount
    
    def heal(self, amount):
        self.health += amount
```

**Using attributes and methods:**

```python
player = Player("Alice", 100)

# Access attributes
print(player.name)  # Alice
print(player.health)  # 100

# Call methods
player.take_damage(10)
print(player.health)  # 90

player.heal(5)
print(player.health)  # 95
```

---

## Mental Model 3: Constructor and Self (The Initialization Model)

**`__init__`** initializes new objects.
**`self`** refers to current object.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name   # Set attribute
        self.breed = breed  # Set attribute

dog = Dog("Rex", "Labrador")
# Calls __init__ with self=dog
# Sets dog.name = "Rex"
# Sets dog.breed = "Labrador"
```

**How `self` works:**

```python
class Cat:
    def __init__(self, name):
        self.name = name  # self = this object
    
    def meow(self):
        print(f"{self.name} says meow!")

cat = Cat("Whiskers")
cat.meow()  # Passes cat as self automatically
# Output: Whiskers says meow!
```

**Multiple instances, separate data:**

```python
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Buddy", "Poodle")

dog1.name  # "Rex"
dog2.name  # "Buddy"
# Different objects, separate data
```

---

## Mental Model 4: Instance vs Class Attributes (The Scope Model)

**Instance attributes** belong to individual objects.
**Class attributes** belong to entire class.

```python
class Player:
    level = 1  # Class attribute (shared)
    
    def __init__(self, name):
        self.name = name  # Instance attribute (per object)

player1 = Player("Alice")
player2 = Player("Bob")

player1.name  # "Alice"
player2.name  # "Bob"
# Different

Player.level  # 1
player1.level  # 1
player2.level  # 1
# Same
```

**When to use each:**

```python
class Dog:
    species = "Canis familiaris"  # Class - all dogs same
    
    def __init__(self, name):
        self.name = name  # Instance - each dog different
```

---

## Mental Model 5: Inheritance (The Hierarchy Model)

**Inheritance** lets classes inherit from parent classes.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):  # Inherits from Animal
    def speak(self):  # Override method
        return f"{self.name} barks"

dog = Dog("Rex")
print(dog.speak())  # Rex barks
```

**Hierarchy:**

```
      Animal
        ↑
   _____|_____
  |     |     |
 Dog   Cat   Bird

Dog inherits from Animal
- Gets __init__ from Animal
- Gets other methods from Animal
- Can override methods
- Can add new methods
```

**Is-a relationships:**

```python
class Vehicle:
    pass

class Car(Vehicle):  # Car IS-A Vehicle
    pass

class Truck(Vehicle):  # Truck IS-A Vehicle
    pass
```

---

## Mental Model 6: Method Overriding (The Customization Model)

**Override** methods to customize behavior in subclasses.

```python
class Animal:
    def speak(self):
        return "Generic sound"

class Dog(Animal):
    def speak(self):  # Override
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Override
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
```

**Super keyword (call parent method):**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says:"

class Dog(Animal):
    def speak(self):
        parent_message = super().speak()  # Call parent
        return f"{parent_message} Woof!"

dog = Dog("Rex")
print(dog.speak())  # Rex says: Woof!
```

---

## Mental Model 7: Encapsulation (The Privacy Model)

**Encapsulation** hides internal details.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private (by convention)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
    
    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(100)
print(account.get_balance())  # 1100
```

**Privacy levels (Python convention):**

```python
class Example:
    def public_method(self):
        pass  # Can access anywhere
    
    def _protected_method(self):
        pass  # Convention: internal use only
    
    def __private_method(self):
        pass  # Name mangled (more private)
```

---

## Mental Model 8: Polymorphism (The Many Forms Model)

**Polymorphism** means objects can be treated the same way despite different types.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(animal.speak())
# Woof!
# Meow!
# Tweet!
# Same code works for all types!
```

**Duck typing:**

```python
# Don't check type, just call method
def make_sound(thing):
    print(thing.speak())  # Works if it has speak()

make_sound(Dog())  # Works
make_sound(Cat())  # Works
make_sound(Bird())  # Works
```

---

## Mental Model 9: Special Methods (The Protocol Model)

**Special methods** enable built-in Python behavior.

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name  # For print()
    
    def __repr__(self):
        return f"Person({self.name})"
    
    def __eq__(self, other):
        return self.name == other.name  # For ==

person = Person("Alice")
print(person)  # Alice (uses __str__)
person == Person("Alice")  # True (uses __eq__)
```

**Common special methods:**

```python
__init__()      # Constructor
__str__()       # String representation
__repr__()      # Developer representation
__len__()       # len()
__getitem__()   # indexing []
__setitem__()   # assignment []
__eq__()        # ==
__lt__()        # <
__add__()       # +
```

---

## Common Confusion Points (Deep Dives)

### Confusion 1: "Self vs Self as Parameter"

**The question:** Why do I write `self` but don't pass it?

**The answer:** Python automatically passes object as `self`.

```python
class Dog:
    def bark(self):
        print(f"Woof from {self}")

dog = Dog()
dog.bark()  # Python automatically passes dog as self

# Equivalent to:
Dog.bark(dog)  # Explicit form (rarely used)
```

### Confusion 2: "Instance vs Class Attributes"

**The question:** When do attributes change?

**The answer:** Instance attributes per object, class attributes shared.

```python
class Counter:
    count = 0  # Class attribute
    
    def __init__(self):
        self.value = 0  # Instance attribute

c1 = Counter()
c2 = Counter()

c1.value = 5
c2.value = 10
# Different values

Counter.count = 100
# All objects share this
```

### Confusion 3: "Inheritance Doesn't Copy"

**The question:** Where are inherited methods?

**The answer:** In parent class. Child searches if not found locally.

```python
class Parent:
    def speak(self):
        return "Parent speaks"

class Child(Parent):
    pass

child = Child()
child.speak()  # Looks in Child, not found
               # Looks in Parent, found!
```

### Confusion 4: "__init__ Only on First Creation"

**The question:** Why does __init__ only run once?

**The answer:** It's called once per object creation.

```python
class Dog:
    def __init__(self):
        print("Created!")

dog1 = Dog()  # __init__ runs: Created!
dog2 = Dog()  # __init__ runs: Created!
# Not run again for same object
dog1.method()  # __init__ doesn't run
```

### Confusion 5: "Private Doesn't Mean Completely Hidden"

**The question:** Why can I still access private attributes?

**The answer:** Python's `_private` is convention, not enforcement.

```python
class Secret:
    def __init__(self):
        self._secret = "hidden"

obj = Secret()
obj._secret  # You CAN access (not truly private)
# But convention says: don't do this!
```

---

## How OOP Works Internally (Execution Model)

**Object creation:**

```python
class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("Rex")

# 1. Create empty object
# 2. Call __init__(dog, "Rex")
# 3. Set dog.name = "Rex"
# 4. Return dog object
```

**Method calling:**

```python
dog.speak()

# 1. Look up speak in dog's class
# 2. Found! It's a method
# 3. Call speak(dog) with dog as self
# 4. Return result
```

---

## Real-World OOP (Practical Applications)

**Game characters:**

```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_damage(self, amount):
        self.health -= amount

class Warrior(Character):
    def attack(self):
        return "Sword slash"

class Mage(Character):
    def attack(self):
        return "Fireball"
```

**Bank accounts:**

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
```

---

## Summary - The Big Picture

**What you learned:**
1. Classes are blueprints
2. Objects are instances
3. Attributes store data
4. Methods perform actions
5. Inheritance organizes hierarchies
6. Polymorphism allows flexible code
7. Encapsulation hides details
8. Special methods enable protocols

**Why this matters:**
- Organize complex systems
- Model real-world concepts
- Scale to large programs
- Enable team collaboration
- Professional architecture

**What's next:**
Now you understand objects.

Topic 20 teaches **Modules** - how to package and share code.

---

## What You Should Be Able To Do Now

✅ Define classes and create objects
✅ Create attributes and methods
✅ Understand constructors (__init__)
✅ Use inheritance
✅ Override methods
✅ Understand polymorphism
✅ Implement encapsulation
✅ Use special methods
✅ Model real-world concepts
✅ Organize complex systems

