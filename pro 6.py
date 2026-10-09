# program 6 : Write a program to illustrate the use of tuples and sets with basic operations.

user_input = input("Enter tuple elements (space-separated): ").split()
my_tuple = tuple(user_input)

print("Tuple:", my_tuple)
print("First Element:", my_tuple[0] if my_tuple else "Empty")
print("Total Count:", len(my_tuple))

set1 = set(input("Enter Set 1 elements: ").split())
set2 = set(input("Enter Set 2 elements: ").split())

print("Union (All unique):", set1 | set2)
print("Intersection (Common):", set1 & set2)
print("Difference (Set1 - Set2):", set1 - set2)
