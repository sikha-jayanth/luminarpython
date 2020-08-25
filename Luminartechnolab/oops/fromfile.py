class Employee:
    def __init__(self,eid,name,des,salary):
        self.eid=eid
        self.name=name
        self.des=des
        self.salary=int(salary)

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


# for emp in emplst:
#     print(emp.salary)



out=list(map(lambda obj:obj.name.upper(),emplst))
print(out)
out2=list(filter(lambda obj:obj.salary>10000,emplst))
for i in out2:
    print(i)
out3=list(map(lambda obj:obj.salary+5000,emplst))
#print(out3)
for i in out3:
    print(i)