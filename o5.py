class Human:
    def __init__(self,heart):
        print("calling init from Human Class")
        self.num_eyes=2
        self.num_nose=1
        self.heart=heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male:
    def __init__(self,name):
        print("calling a init from Male Class")
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can Code")
    def morning(self):
        print("I want to study at 6:00 AM")
    def night(self):
        print("I want to sleep at 11:00 PM")
class Female:
    def morning(self):
        print("I want to study at 5AM")
    def night(self):
        print("I want to seep at 10o clock")
class Boy(Human,Male):
    def __init__(self,name,heart,language):
        Human. __init__(self,heart)
        Male.__init__(self,name)
        self.language=language
    def sleep(self):
        print("I can Sleep")
    def work(self):
        print("I can Learn")
    def display(self):
        print(f"I My name is {self.name} I am learning {self.language} language")
boy_1=Boy("Rahul",1,"python")
boy_1.flirt() 
boy_1.work() # it only print a human class work because by passing an argument we pass 1st human class thus it is 1st prefirance.. 
# we want to print Male class work function 
Male.work(boy_1)
# yes we have done it 
#Boy.work(boy_1)# this is one way 
print(Boy.mro())# order of Boy class  
print(boy_1.num_nose)
print(boy_1.num_eyes)
print(boy_1.language)
boy_1.display()
# this is the topic of multiple inheritance which we can inheret the two or more class
boy_1.morning()
boy_1.night()
