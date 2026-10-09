# program 9: Write a program to define and use user-defined functions with different types of arguments.
def greet(name, message="Welcome!"):
    print(f"Hello {name}, {message}")


def calculate_sum(*numbers):
    return sum(numbers)

user_name = input("Enter your name: ")
greet(user_name)

nums = list(map(float, input("Enter numbers to sum: ").split()))
print("Total Sum:", calculate_sum(*nums))
