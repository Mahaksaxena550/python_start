# ........positinal argument...........

# def fun_name(x,y,z):
#     print(f'{x,y,z} hello')
# p= int(input("entre value"))
# q= input("entre value")
# r= int(input("entre value"))

# fun_name(p,q,r)
 
# ...... default argument.....


# def fun_name(x=0,y=0,z=0):
#     print(f'{x,y,z} hello')
# p= int(input("entre value"))
# q= input("entre value")
# r= int(input("entre value"))
# fun_name()
# fun_name(p)
# fun_name(p,q)
# fun_name(p,q,r)




#  .........variable length positional argument...

# def fun_name(*args):
#     print(args)
#     print(type(args))
# fun_name()
# fun_name(10,20,30,40,50,60,70,"mahak")



# def fun_name(*args):
#     print(args)
#     print(type(args))

# t=eval(input("enter values tuple:"))
# fun_name(t)


# .....example...

# def add_all(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(f'sum is {sum}')
# add_all(10,20,30,40,50)

# def add_all(*n):
#     sum=0
#     for i in n:
#         print(i)
#         for j in i:
#             sum=sum+j    
#     print(f'sum is {sum}')
# var=eval(input("entre any collection:"))
# add_all(var)

# ...............unpaking logic.............

# def add_all(*n):
#     sum=0
#     for i in n:
#         sum=sum=i
#     print (f'sum of {sum}')

   
# var=eval(input("entre any collection:"))
# add_all(*var)

# ...........error statement.........
# def display(x=0,y):
#     print(f'{x,y}')

# display(10,20,)

# ...........how to write in squence....

# def display(x,y=0,*z):
#     print(f'{x,y,z}')
# display(10,20,30,40,50)


# def fun_name(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# fun_name(x=10,y=2,z=40)

def fun_name(**kwargs):
    print(kwargs)
    print(type(kwargs))
var=eval(input("entre any dict:"))
fun_name(**var)