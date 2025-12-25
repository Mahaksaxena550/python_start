# 1)
# def showdetail(name):
#     print(name)
#     return "hello"
# Y=showdetail(10)
# print(Y)


# 2)
# def shoedetail(name):
#     print(name)
# shoedetail(20)


# 3)
# def showdetail():
#     name=20
#     print(name)
#     return "hello"
# Y=showdetail()
# print(Y)


# 4)
# def showdetail():
#     name=10
#     print(name)
# showdetail()



# ........ variable scope...

x,y=10,20
# def add():
#     print(x+y)
# add()

# def add():
#     p,q=10,20
#     print(x,y)
#     print(p,q)
# add()
# print(x,y)
# print(p,q)

def add():
    x=20
    global z
    z=20
    sum=globals()['x']+z
    print(sum)
add()
# print(x)
# print(z)
