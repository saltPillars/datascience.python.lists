# List is a collection of items in no particular order
# Square brackets indicate al list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements
# To access elements in a list write the name of the list followed by thte index in brackets
# FIRST ITEM IS 0 NOT 1
print(bicycles[0])

# Items in a list can be treated like an ordinary object of that type
print(bicycles[2].upper())
print(f"My first bike was a {bicycles[1].title()}")

# Can acces last item at index -1. -2 will pull second to last and so on.
print(bicycles[-1])