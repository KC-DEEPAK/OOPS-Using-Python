class Instructor:
    followers=0
    following=0
    def __init__(self,name,address):
            self.name=name
            self.address=address
    def display(self,subject_name):# this is called metheod in oops and it used to 
          print(f"Hi i am {self.name} i am teaching a {subject_name} ")
    def update_followers(self,followers_name):
          self.followers+=1
          print(f"follower name is :{followers_name}")
    def update_following(self,following_name):
          self.following+=1
instructor_1=Instructor("deepak","iran")# this is called as object creation
instructor_1.display("Dsa")
instructor_1.update_followers("harshith")
instructor_1.update_following("harshith")
print(f"followers are :{instructor_1.followers}")
print(f"following are :{instructor_1.following}")
instructor_2=Instructor("manu","skp")
instructor_2.display("OOPS")
print(f"followers are :{instructor_2.followers}")
print(f"following are :{instructor_2.following}")