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

##################################33classes@###################33333
# class Customer:
#     """
#     Creates an instance of Customer
#     """
#     def __init__(self,fname,lname,email,phone):
#         self.fname=fname
#         self.lname=lname
#         self.email=email
#         self.phone=phone


# customer_one=Customer("Theon","Geyjoy","t.gj@mail.com","123456789")
# print(customer_one)
# print(customer_one.fname)
# print(customer_one.lname)
# print(customer_one.email)

class Bird:
    """
    Bird class
    """
    def __init__(self,kind,call):
        self.kind=kind
        self.call=call

    #behaviour
#     def description(self):
#         """
#         describe the bird
#         """
#         return F"A {self.kind} goes {self.call}"

# owl = Bird('Owl',"twit Twoo!")
# print(owl.description())

# class Orderitem:
#     """
#     Creates an instance of Oderitem
#     """
#     def __init__(self,item,price,quantity):
#         self.item=item
#         self.price=price
#         self.quantity=quantity

#     def description(self):
#         return f"{self.quantity} X {self.item} at $ {self.price} each."

# order_item_one=Orderitem("bowtie",10,3)
# print(order_item_one)
# print(order_item_one.price)
# print(order_item_one.quantity)
# print(order_item_one.description())
# order_item_two=Orderitem("Fez",25,1)
# print(order_item_two.description())
# class User():
#     """
#     Creates an instance of user
#     """
#     def __init__(self,username,email,subscribed):
#         self.username=username
#         self.email=email
#         self.subscribed = subscribed

#     def description(self):
#         """
#         Describes the instance of User
#         """
#         return f"user:{self.username},email:{self.email},subscribed:{self.subscribed}"


# user_one=User("arnol","arnold@email.com",True)

# print(user_one.email)
# user_one.email="murpy@email.com"
# print(user_one.description())
# class Contactinfo():
#     """
#     Creates an instance of Contactinfo
#     """
#     about="Contact information for customer"
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email

#     def description(self):

#         return f"name:{self.name} email:{self.email}"

# print(Contactinfo.about)

# contact=Contactinfo("dave","lister@email.com")

# print(contact.description())

# class BlogPost():
#     """
#     Creates an instance of BlogPost
#     """
#     def __init__(self,title,content,author):
#         self.title=title
#         self.content=content
#         self.author=author

#     def get_overview(self):
#         return f"<{self.title}> by <{self.author}>"

#     def full_info(self):
#         return f"Blog post:<{self.title}>,Content:<{self.content}>Author:<author>"

# post=BlogPost("Python Classes","Python is know as an object-oriented language...","Code institute")

# print(post.get_overview())
# print(post.full_info())
class JobListing():
    """
    Creates an instance of Jbolisting
    """
    def __init__(self,job_title,department):
        self.job_title=job_title
        self.department=department

    def description(self):
        return f"job opening for {self.job_title} in {self.department} department"

class SalesManager(JobListing):
    def __init__(self,salary):
        JobListing.__init__(self,"Sales Manager","Sales")
        self.salary=salary
    

sales_manager=SalesManager(45000)
print(sales_manager.description())
print(sales_manager.salary)


