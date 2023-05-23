# Tuples

# Lists work well for collections that will change throughout a program
# Sometimes there is a need for a list that cannot change
# For this we use tuples, tuples are immutable

# A tuple looks likea list except it is declared with parenthesis rather than brackets

# Once it is defined you can access items by index like a list
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Python returns a type error if any element is attempted to be changed
# dimensions[0] = 250
# Output: TypeError: 'tuple' object does not support item assignment

# Tuples are defined by presence of commas
# if you want to define a tuple with on element you need a trailing comma
my_t = (3,)

print("\n----------------------\n")

# You can loop through tuples just like lists
for dimension in dimensions:
	print(dimension)

print("\n----------------------\n")

# Writing over a tuple

# We cannot modify a tuple but we can assign a new value to a variable that represents a tuple
dimensions = (200, 50)
print("Original Dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
	print(dimension)

