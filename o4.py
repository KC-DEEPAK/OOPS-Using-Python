class Human:
    def __init__(self,num_heart):# which can be defined 
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("I can eat")#this are method
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()# for access the base class metheod
        print("I can code")
    def display(self):
        print(f"Hi, I am {self.name} and I have {self.num_heart} Heart")
    
male_1=Male("Ramu",1)
male_1.eat()
male_1.work()# this is called overedden concept
male_1.flirt()
print(male_1.num_eyes)
print(male_1.name)
male_1.display()
 