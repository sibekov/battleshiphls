# class Dog():

#     #CLASS OBJECT ATTIBUTE

#     species = "mammal"
    

#     def __init__(self,breed,name):
#         self.breed=breed
#         self.name=name
        

# mydog = Dog(breed="Lab",name="Sammy")
# otherdog=Dog(breed="haskie",name="bobie")
# print((mydog.name,mydog.species))
# print(otherdog.name)

######################################################################################

# class Circle():
#     pi = 3.14

#     def __init__(self,radius=1):
#         self.radius=radius

#     def area(self):
#         return self.radius*self.radius*Circle.pi

#     def set_radius(self,new_r):
#         self.radius = new_r



# myc=Circle()
# myc.set_radius(999)
# print(myc.area())

#INHERITANCE

# class Animal():

#     def __init__(self):
#         print("ANIMAL CREATED")

#     def whoAmI(self):
#         print("ANIMAL")

#     def eat(self):
#         print("EATING")


# class Dog(Animal):

#     def __init__(self):
#         Animal.__init__(self)
#         print("DOG CREATED")

#     def bark(self):
#         print("Whoof Whoof")


# mydog=Dog()

# mydog.whoAmI()
# mydog.eat()
# mydog.bark()



    
