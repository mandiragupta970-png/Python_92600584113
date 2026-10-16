class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

s1 = Student("Manasvi")
s2 = Student("Vishruti")

print("Name:", s1.name)
print("College:", s1.college)
print("Name:", s2.name)
print("College:", s2.college)
