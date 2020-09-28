f=open("complete.csv")
dict={}
def fetchData(**kwargs):
    state=kwargs["state"]
    if state not in dict:
        print("not found")
    else:
        print("total confirmed cases in",state,":",dict[state]["confirmed"])
        if "param" in kwargs:
            val=kwargs["param"]
            print("total",val,dict[state][val])



for lines in f:
    data=lines.rstrip("\n").split(",")
    date,state,confirmed,recovered,death=data[0],data[1],int(data[4]),int(data[6]),int(data[5])

    if state not in dict:
        dict[state] = {"confirmed":confirmed,"recovered": recovered, "death": death}
    else:
        dict[state]['confirmed']+=confirmed
        dict[state]['recovered']+=recovered
        dict[state]['death']+=death


# for k,v in dict.items():
#     print(k,v)
# # print(dict)


fetchData(state="Odisha")
fetchData(state="Odisha",param="recovered")
fetchData(state="Odisha",param="death")