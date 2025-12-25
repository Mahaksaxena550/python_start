# d={'name':'neeraj','age':'37','quali':'M.tach'}

# print(len(d))

# print(max(d))

# print(min(d))

# e={1:20,2:30,3:40}

# print(sum(e))

# print(type(d))

# print(id(d))

# l=['x','y','z',1,2,3]

# d1=dict.fromkeys(l,50)
# print(d1)
# print(type(d1))

# d1={'x':10,'y':20,'z':30}
# d2={'p':10,'q':20,'x':30}
# d1.update(d2)
# print(d1)


d1={'x':10,'y':20,'z':30}
d=d1.setdefault('x',100)
print(d)

d=d1.setdefault('name','neeraj')
print(d)