employee={"eid":1000,"ename":"abc","desg":"place","salary":15000}
print(employee["ename"])
if "company" in employee:
    print("key already exists")
else:
    employee["company"]="luminar"
employee["salary"]+=5000
for key in employee:
    print(key,":",employee[key])