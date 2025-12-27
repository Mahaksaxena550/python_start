# l={1,2,'python','java'}
# fs=frozenset(l)
# print(fs,type(fs))

# print(len(fs))

# print(max(fs))
# print(min(fs))
# print(sum(fs))
# print(type(fs))

# fs1=({10,20,30,'python'})
# fs2=({2,4,6,8,'java','python'})
# print(fs1.union(fs2))
# print(fs1.intersection(fs2))
# print(fs1.difference(fs2))
# print(fs1.symmetric_difference(fs2))

# print(fs1.isdisjoint(fs2))
# print(fs1.issuperset(fs2))
# print(fs1.issubset(fs2))

# x=True
# print(x)
# print(type(x))
# x=None
# print(x)
# print(type(x))
# x=range(10)
# print(x)
# print(type(x))

import sys
x=int()
y=sys.getsizeof(x)
print(y)

x=float()
y=sys.getsizeof(x)
print(y)

x=complex()
y=sys.getsizeof(x)
print(y)

x=str()
y=sys.getsizeof(x)
print(y)

x=list()
y=sys.getsizeof(x)
print(y)

x=tuple()
y=sys.getsizeof(x)
print(y)

x=set()
y=sys.getsizeof(x)
print(y)

x=frozenset()
y=sys.getsizeof(x)
print(y)

x=dict()
y=sys.getsizeof(x)
print(y)