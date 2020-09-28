f = open("complete.csv","r")

dict={}

for lines in f:
   lines = lines.rstrip().split(",")
   state = lines[1]
   tot_confd = lines[4]
   death = lines[5]
   recovrd = lines[9]

   if(state not in dict):
        dict[state] = {"confirmed": tot_confd, "recovered": recovrd, "death": death}
   else:
        dict[state] = {"confirmed": tot_confd, "recovered": recovrd, "death": death}

def Fetchdata(**kwargs):
    if(kwargs["state"] not in dict):
        print(" ")
    else:
        for k,v in dict.items():
            if(k==kwargs["state"]):
                print("Total confirmed cases : ",v["confirmed"])
                if("param" in kwargs):
                    val=kwargs["param"]
                    if(val=="recovered"):
                        print("Recoverd :",v["recovered"])
                    elif(val=="death"):
                        print("Death :",v["death"])

Fetchdata(state="kerala")
Fetchdata(state="Kerala",param="recovered")
Fetchdata(state="Kerala",param="death")