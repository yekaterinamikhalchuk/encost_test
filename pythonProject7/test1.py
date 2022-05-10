class A:
    def hi(self):
        print("A")


class B(A):
    def hi(self):
        super().hi()
        print("B")


class C(A):
    def hi(self):
        super().hi()
        print("C")

class M(A):
    def hi(self):
        super().hi()
        print("M")


class D(M, B,C):
    def hi(self):
        super().hi()


d = D()
d.hi()
print(D.mro())
