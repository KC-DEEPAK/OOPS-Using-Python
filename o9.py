class A:
    def display(self):
        print("It is from class  A")
class B(A):
    def display(self):
        print("It is from class B")
class C:
    def display(self):
        print("It is from class C")
class D(B,C):
    def display(self):
        print("It is from class D")
        super().display()
d1=D()
d1.display()
#parent class is university and its attribute is university name and method is show details
#another class is course and branch course have a show detail method it sholud show the university name and details 
#branch name and details  another class is student is name and course name and university name 
#another class name is faculity branch
class University:
    def __init__(self,uni_name):
        self.uni_name=uni_name
    def show_details(self):
        print(f"University name is {self.uni_name} in Hassan")
class Course(University):
        def __init__(self,uni_name,course):
            University.__init__(self,uni_name)
            self.course=course
        def show_details(self):
            print(f"Course name is {self.course} which University name is {self.uni_name}")
class Branch(University):
    def __init__(self,uni_name,branch):
        University.__init__(self,uni_name)
        self.branch=branch
    def show_detals(self):
        print(f"Branch name is {self.branch} which university name is {self.uni_name}")
class Student(Course,Branch):
    def __init__(self,s_name,uni_name,course,branch):
        Course.__init__(self,uni_name,course)
        Branch.__init__(self,uni_name,branch)
        self.s_name=s_name
    def show_details(self):
        print(f"MY name is {self.s_name} MY Branch is {self.branch} MY course name is {self.course} MY University Name is {self.uni_name} ")
student1=Student("Deepu","RIT","SE","CS")
student1.show_details()
