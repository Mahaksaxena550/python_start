# p=lambda x,y:x+y

# p(4,5)
# print(p)
# print(p(3,4))


# p=lambda x,y:print(x+y)

# p(4,5)
# print(p)
# print(p(3,4))


# p=lambda x,y: print(x+y)

# z=p(4,5)
# print(z)



# l=[1,2,3,4,5]
# print(list(map(lambda n:n*n,l)))

# l=[1,2,3,4]
# l1=[1,2,3,4]
# l2=[2,4,5,6]
# print(list(map(lambda x,y,z:x+y+z,l,l1,l2)))

l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda n:n if n%2==0 else None,l)))
# print(list(map(lambda n:'even' if n%2==0 else 'odd',l)))

import functools
print(functools.reduce(lambda x,y:x+y,l))
print(functools.reduce(lambda x,y: x if x>y else y,l))
print(functools.reduce(lambda x,y: x if x<y else y,l))