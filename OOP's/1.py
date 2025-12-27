# class Student:
#     pass
# print(id(Student))
# obj1=Student
# print(id(obj1))
# obj2=Student
# print(id(obj2))


# class Student:
#     '''helooooooo'''
#     school='shss'
#     def showdetail():
#         print("welcome to school")
# print(dir(Student))
# print(Student.__doc__)
# # obj1=Student



# ...........12/11/25.......

# class Student:
#     pass
# print(id(Student))
# obj1=Student()
# print(id(obj1))
# obj2=Student()
# print(id(obj2))


# class Student:
#     def __init__(self):
#         print("contructor called")

# obj1=Student
# obj=Student()

# class Student:
#     def __init__(self):
#         print("contructor called")
#         print(id(self))

# obj=Student()
# print(id(obj))


# class Student:
#     def __init__(self,name,quali):
#         self.n=name
#         self.q=quali

# obj1=Student('neeraj','M.tech')
# obj2=Student('mahak','M.tech')
# print(obj1.n,obj2.n)



# class Student:
#     def __init__(self,name,rollno):
#         self.n,self.r=name,rollno
#         print(self.n,self.r)
#     def addnew(self,contact):
#         self.c=contact
#         print(self.n,self.r,self.c,self.city)
# obj1=Student('mahak',52)
# x=eval(input("entre contact details:"))
# # obj1.addnew(x)
# obj1.city='Bhopal'
# obj1.addnew(x)
# print(obj1.n,obj1.r,obj1.c,obj1.city)



# class Student:
#     school_name='shssssss..'
#     def __init__(self,name,rollno):
#         self.n,self.r=name,rollno
#         Student.gread='10th'
#         # print(self.n,self.r)
#         print(Student.school_name)
#     def addnew(self,):
#         Student.principal='Python'
#         # print(self.n,self.r,self.c,self.city)
#         print(Student.school_city,Student.gread)

# Student.school_city='bhopal'
# obj1=Student('mahak',52)
# obj1.addnew()
# print(Student.principal)


#...............14/11/25.................

# class Student:
#     def __init__(self,name,rollno):
#         x=10
#         print(x)
#     def new(self):
#         y=10
#         print(y)
#         print(x)

# obj=Student()
# obj.new()


# class Book:
#     price=100
#     def __init__(self,title,total_page):
#         self.t=title
#         self.tp=total_page
#     @classmethod
#     def update_price(cls,p):
#          cls.price=p
# obj = Book('python',500)
# print(obj.t,obj.tp,Book.price)   # output - python 500 100

# x=float(input("entre updated price"))
# obj.update_price(x)
# obj1=Book('python',510)
# print(obj.t,obj.tp,Book.price)   # output - python 500 200




# class web:
#     def __init__(self,name):
#         self.n=name
#     def great():
#         print("welcome to my web page")
   
# # obj =web
# # obj.great()
# obj=web('ecomm')
# obj.great()




# class web:
#     def __init__(self,name):
#         self.n=name
#     @staticmethod
#     def great():
#         print("welcome to my web page")
   
# # obj =web
# # obj.great()
# obj=web('ecomm')
# obj.great()


# .............15/11/25......
# class Student:
#     x=10
#     y=20
#     def new(self):
#         print("from new")
    
# obj=Student
# obj.new()

# .............single level inheritance...


# class Parent:
#     car="nexon"
#     def home(self):
#         print("home from parent")
# class Child(Parent):
#     pass
# obj=Child()
# print(obj.car)
# obj.home()




# class Parent:
#     car="nexon"
#     def home(self):
#         print("home from parent")
# class Child(Parent):
#     def home(self):
#         print("home from Child")
#         super().home()                # to acess parent property
# obj=Child()
# print(obj.car)
# obj.home()





# ........ 17/11/2025......  revesion class object

# class Student:
#     school="Cybrom"
#     gread="10th"
#     def __init__(self,name,rollno):
#         self.n,self.r=name,rollno
#         print(id(self))
#     @classmethod
#     def upgread_grd(cls,new_gread):
#         print(id(cls))
# obj1=Student('mahak',101)
# obj1.upgread_grd('11th')
# print(id(obj1))
# print(id(Student))


#.......... 18/11/25...            multi - leve inheritance


# class GrandParent:
#     def home(self):
    
#         print("home from grand parent")
#     def car(self):
#         print("car from gp")

# class Parent(GrandParent):
#     def home(self):
#         super().home()
#         print("home from parent")
#     def bank(self):
#         print("bank from parent")

# class Child(Parent):
#     def home(self):
#         super().home()
#         print("home from child")
# obj=Child()
# obj.car()
# obj.bank()
# obj.home()

# ....... Multiple inheritance

# class Parent1:
#     def home(self):
#         print("home from parent1")
#         Parent2.home(self)
#     def car(self):
#         print("car from parent1")

# class Parent2:
#     def home(self):
#         print("home from parent2")
#     def bank(self):
#         print("bank from parent2")

# class Child(Parent1,Parent2):
#     def home(self):
#         super().home()
#         print("home from child")

# obj=Child()
# obj.home()
# obj.bank()
# obj.car()




# .......... hierarical inhertance....

# class Parent1:
#     def home(self):
#         print("home from parent1")
#     def car(self):
#         print("car from parent1")

# class Child1(Parent1):
#     def home(self):
#         super().home()
#         print("home from child1")


# class Child2(Parent1):
#     def home(self):
#         super().car()
#         print("home child2")
    

# obj=Child1()
# obj2=Child2()
# obj.home()
# obj2.home()


# ...... Hybrid Inheritance............

# class Parent1:
#     def home(self):
#         print("home from parent1")
#     def car(self):
#         print("car from parent1")

# class Child1(Parent1):
#     def home(self):
#         super().home()
#         print("home from child1")


# class Child2(Parent1):
#     def home(self):
#         super().home()
#         print("home child2")

# class Child3(Child1,Child2):
#     def home(self):
#         super().home()
#         print("Child3 home ")

    

# # obj=Child1()
# # obj2=Child2()
# obj3=Child3()
# # obj.home()
# # obj2.home()
# obj3.home()


# ................abstractmethod....

# from abc import ABC, abstractmethod

# class WebPage(ABC):
#     def dashboard(self):
#         print("wlcome to dashboard")
#     def userprofile(self):
#         print("welcome to profile page")
#     @abstractmethod
#     def login(self,user,password):
#         pass
# class user(WebPage):
#     def login(self, user, password):
#         print("login sacefully")
# obj=user()
# obj.dashboard()
# obj.login("mahak",54)


# ........   Encapsulation.....

# .......   1) public

# class A:
#     x=10
#     def show(self):
#         print("hello")
# class B(A):
#     pass
# obj=B()
# print(obj.x)
# obj.show()
# print(A.x)


# .......   2) protected   "not supported in python"

# class A:
#     _x=10
#     def _show(self):
#         print("hello")
# class B(A):
#     pass
# obj=B()
# print(obj._x)
# obj._show()
# print(A._x)   # because here it is accessable outside class




# .......   3) private

class A:
    __x=10
    def __show(self):
        print("hello")
class B(A):
    pass
obj=B()
# print(obj.__x)
# obj.__show()
# print(A.__x)


print(A._A__x)

# print(dir(A))