def math_op(op, n1, n2):
    return op(n1, n2)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


add2 = add
print(add(10, 20), add2(10, 20))

print(math_op(add, 10, 20))
print(math_op(mul, 10, 20))
