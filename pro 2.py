# Program 2: Data Types and Type Casting with user input

num_str = input("Enter an integer string: ")
float_str = input("Enter a floating-point string: ")

converted_int = int(num_str)
converted_float = float(float_str)

back_to_str = str(converted_int)

print("\n--- Converted Types and Values ---")
print(f"converted_int: {converted_int} (Type: {type(converted_int)})")
print(f"converted_float: {converted_float} (Type: {type(converted_float)})")
print(f"back_to_str: '{back_to_str}' (Type: {type(back_to_str)})")
