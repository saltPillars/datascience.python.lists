# Organizing Lists

# .sort() permanently organizes the list in ascending order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort()
print(cars)

# .sort(reverse=True) permanently organizes the list in descending order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\n{cars}")

cars.sort(reverse=True)
print(cars)

# .sorted() temporarily organizes lists
# .sorted(reverse=True) works here as well
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(f"{cars}")

print("Here is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(f"{cars}")

# .reverse() permanently organizes list in reverse of original order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\n{cars}")

cars.reverse()
print(cars)

# len() returns the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\n {len(cars)}")