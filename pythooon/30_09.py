# d={'x':10,'y':20,'z':30}
# print(d.get('x'))
# print(d.get('xyz','guest '))

# d1=d.copy()
# print(d1,d)
# print(id(d),id(d1))
# d.clear()
# print(d)
# print(id(d))

# del d
# print(d)

# print(dir(int))

# print(dir(str))


# my_Set={'python',10,10,30,'java','php'}
# print(my_Set)

# print(len(my_Set))
# print(type(my_Set))
# print(id(my_Set))
# print(max(my_Set))
# print(min(my_Set))
# print(sum(my_Set))

s1={1,2,3,4,5}
s2={4,5,6,7,8}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
