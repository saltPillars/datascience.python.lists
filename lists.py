# Numerical Lists

# Lists are ideal for storing sets of numbers

# range() is used to generate a series of numbers
# It starts the count at the number you provide
# Don't fall into off-by-one errors
for value in range(1, 5):
	print(value)
# Output: 1-4

print("\n---------\n")

for value in range(1, 6):
	print(value)
# Output: 1-5

print("\n---------\n")

# You can also pass range() only one value and it will start at 0
for value in range(10):
	print(value)
# Output: 1-9

print("\n---------\n")

# You can convert range into a list by wrapping range() with list()
numbers = list(range(1,6))
print(numbers)
# Output: [1, 2, 3, 4, 5]

# If you pass a third argument to range() Python uses it to size steps
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# Output: [2, 4, 6, 8, 10]

# range() is very versatile 
# To put the first 10 squares of numbers you could do:
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Can be written more concisely
squares = []
for value in range(1, 11):
	squares.append(value ** 2)

print(squares)

# Python has built in functions for working with lists of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))
# Output: 1

print(max(digits))
# Output: 10

print(sum(digits))
# Output: 55

# List Comprehensions allow you to generate complex lists (such as squares) in one line of code
# List comprehension combines for loop and creation of new elements into one line and automatically appends each new element
squares = [value ** 2 for value in range(1, 11)]
print(squares)