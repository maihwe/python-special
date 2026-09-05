# Topic 19: OOP Basics - Elaborate Examples
# Comprehensive examples of classes, objects, inheritance, and polymorphism

# ============================================================================
# EXAMPLE 1: Simple Class Definition
# ============================================================================
# Define and create objects

print("Example 1: Simple Class")
print("-" * 50)

class Person:
    pass

person = Person()
print(f"Created person: {person}")
print()

# ============================================================================
# EXAMPLE 2: Class with Attributes
# ============================================================================
# Store data in objects

print("Example 2: Attributes")
print("-" * 50)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog = Dog("Rex", "Labrador")
print(f"Name: {dog.name}")
print(f"Breed: {dog.breed}")
print()

# ============================================================================
# EXAMPLE 3: Methods
# ============================================================================
# Functions inside classes

print("Example 3: Methods")
print("-" * 50)

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def sit(self):
        print(f"{self.name} sits down")

dog = Dog("Rex")
dog.bark()
dog.sit()
print()

# ============================================================================
# EXAMPLE 4: Self Reference
# ============================================================================
# self refers to current object

print("Example 4: Self Reference")
print("-" * 50)

class Counter:
    def __init__(self):
        self.value = 0
    
    def increment(self):
        self.value += 1
        print(f"Value: {self.value}")

counter = Counter()
counter.increment()
counter.increment()
counter.increment()
print()

# ============================================================================
# EXAMPLE 5: Multiple Instances
# ============================================================================
# Each object has separate data

print("Example 5: Multiple Instances")
print("-" * 50)

class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Rex")
dog2 = Dog("Buddy")
dog3 = Dog("Max")

print(f"Dog 1: {dog1.name}")
print(f"Dog 2: {dog2.name}")
print(f"Dog 3: {dog3.name}")
print()

# ============================================================================
# EXAMPLE 6: Constructor with Defaults
# ============================================================================
# Initialize with default values

print("Example 6: Default Values")
print("-" * 50)

class Car:
    def __init__(self, brand, model="Unknown", color="white"):
        self.brand = brand
        self.model = model
        self.color = color

car1 = Car("Toyota", "Camry", "blue")
car2 = Car("Honda")

print(f"Car 1: {car1.color} {car1.brand} {car1.model}")
print(f"Car 2: {car2.color} {car2.brand} {car2.model}")
print()

# ============================================================================
# EXAMPLE 7: Instance Attributes
# ============================================================================
# Data stored per instance

print("Example 7: Instance Attributes")
print("-" * 50)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

account = BankAccount("Alice", 1000)
print(f"Initial: {account.balance}")

account.deposit(100)
print(f"After deposit: {account.balance}")

account.withdraw(50)
print(f"After withdrawal: {account.balance}")
print()

# ============================================================================
# EXAMPLE 8: Class Attributes
# ============================================================================
# Data shared by all instances

print("Example 8: Class Attributes")
print("-" * 50)

class Dog:
    species = "Canis familiaris"  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute

dog1 = Dog("Rex")
dog2 = Dog("Buddy")

print(f"Dog 1 species: {dog1.species}")
print(f"Dog 2 species: {dog2.species}")
print(f"Class species: {Dog.species}")
print(f"All reference same: {dog1.species is dog2.species}")
print()

# ============================================================================
# EXAMPLE 9: Inheritance - Basic
# ============================================================================
# Child class inherits from parent

print("Example 9: Inheritance")
print("-" * 50)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Generic sound"

class Dog(Animal):
    pass

dog = Dog("Rex")
print(f"Name: {dog.name}")
print(f"Sound: {dog.speak()}")
print()

# ============================================================================
# EXAMPLE 10: Method Overriding
# ============================================================================
# Child overrides parent method

print("Example 10: Method Overriding")
print("-" * 50)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Rex")
cat = Cat("Whiskers")

print(f"{dog.name}: {dog.speak()}")
print(f"{cat.name}: {cat.speak()}")
print()

# ============================================================================
# EXAMPLE 11: Super() - Call Parent Method
# ============================================================================
# Access parent class methods

print("Example 11: Super()")
print("-" * 50)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says:"

class Dog(Animal):
    def speak(self):
        parent_speak = super().speak()
        return f"{parent_speak} Woof!"

dog = Dog("Rex")
print(dog.speak())
print()

# ============================================================================
# EXAMPLE 12: Multilevel Inheritance
# ============================================================================
# Chain of inheritance

print("Example 12: Multilevel Inheritance")
print("-" * 50)

class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def feed_milk(self):
        return "Feeding milk"

class Dog(Mammal):
    def bark(self):
        return "Woof!"

dog = Dog("Rex")
print(f"Name: {dog.name}")
print(f"Mammal ability: {dog.feed_milk()}")
print(f"Dog ability: {dog.bark()}")
print()

# ============================================================================
# EXAMPLE 13: Polymorphism
# ============================================================================
# Different objects, same method

print("Example 13: Polymorphism")
print("-" * 50)

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
print()

# ============================================================================
# EXAMPLE 14: __str__ Method
# ============================================================================
# Custom string representation

print("Example 14: __str__ Method")
print("-" * 50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age} years old)"

person = Person("Alice", 30)
print(person)
print(str(person))
print()

# ============================================================================
# EXAMPLE 15: __repr__ Method
# ============================================================================
# Developer representation

print("Example 15: __repr__ Method")
print("-" * 50)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book = Book("1984", "Orwell")
print(repr(book))
print()

# ============================================================================
# EXAMPLE 16: __eq__ Method
# ============================================================================
# Equality comparison

print("Example 16: __eq__ Method")
print("-" * 50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
person3 = Person("Bob", 25)

print(f"person1 == person2: {person1 == person2}")
print(f"person1 == person3: {person1 == person3}")
print()

# ============================================================================
# EXAMPLE 17: Private Attributes
# ============================================================================
# Convention for internal attributes

print("Example 17: Private Attributes")
print("-" * 50)

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private (by convention)
    
    def deposit(self, amount):
        self._balance += amount
    
    def get_balance(self):
        return self._balance

account = BankAccount(1000)
print(f"Balance: {account.get_balance()}")
account.deposit(100)
print(f"After deposit: {account.get_balance()}")
print()

# ============================================================================
# EXAMPLE 18: Encapsulation
# ============================================================================
# Hide internal details

print("Example 18: Encapsulation")
print("-" * 50)

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def get_area(self):
        return self._width * self._height
    
    def get_perimeter(self):
        return 2 * (self._width + self._height)

rect = Rectangle(5, 3)
print(f"Area: {rect.get_area()}")
print(f"Perimeter: {rect.get_perimeter()}")
print()

# ============================================================================
# EXAMPLE 19: Class Methods
# ============================================================================
# Methods that work on class, not instance

print("Example 19: Class Methods")
print("-" * 50)

class Circle:
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

circle1 = Circle(5)
circle2 = Circle.from_diameter(10)

print(f"Circle 1 area: {circle1.area():.2f}")
print(f"Circle 2 area: {circle2.area():.2f}")
print()

# ============================================================================
# EXAMPLE 20: Static Methods
# ============================================================================
# Methods that don't need instance or class

print("Example 20: Static Methods")
print("-" * 50)

class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

print(f"Add: {MathHelper.add(5, 3)}")
print(f"Multiply: {MathHelper.multiply(5, 3)}")
print()

# ============================================================================
# EXAMPLE 21: Composition
# ============================================================================
# Objects containing other objects

print("Example 21: Composition")
print("-" * 50)

class Engine:
    def __init__(self, type):
        self.type = type
    
    def start(self):
        return f"Starting {self.type}"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine
    
    def start(self):
        return f"{self.brand}: {self.engine.start()}"

engine = Engine("V8")
car = Car("Ferrari", engine)
print(car.start())
print()

# ============================================================================
# EXAMPLE 22: Initialization with Arguments
# ============================================================================
# Flexible object creation

print("Example 22: Flexible Init")
print("-" * 50)

class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades else []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

student1 = Student("Alice", [85, 90, 92])
student2 = Student("Bob")
student2.add_grade(88)

print(f"{student1.name}: {student1.average():.1f}")
print(f"{student2.name}: {student2.average():.1f}")
print()

# ============================================================================
# EXAMPLE 23: Object Comparison
# ============================================================================
# Comparing objects

print("Example 23: Object Comparison")
print("-" * 50)

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score

player1 = Player("Alice", 100)
player2 = Player("Bob", 85)
player3 = Player("Charlie", 120)

print(f"{player1.name} > {player2.name}: {player1 > player2}")
print(f"{player3.name} > {player1.name}: {player3 > player1}")
print()

# ============================================================================
# EXAMPLE 24: Real-world: Game Character
# ============================================================================
# Complete game character class

print("Example 24: Game Character")
print("-" * 50)

class Character:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
    
    def take_damage(self, amount):
        self.health -= amount
    
    def heal(self, amount):
        self.health += amount
    
    def level_up(self):
        self.level += 1
        self.health += 10
    
    def __str__(self):
        return f"{self.name} (Lvl {self.level}, HP {self.health})"

char = Character("Hero", 100, 1)
print(f"Start: {char}")
char.take_damage(20)
print(f"After damage: {char}")
char.heal(10)
print(f"After heal: {char}")
char.level_up()
print(f"After level up: {char}")
print()

# ============================================================================
# EXAMPLE 25: Real-world: Bank Account
# ============================================================================
# Complete bank account class

print("Example 25: Bank Account")
print("-" * 50)

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.transactions.append(f"Deposit: +{amount}")
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
    
    def get_balance(self):
        return self._balance
    
    def get_statement(self):
        print(f"\n{self.owner}'s Account Statement")
        print(f"Balance: ${self._balance}")
        print("Transactions:")
        for trans in self.transactions:
            print(f"  {trans}")

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.deposit(100)
account.get_statement()

