g = "Global"


def f1():
    # global g
    g = "A new value"
    e = "enclose"
    count = 0
    print("In f1()")

    def f2():
        nonlocal count
        count = count + 1
        l = "local"
        print("In f2()")
        print(l, e, g, True)

    f2()  # call local function


print(g)
f1()
print(g)

