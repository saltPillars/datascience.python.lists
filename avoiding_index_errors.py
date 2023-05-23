# Avoiding Index Errors

# Index errors are common. Occur when trying to access an element that doesn't exist
motorcycles = ['honda', 'yamaha', 'suzuki']

# results in index error due to no element at index 3
print(motorcycles[3])

# Use bult in index indicators to avoid
print(motorcycles[-1])

# The only time -1 will result in index error is if list is empty
motorcycles = []
print(motorcycles[-1])

# If index errors occur and you cant figure it out print the list and trace data