# Program 5: Lists with user input

raw_input = input("Enter numbers separated by spaces (e.g., 10 5 8 20 3): ")

numbers = [int(x) for x in raw_input.split()]

print("Your List:", numbers)

if numbers:
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])
    print("Sliced List (index 1 to 3):", numbers[1:4])

    squares = [x**2 for x in numbers]
    evens = [x for x in numbers if x % 2 == 0]

    print("\n--- List Comprehensions ---")
    print("Squared values:", squares)
    print("Even values only:", evens)
