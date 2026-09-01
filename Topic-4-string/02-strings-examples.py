# Topic 4: Strings - Examples

# Example 1: Access character by index
word = "Python"
print(word[0])
print(word[3])

# Example 2: Negative indexing
print(word[-1])
print(word[-2])

# Example 3: String slicing
print(word[0:3])
print(word[3:])

# Example 4: String length
text = "Hello"
print(len(text))

# Example 5: Uppercase
text = "hello"
print(text.upper())

# Example 6: Lowercase
text = "HELLO"
print(text.lower())

# Example 7: Capitalize
text = "hello"
print(text.capitalize())

# Example 8: Replace
text = "hello"
print(text.replace("l", "L"))

# Example 9: String concatenation
first = "Hello"
second = "World"
result = first + " " + second
print(result)

# Example 10: String repetition
dash = "-"
line = dash * 10
print(line)

# Example 11: Membership test
text = "Python"
print("y" in text)
print("x" in text)

# Example 12: Find substring
text = "Python"
position = text.find("tho")
print(position)

# Example 13: String splitting
sentence = "Hello World Python"
words = sentence.split()
print(words)

# Example 14: String joining
words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(sentence)

# Example 15: F-string formatting
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old"
print(message)

