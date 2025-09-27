#Hierarchical Inheritance
class Human:
    def __init__(self,name,age):
        print("calling init from human class")
        self.name=name
        self.age=age
    def showDetails(self):
        print(f"name:{self.name},age:{self.age}")
    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self,m_name,age,location):
        print("calling init from male class")
        Human.__init__(self,m_name,age)
        self.location=location
    def sleep(self):
        print("I can sleep whole day.")
class Female(Human):
    def __init__(self,name,age,can_dance):
        super().__init__(name,age)
        self.know_dancing=can_dance
    def work(self):
        print("I can code")
# creating a object of female
female_1=Female("Sanjana",34,True)
print(female_1.know_dancing)
# creating a object of male
male_1=Male("GOWTHAM",36,"MYSORE")
male_1.sleep()