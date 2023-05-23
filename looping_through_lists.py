# Looping Through Lists

magicians = ['alice', 'david', 'carolina']

# for loop iterates through the entire loop
# uses a temporary variable to be associated with item in list
# make temporary variable meaningful name
for magician in magicians:
	print(magician)

# You can do anything you want in a for loop
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")

# You can write as many lines in a loop as you want
# Any line thta is indented is considered inside the loop
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}\n")

#Any lines of code after the loop are executed once the loop ends
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}\n")
print("Thank you, everyone. That was a great magic show!")