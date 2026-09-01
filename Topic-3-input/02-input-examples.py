# Topic 3: Input - Examples

# Example 1: Basic input
name = input("What is your name? ")
print("Hello, " + name)

# Example 2: Input and conversion
age = int(input("How old are you? "))
print("You are", age, "years old")

# Example 3: Multiple inputs
first = input("First name: ")
last = input("Last name: ")
print("Full name:", first, last)

# Example 4: Input with float
price = float(input("Price: $"))
print("You entered:", price)

# Example 5: Math with converted input
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
print("Sum:", num1 + num2)

# Example 6: Calculate future age
age = int(input("Current age: "))
future_age = age + 10
print("In 10 years you will be:", future_age)

# Example 7: Temperature conversion
celsius = float(input("Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

# Example 8: Grade average
score1 = int(input("Score 1: "))
score2 = int(input("Score 2: "))
score3 = int(input("Score 3: "))
average = (score1 + score2 + score3) / 3
print("Average:", average)

# Example 9: Rectangle area
width = int(input("Width: "))
height = int(input("Height: "))
area = width * height
print("Area:", area)

# Example 10: Price with tax
price = float(input("Price: $"))
tax_rate = float(input("Tax rate (0.1 for 10%): "))
tax = price * tax_rate
total = price + tax
print("Total: $" + str(total))

# Example 11: Currency conversion
usd = float(input("USD: $"))
exchange_rate = float(input("Exchange rate: "))
eur = usd * exchange_rate
print("EUR:", eur)

# Example 12: Personal info
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
print(name, "is", age, "and from", city)

# Example 13: Store text input
username = input("Username: ")
password = input("Password: ")
print("Username set to:", username)

# Example 14: Years of experience
start_year = int(input("Start year: "))
current_year = 2026
experience = current_year - start_year
print("Years of experience:", experience)

# Example 15: Simple calculation
quantity = int(input("Quantity: "))
unit_price = float(input("Unit price: $"))
total = quantity * unit_price
print("Total: $" + str(total))

