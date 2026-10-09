# 1. Using if statement
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")


# 2. Using if-else statement
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# 3. Using if-elif-else statement
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
