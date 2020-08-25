class Parent:
    def m1(self):
        print("inside parent")


class Child():
    def m1(self):
        print("inside child")


class Subchild(Child,Parent): #execute m1 in child
    def m3(self):
        print("inside subchild")

s=Subchild()
s.m3()
#s.m2()
s.m1()