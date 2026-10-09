# Program 4: String Operations with user input

user_string = input("Enter a sentence or string: ")

print("\n--- String Slicing ---")
print("First 5 characters:", user_string[:5])
print("Reversed string:", user_string[::-1])

print("\n--- Built-in String Functions ---")
print("Uppercase:", user_string.upper())
print("Lowercase:", user_string.lower())
print("Title Case:", user_string.title())
print("Stripped whitespace:", user_string.strip())
print("Total Character Count:", len(user_string))

search_term = input("\nEnter a character or word to search for: ")
print(f"Does it contain '{search_term}'? : {search_term in user_string}")
