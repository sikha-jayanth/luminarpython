class Parent:
    def m1(self):
        print("inside parent")


class Child(Parent):
    def m2(self):
        print("inside child")


class Subchild(Child):
    def m3(self):
        print("inside subchild")

c=Child()
c.m2()
c.m1()
s=Subchild()
s.m3()
s.m2()
s.m1()