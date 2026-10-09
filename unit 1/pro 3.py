# Program 3: Operators with user input

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

print("\n--- Arithmetic Operations ---")
print(f"a + b  = {a + b}")
print(f"a - b  = {a - b}")
print(f"a * b  = {a * b}")
print(f"a / b  = {a / b if b != 0 else 'Undefined (div by 0)'}")
print(f"a // b = {a // b if b != 0 else 'Undefined'}")
print(f"a % b  = {a % b if b != 0 else 'Undefined'}")
print(f"a ** b = {a ** b}")

print("\n--- Relational Operations ---")
print(f"a > b  : {a > b}")
print(f"a == b : {a == b}")
print(f"a != b : {a != b}")

print("\n--- Logical Operations ---")
p = input("Enter 'true' or 'false' for condition P: ").strip().lower() == "true"
q = input("Enter 'true' or 'false' for condition Q: ").strip().lower() == "true"

print(f"P AND Q : {p and q}")
print(f"P OR Q  : {p or q}")
print(f"NOT P   : {not p}")
