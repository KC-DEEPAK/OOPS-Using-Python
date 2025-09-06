#class Instructor:
#    pass
#instructor_1=Instructor()
#instructor_1.name="DEEPAK"
#instructor_1.address="CKM"
#print(instructor_1.name)
#print(instructor_1.address)
#THIS METHOD IS DIFICULT AND THATS why we are using a init function to implement the repeted name and address
# thats why we are creating a init function....
class Instructor:
    def __init__(self,instructor_name,address):
        self.name=instructor_name
        self.address=address
        self.followers=0

instructor_1=Instructor("deepak","ckm") 
print(instructor_1.name)
print(instructor_1.followers)
instructor_2=Instructor("guru","hassan")
print(instructor_2.name)
print(instructor_2.address)
# BY Using a init function it first declare the comman thinks in the instructor


    