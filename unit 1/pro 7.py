# program 7: Write a program to create a dictionary and demonstrate dictionary methods and iteration.

student = {}
count = int(input("How many fields to add? "))

for i in range(count):
    key = input("Enter key (e.g. name, age): ")
    value = input("Enter value: ")
    student[key] = value

print("\nDictionary:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

print("\nIteration:")
for k, v in student.items():
    print(f"{k} : {v}")
