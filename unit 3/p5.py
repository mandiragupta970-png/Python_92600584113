from datetime import datetime

name = input("Enter your name: ")

now = datetime.now()

print("\nHello", name)
print("Current Date:", now.strftime("%d-%m-%Y"))
print("Current Time:", now.strftime("%H:%M:%S"))
