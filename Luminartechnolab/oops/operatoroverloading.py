class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return str(self.pages)
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __sub__(self, other):
        return Book(self.pages-other.pages)
obj=Book(100)
ob2=Book(200)
ob3=Book(300)
print(obj+ob2)
print(obj-ob2)
print(obj+ob2+ob3)
print(obj-ob2+ob3)