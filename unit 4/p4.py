class Student:
    school = "ABC School"

    def instance_method(self):
        print("Instance method called")

    @classmethod
    def class_method(cls):
        print("Class method:", cls.school)

    @staticmethod
    def static_method():
        print("Static method called")

s = Student()

s.instance_method()
Student.class_method()
Student.static_method()
