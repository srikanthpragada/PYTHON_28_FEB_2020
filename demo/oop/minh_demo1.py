class A:
    def fun(self):
        print("A.fun()")


class B:
    def fun(self):
        print("B.fun()")


class C(A, B):
    def funny(self):
        print("C.fun()")


obj = C()
obj.fun()
