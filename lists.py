# Working with part of a list

# A slice will create a specific group of items in a list
# To create a slice you must specify the index of the first and last elements
# Python stops one item before the second index
# If you want the first 3 elements you would list 0 and 3 which would return elements 0, 1, 2
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# Output: ['charles', 'martina', 'michael']

# If you omit the first index it starts at the beginning of the list
print(players[:4])
# Output: ['charles', 'martina', 'michael', 'florence']

# If you omit the second index it starts at the provided index and goes to the end of the list
print(players[2:])
# Output: ['michael', 'florence', 'eli']

# Negative indexes work
print(players[1:-3])
# Output: ['martina']

print(players[-2:])
# Output: ['florence', 'eli']

print(players[:-1])
# Output: ['charles', 'martina', 'michael', 'florence']

print("\n------------------\n")

# Looping Through a Slice

# You can use a slice in a for loop
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

print("\n------------------\n")

# Copying a List

# you can store the value of a slice as a copy of a list
# if no idexes are specified the entire list will be copied
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n------------------\n")

# The two lists are truly two seperate objects
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n------------------\n")

# Assigning a list to a variable does not create a copy of the list
# Instead it just references the original list (think points to original object)
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)