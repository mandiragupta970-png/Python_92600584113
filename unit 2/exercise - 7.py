
# 1. List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [n * n for n in numbers]

print("List Comprehension:")
print(squares)


# 2. Dictionary Comprehension
squares_dict = {n: n * n for n in numbers}

print("\nDictionary Comprehension:")
print(squares_dict)


# 3. Set Comprehension
square_set = {n * n for n in numbers}

print("\nSet Comprehension:")
print(square_set)
