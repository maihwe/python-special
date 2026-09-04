# Topic 15: Tuples and Sets - Elaborate Examples
# Comprehensive examples of creating and using tuples and sets

# ============================================================================
# EXAMPLE 1: Creating Tuples
# ============================================================================
# Different ways to create tuples

print("Example 1: Creating Tuples")
print("-" * 50)

t1 = (1, 2, 3)
print(f"Tuple: {t1}")

t2 = (10, 20)
print(f"Coordinates: {t2}")

t3 = (1, "hello", 3.14, True)
print(f"Mixed: {t3}")

empty = ()
print(f"Empty: {empty}")

single = (42,)
print(f"Single element: {single}")

implicit = 1, 2, 3
print(f"Implicit (no parens): {implicit}")
print()

# ============================================================================
# EXAMPLE 2: Tuple Constructor
# ============================================================================
# Create tuples from other sequences

print("Example 2: Using tuple() Constructor")
print("-" * 50)

from_list = tuple([1, 2, 3])
print(f"From list: {from_list}")

from_string = tuple("abc")
print(f"From string: {from_string}")

from_range = tuple(range(5))
print(f"From range: {from_range}")
print()

# ============================================================================
# EXAMPLE 3: Indexing Tuples
# ============================================================================
# Access items by position

print("Example 3: Indexing Tuples")
print("-" * 50)

t = (10, 20, 30, 40, 50)
print(f"Tuple: {t}")
print()

print(f"t[0] = {t[0]}")
print(f"t[2] = {t[2]}")
print(f"t[-1] = {t[-1]}")
print(f"t[-2] = {t[-2]}")
print()

# ============================================================================
# EXAMPLE 4: Slicing Tuples
# ============================================================================
# Extract subsequences

print("Example 4: Slicing Tuples")
print("-" * 50)

t = (0, 1, 2, 3, 4, 5)
print(f"Tuple: {t}")
print()

print(f"t[1:4] = {t[1:4]}")
print(f"t[:3] = {t[:3]}")
print(f"t[3:] = {t[3:]}")
print(f"t[::2] = {t[::2]}")
print(f"t[::-1] = {t[::-1]}")
print()

# ============================================================================
# EXAMPLE 5: Tuple Immutability
# ============================================================================
# Show that tuples can't change

print("Example 5: Immutability")
print("-" * 50)

t = (1, 2, 3)
print(f"Tuple: {t}")

try:
    t[0] = 99
    print("Changed!")
except TypeError as e:
    print(f"Can't change: {e}")

try:
    t.append(4)
    print("Appended!")
except AttributeError as e:
    print(f"No append method: {e}")
print()

# ============================================================================
# EXAMPLE 6: Tuple Unpacking
# ============================================================================
# Assign tuple elements to variables

print("Example 6: Tuple Unpacking")
print("-" * 50)

coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: {coordinates}")
print(f"x = {x}, y = {y}")
print()

# Multiple unpacking
a, b, c = (1, 2, 3)
print(f"Unpacked (1, 2, 3) → a={a}, b={b}, c={c}")
print()

# ============================================================================
# EXAMPLE 7: Unpacking in Loops
# ============================================================================
# Unpack while iterating

print("Example 7: Unpacking in Loops")
print("-" * 50)

coordinates = [(1, 2), (3, 4), (5, 6)]
print(f"List of tuples: {coordinates}")
print()

print("Unpacking in loop:")
for x, y in coordinates:
    print(f"  ({x}, {y})")
print()

# ============================================================================
# EXAMPLE 8: Swap with Unpacking
# ============================================================================
# Use unpacking to swap variables

print("Example 8: Swap with Unpacking")
print("-" * 50)

a, b = 10, 20
print(f"Start: a={a}, b={b}")

a, b = b, a
print(f"After swap: a={a}, b={b}")
print()

# ============================================================================
# EXAMPLE 9: Tuple as Dictionary Key
# ============================================================================
# Use immutable tuples as keys

print("Example 9: Tuples as Dictionary Keys")
print("-" * 50)

locations = {
    (0, 0): "start",
    (1, 0): "north",
    (0, 1): "east",
    (1, 1): "northeast"
}

print("Game board positions:")
for pos, location in locations.items():
    print(f"  {pos}: {location}")

print()
print(f"Value at (1, 0): {locations[(1, 0)]}")
print()

# ============================================================================
# EXAMPLE 10: Creating Sets
# ============================================================================
# Different ways to create sets

print("Example 10: Creating Sets")
print("-" * 50)

s1 = {1, 2, 3}
print(f"Set: {s1}")

s2 = {"red", "green", "blue"}
print(f"Colors: {s2}")

empty = set()
print(f"Empty: {empty}")

from_list = set([1, 2, 2, 3, 3, 3])
print(f"From list (removes dupes): {from_list}")
print()

# ============================================================================
# EXAMPLE 11: Set Membership
# ============================================================================
# Check if item in set

print("Example 11: Membership Check")
print("-" * 50)

colors = {"red", "green", "blue"}
print(f"Set: {colors}")
print()

print(f"'red' in colors = {'red' in colors}")
print(f"'yellow' in colors = {'yellow' in colors}")
print(f"'blue' not in colors = {'blue' not in colors}")
print()

# ============================================================================
# EXAMPLE 12: Adding to Sets
# ============================================================================
# Add single and multiple items

print("Example 12: Adding Items")
print("-" * 50)

s = {1, 2, 3}
print(f"Start: {s}")

s.add(4)
print(f"After add(4): {s}")

s.update([5, 6])
print(f"After update([5, 6]): {s}")

s.add(3)  # Duplicate - no change
print(f"After add(3) again: {s}")
print()

# ============================================================================
# EXAMPLE 13: Removing from Sets
# ============================================================================
# Remove items from sets

print("Example 13: Removing Items")
print("-" * 50)

s = {1, 2, 3, 4, 5}
print(f"Start: {s}")

s.remove(3)
print(f"After remove(3): {s}")

s.discard(5)
print(f"After discard(5): {s}")

s.discard(99)  # Doesn't error
print(f"After discard(99): {s}")

item = s.pop()
print(f"Popped {item}, set: {s}")
print()

# ============================================================================
# EXAMPLE 14: Set Union
# ============================================================================
# Combine sets (all items)

print("Example 14: Set Union")
print("-" * 50)

a = {1, 2, 3}
b = {2, 3, 4}
print(f"Set a: {a}")
print(f"Set b: {b}")
print()

union = a | b
print(f"a | b (union): {union}")

union2 = a.union(b)
print(f"a.union(b): {union2}")
print()

# ============================================================================
# EXAMPLE 15: Set Intersection
# ============================================================================
# Common items only

print("Example 15: Set Intersection")
print("-" * 50)

a = {1, 2, 3}
b = {2, 3, 4}
print(f"Set a: {a}")
print(f"Set b: {b}")
print()

intersection = a & b
print(f"a & b (intersection): {intersection}")

intersection2 = a.intersection(b)
print(f"a.intersection(b): {intersection2}")
print()

# ============================================================================
# EXAMPLE 16: Set Difference
# ============================================================================
# Items in a but not b

print("Example 16: Set Difference")
print("-" * 50)

a = {1, 2, 3}
b = {2, 3, 4}
print(f"Set a: {a}")
print(f"Set b: {b}")
print()

difference = a - b
print(f"a - b (difference): {difference}")

difference2 = a.difference(b)
print(f"a.difference(b): {difference2}")
print()

# ============================================================================
# EXAMPLE 17: Set Symmetric Difference
# ============================================================================
# Items in either but not both

print("Example 17: Symmetric Difference")
print("-" * 50)

a = {1, 2, 3}
b = {2, 3, 4}
print(f"Set a: {a}")
print(f"Set b: {b}")
print()

sym_diff = a ^ b
print(f"a ^ b (symmetric difference): {sym_diff}")

sym_diff2 = a.symmetric_difference(b)
print(f"a.symmetric_difference(b): {sym_diff2}")
print()

# ============================================================================
# EXAMPLE 18: Remove Duplicates with Sets
# ============================================================================
# Convert list to set to remove duplicates

print("Example 18: Remove Duplicates")
print("-" * 50)

items = [1, 2, 2, 3, 3, 3, 4, 4]
print(f"List with duplicates: {items}")

unique = set(items)
print(f"As set (no duplicates): {unique}")

unique_list = list(unique)
print(f"Back to list: {unique_list}")
print()

# ============================================================================
# EXAMPLE 19: Set Operations Example
# ============================================================================
# Real-world skills example

print("Example 19: Skills Example")
print("-" * 50)

alice_skills = {"Python", "Java", "SQL"}
bob_skills = {"Python", "JavaScript", "SQL"}
print(f"Alice skills: {alice_skills}")
print(f"Bob skills: {bob_skills}")
print()

common = alice_skills & bob_skills
print(f"Common skills: {common}")

all_skills = alice_skills | bob_skills
print(f"All skills: {all_skills}")

alice_only = alice_skills - bob_skills
print(f"Only Alice knows: {alice_only}")

bob_only = bob_skills - alice_skills
print(f"Only Bob knows: {bob_only}")
print()

# ============================================================================
# EXAMPLE 20: Tuple Multiple Return Values
# ============================================================================
# Return multiple values from function

print("Example 20: Multiple Return Values")
print("-" * 50)

def get_user():
    return ("Alice", 30, "Boston")

name, age, city = get_user()
print(f"User: {name}, age {age}, from {city}")
print()

# ============================================================================
# EXAMPLE 21: Set Length and Iteration
# ============================================================================
# Iterate over sets

print("Example 21: Set Iteration")
print("-" * 50)

colors = {"red", "green", "blue"}
print(f"Set: {colors}")
print(f"Length: {len(colors)}")
print()

print("Iterating:")
for color in colors:
    print(f"  {color}")
print()

# ============================================================================
# EXAMPLE 22: Nested Tuples
# ============================================================================
# Tuples containing tuples

print("Example 22: Nested Tuples")
print("-" * 50)

points = ((1, 2), (3, 4), (5, 6))
print(f"Points: {points}")
print()

print(f"points[0] = {points[0]}")
print(f"points[0][0] = {points[0][0]}")
print(f"points[1][1] = {points[1][1]}")
print()

# ============================================================================
# EXAMPLE 23: Set Subsets and Supersets
# ============================================================================
# Check relationships between sets

print("Example 23: Subset and Superset")
print("-" * 50)

a = {1, 2}
b = {1, 2, 3}
c = {1, 2}

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print()

print(f"a.issubset(b) = {a.issubset(b)}")
print(f"b.issuperset(a) = {b.issuperset(a)}")
print(f"a == c = {a == c}")
print(f"a.isdisjoint({4, 5}) = {a.isdisjoint({4, 5})}")
print()

# ============================================================================
# EXAMPLE 24: Tuple with Dictionary Values
# ============================================================================
# Store tuples as values in dictionary

print("Example 24: Tuples as Values")
print("-" * 50)

users = {
    "alice": ("Alice", 30, "Boston"),
    "bob": ("Bob", 25, "NYC"),
    "charlie": ("Charlie", 28, "LA")
}

print("Users:")
for key, (name, age, city) in users.items():
    print(f"  {key}: {name}, {age}, {city}")
print()

# ============================================================================
# EXAMPLE 25: Set Clearing and Copying
# ============================================================================
# Clear and copy sets

print("Example 25: Set Operations")
print("-" * 50)

original = {1, 2, 3}
copy = original.copy()

print(f"Original: {original}")
print(f"Copy: {copy}")

copy.add(4)
print(f"After adding 4 to copy:")
print(f"  Original: {original}")
print(f"  Copy: {copy}")

original.clear()
print(f"After clearing original: {original}")
print(f"Copy still has data: {copy}")

