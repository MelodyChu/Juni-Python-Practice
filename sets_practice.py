x = set()
x.add(1)
x.remove(1)
x.add(2)
x.add(2)
print(x)

y = [1,1,1,3,3,5]
y = set(y)
print(y)


print(x.union(y))
print(x.intersection(y))
