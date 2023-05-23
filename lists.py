# Indentation and Loop Errors 

# Indentation determines how a line, or group of lines, is related
# More complex code can have multiple levels of indentation

# Forgetting to Indent
# Python will remind you if you forget to indent
#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#print(magician)

# Output: IndentationError: expected an indented block after 'for' statement on line 9

# Forgetting to Indent Additional Lines
# If a loop is behaving weirdly make sure all lines in the loop are indented.
# A runtime error wont be thrown here so you'll have to check you output an make sure its right
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# If you indent when it doesn't need to be Python will throw an error
message = "Hello Python world!"
#	print(message)

# Output: IndentationError: unexpected indent

# If you indent a line after the loop that shouldn't it will be ran with the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
	
	print("Thank you everyone, that was a great magic show!")

# Output: Prints all 3 lines for each item in the list

# Forgetting the colon results in a syntax error
magicians = ['alice', 'david', 'carolina']
#for magician in magicians
#	print(magician)

# Output: SyntaxError: expected ':'