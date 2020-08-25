class Employee:
    def __init__(self,eid,name,des,salary):
        self.eid=eid
        self.name=name
        self.salary=salary
        self.des=des
    def printValues(self):
        print(self.eid,self.name,self.salary)
    def __str__(self):
        return self.name

f=open("edetails","r")
emplst=[]
for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    desg=values[2]
    sal=values[3]
    obj=Employee(id,name,desg,sal)
    #print(obj)
    #obj.printValues()
    emplst.append(obj)
print(emplst.salary)
