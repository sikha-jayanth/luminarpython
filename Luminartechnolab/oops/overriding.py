class Parent:
    def phone(self):
        print("have samsung galaxy s6")
class Child(Parent):
    def phone(self):
        print("iphone")

c=Child()
c.phone()
