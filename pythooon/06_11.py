#...... generator   ...... yield .....

def data():
    for i in range(1,10):
        yield i
x=data()
# print(x)
# for i in x:
#     print(i)
print(next(x))
print(next(x))
print("hello")
print(next(x))
for i in x:
        print(i)


# l=[1,2,3,4,5,1,'pythion']
# l1=iter(l)
# print(l1)
# print(next(l1))




