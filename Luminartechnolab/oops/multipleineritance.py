class Parent:
    def m1(self):
        print("inside parent")


class Child():
    def m2(self):
        print("inside child")


class Subchild(Child,Parent):
    def m3(self):
        print("inside subchild")

s=Subchild()
s.m3()
s.m2()
s.m1()