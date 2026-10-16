f = open("sample.txt", "w")
f.write("Hello Python\n")
f.write("File handling")
f.close()

f = open("sample.txt", "a")
f.write("\nWelcome to Python")
f.close()

f = open("sample.txt", "r")
print(f.read())
f.close()
