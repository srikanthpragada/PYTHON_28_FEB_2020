def fun1(*, a, b):    # Keyword only args
    pass

def fun2(a, b, /):    # Positional only args
    pass


fun1(a=10, b=20)
# fun1(10, 20)
fun2(10,20)
fun2(a = 10,b = 20)
