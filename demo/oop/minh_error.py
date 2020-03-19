class A:
    def fun(self):
        print("A.fun()")

class B(A):

    def fun(self):
        print("B.fun()")


class C(A, B):
    def fun(self):
        print("C.fun()")


print(C.mro())
# obj = C()
# obj.fun()
