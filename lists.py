# List Exercises 3

# 4-3 Counting to Twenty
for value in range(1, 21):
	print(value)

print("\n--------------------\n")

# 4-4 One Million
#for value in range(1, 1_000_001):
	#print(value)

print("\n--------------------\n")

# 4-5 Summing a million
million = range(1, 1_000_001)
print(min(million))
print(max(million))
print(sum(million))

print("\n--------------------\n")
# 4-6 Odd Numbers
odd_numbers = range(1, 21, 2)
for number in odd_numbers:
	print(number)

print("\n--------------------\n")
# 4-7 Threes
threes = range(3, 31, 3)
for number in threes:
	print(number)

print("\n--------------------\n")
# 4-8 Cubes
cubes = []
for value in range(1, 11):
	cubes.append(value ** 3)

for cube in cubes:
	print(cube)

print("\n--------------------\n")
# 4-9 Cube Comprension
cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
	print(cube)