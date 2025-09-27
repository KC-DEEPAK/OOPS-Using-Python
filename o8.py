class Person:
    def __init__(self,name,eyes):
       self.name=name
       self.eyes=eyes
class Student(Person):
    def __init__(self,name,eyes,USN):
        super().__init__(name,eyes)
        self.usn=USN
    def standarded(self):
        print("I am studing in 10 th class..")
class Faculity(Person):
    def __init__(self,name,eyes,Department):
        super().__init__(name,eyes)
        self.department=Department
    def subject():
        print("I am taking a python subject..")
faculity_1=Faculity("Raju",2,"CSE")
print(faculity_1.department)
student_1=Student("kiran",2,"CS042")
student_1.standarded()
print(student_1.name)
print(student_1.usn)