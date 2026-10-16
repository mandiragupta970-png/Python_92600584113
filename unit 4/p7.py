class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.show()

print(D.mro())

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s = Student("Rahul")
print(s)
