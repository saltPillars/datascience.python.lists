# List Exercises 1

# 3-4 Guest List
dinner_list = ['bob', 'chuck', 'ruth', 'jean', 'erin']
print(f"Dear {dinner_list[0].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[1].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[2].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[3].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[4].title()}, I would like to invite you to dinner.")

# 3-5 Changing Guest List
unavailable = dinner_list.pop(3)
print(f"\nOh no! {unavailable.title()} isn't able to make it!")
dinner_list.insert(3, 'jill')
print(f"{dinner_list[3].title()} is available to take their place.")
print(f"Dear {dinner_list[0].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[1].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[2].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[3].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[4].title()}, I would like to invite you to dinner.")

# 3-6 More Guests
print(f"\nGREAT NEWS! I've found a bigger table!")
dinner_list.insert(0, 'Alaina')
dinner_list.insert(2, 'Marc')
dinner_list.append('Brian')
print(f"Dear {dinner_list[0].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[1].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[2].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[3].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[4].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[5].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[6].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[7].title()}, I would like to invite you to dinner.")

# 3-7 Shrinking Guest List
print(f"\nI'm sorry guys, my new table wont be here in time.")
cut = dinner_list.pop()
print(f"Dear {cut.title()}, I'm sorry, but you're cut")
cut = dinner_list.pop()
print(f"Dear {cut.title()}, I'm sorry, but you're cut")
cut = dinner_list.pop()
print(f"Dear {cut.title()}, I'm sorry, but you're cut")
cut = dinner_list.pop()
print(f"Dear {cut.title()}, I'm sorry, but you're cut")
cut = dinner_list.pop()
print(f"Dear {cut.title()}, I'm sorry, but you're cut")
cut = dinner_list.pop()
print(f"Dear {cut.title()}, I'm sorry, but you're cut")
print(f"Dear {dinner_list[0].title()}, I would like to invite you to dinner.")
print(f"Dear {dinner_list[1].title()}, I would like to invite you to dinner.")

del dinner_list[0]
del dinner_list[0]

print(dinner_list)