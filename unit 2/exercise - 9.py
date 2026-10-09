
# Iterable
numbers = [10, 20, 30, 40, 50]

print("Iterable:")
for num in numbers:
    print(num)


# Iterator
print("\nIterator:")

numbers = [10, 20, 30, 40, 50]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
