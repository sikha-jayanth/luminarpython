f=open("employ")
emp={}
def fetchData(**kwargs):
    id=kwargs["id"]
    #prop=kwargs["prop"]


    if id not in emp:
        print("not exist")
    else:
        print(emp[id]["name"])
        if "prop" in kwargs:
            val=kwargs["prop"]
            print(emp[id][val])


for lines in f:
    id,name,desg,sal=lines.rstrip().split()
    emp[id]={"id":id,"name":name,"desg":desg,"sal":sal}

print(emp)

# fetchData(id="1001")
fetchData(id="1001",prop="desg")