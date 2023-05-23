# Changing, Adding, and Removing Elements

# Changing is similar to calling and element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# .append adds an element to a list
motorcycles.append('honda')
print(motorcycles)

# Empty lists can be created and elements can be added dynamically
motorcycles = []
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('honda')
motorcycles.append('ducati')
print(motorcycles)

# Elements can be inserted at any position using .insert()
# Elements are shifted one "down" the list
motorcycles.insert(0, 'harley')
print(motorcycles)

# Elements can be removed with del
# Remaining elements are shifted "up" the list
# Removed elements are permanently removed and no longer accessible
del motorcycles[0]
print(motorcycles)

# The .pop() method removes the element and makes it accessible
# popping an element comes off the top (end) of the stack
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# We can also pop from any position in the list
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")
print(motorcycles)

# .remove() will remove an element by the value rather than position
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# you can use stored strings to provide the value to remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")