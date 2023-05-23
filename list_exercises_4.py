# List Exercises 4

# 4-10 Slices
travel_locations = ['japan', 'greece', 'germany', 'wales', 'scotland', 'new zealand', 'australia', 'portugal', 'spain', 'canada']

print("The first three items in the list are:")
for location in travel_locations[:3]:
	print(location)

print("\nThree items from the middle list are:")
for location in travel_locations[4:7]:
	print(location)

print("\nThe last three items in the list are:")
for location in travel_locations[-3:]:
	print(location)

print("\n--------------------\n")

# 4-11 My Pizzas, Your Pizzas
my_pizzas = ['cheese', 'pineapple', 'pepperoni', 'roasted corn', 'pine nut']
friend_pizzas = my_pizzas[:]

my_pizzas.append('bbq')
friend_pizzas.append('hawaiian')

print("My favorite pizzas are:")
print(my_pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)