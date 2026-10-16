f = open("demo.txt", "w")
f.write("Python Programming")
f.close()

f = open("demo.txt", "r")

print("Initial position:", f.tell())

print("Data:", f.read(6))
print("Current position:", f.tell())

f.seek(0)
print("Position after seek:", f.tell())

print("Data:", f.read(6))
print("Current position:", f.tell())

f.close()
