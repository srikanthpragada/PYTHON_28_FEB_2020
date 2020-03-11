# Immutable object

def zero(n):
    print(id(n))
    n = 0
    print(id(n))


v = 100
print(id(v))
zero(v)
print(v)


# Mutable object

def addleft(lst, v):
    lst.insert(0, v)


l = [1, 2, 3]
addleft(l, 10)
print(l)
