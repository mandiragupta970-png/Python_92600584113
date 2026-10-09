# program 8: Write a program to explain mutable and immutable objects in Python.
num = int(input("Enter an integer: "))
print("Value:", num, "| Memory ID:", id(num))
num += 10
print("After +10:", num, "| Memory ID:", id(num), "(ID changes -> Immutable)")


my_list = input("\nEnter list elements: ").split()
print("List:", my_list, "| Memory ID:", id(my_list))
my_list.append(input("Enter item to append: "))
print("Updated List:", my_list, "| Memory ID:", id(my_list), "(ID same -> Mutable)")
