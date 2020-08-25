class Employee:
    def __init__(self,eid,name,salary):
        self.eid=eid
        self.name=name
        self.salary=salary
    def printValues(self):
        print(self.eid,self.name,self.name)
    def __str__(self):
        return self.name

ls=[]
emp1=Employee(1001,"abin",25000)
#print(e)
emp2=Employee(1002,"reeta",240000)
emp3=Employee(1003,"ron",35000)
ls.append(emp1)
ls.append(emp2)
ls.append(emp3)
big=0
#print(ls)
for e in ls:
    if(e.salary>big):
        big=e.salary
        ename=e.name
print(ename)
