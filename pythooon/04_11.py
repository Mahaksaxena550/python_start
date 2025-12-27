# def outer(x):
#     def inner ():
#         print("welcome")
#         x()
#     return inner
# def display():
#     print("hello")
# res = outer(display)
# res()


# def outer(x):
#     def inner ():
#         print("welcome")
#         x()
#     return inner
# @outer
# def display():
#     print("hello")
# res = outer(display)
# display()


# def outer(x):
#     def inner (p,q):
#         p=p+5
#         q=q+10
#         x(p,q)
#     return inner
# @outer
# def display(x,y):
#     print(x+y)

# display(10,20)



# def decorator(x):
#     def inner (p,q,r):
#         p=p+5
#         q=q+10
#         r=r+15
#         z=x(p,q,r)
#         return z
#     return inner
# @decorator
# def add(a,b,c):
#     return a+b+c
# res=add(2,4,6)
# print(res)





# def decorator(x):
#     def inner (p,q,r):
#         p=p+5
#         q=q+10
#         r=r+15
#         z=x(p,q,r)
#         return z
#     return inner
# @decorator
# def add(a,b,c):
#     return a-b*c
# res=add(2,4,6)
# print(res)



# def decorator(even_no):
#     def inner(p,q,r):
#         p=p-1
#         even_no(p,q+1,r)
#     return inner
# @decorator
# def even_no(start,stop,step):
#     for i in range(start,stop,step):
#         print(i)

# s,e,sd=2,101,2
# even_no(s,e,sd)





# def decorator(even_no):
#     def inner(p,q,r):
#         print("hello")
        
#     return inner
# @decorator
# def even_no(start,stop,step):
#     for i in range(start,stop,step):
#         print(i)

# s,e,sd=2,101,2
# even_no(s,e,sd)



def outer_fun(x):
    def inner_fun(p,q):
        p=p+5
        q=q+10
        res1=x(p,q)
        return res1
    return inner_fun
@outer_fun
def add(s,t):
    return s+t

a=int(input("entre a numbmer"))
b=int(input("entre a numbmer"))
result=add(a,b)
print(result)

