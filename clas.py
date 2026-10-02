class WeekDays:
    def __init__(self, time, hours):
        self.time = time
        self.hours = hours
    def __str__(self):
        return f"This {self.time} at about exactly {self.hours} ago he arived!"
monday = WeekDays("morning", "one hour")
print(monday)
print()

class TeaCup:
    def __init__(self, size, owner):
        self.size = size
        self.owner = owner
    def __str__(self):
        return f"This is a {self.size} cup owned by {self.owner}\n"
Mathias_Cup = TeaCup("large", "Mathias")
print(Mathias_Cup)

class Cup:
    def __init__(self, color):
        self.color = color
        self.contents = []

    def add_liquid(self, drink_name):
        self.contents.append(drink_name)
        print(f"poured {drink_name} into the {self.color} cup!\n")

blue_cup = Cup("blue")

blue_cup.add_liquid("Coffee")
blue_cup.add_liquid("Milk")
blue_cup.add_liquid("Tea")

print(blue_cup.contents)