f=open("complete.csv","r")
st={}
dict={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    state=data[1]
    total=data[4]
    death=data[5]
    recover=data[6]
    if state not in st:
        st[state]={"state":state,"total":total,"death":death,"recover":recover}
def fetchData(**kwargs):
    state=kwargs["state"]
    dict={}
    re={}
    de={}
    totalconfirm=0
    totalrecovered=0
    totaldeath=0
    par=kwargs["param"]
    if state not in st:
        print("Doesnot exist")
    else:
        if state not in dict:
            dict[state] = total
        else:
            dict[state] = total
        for k, v in dict.items():
            totalconfirm = totalconfirm + int(v)
        print("Total confirmed Cases in ",state,"is",totalconfirm)
        if "param" in kwargs:
            if par=="recovered":
                if state in re:
                    re[state]=recover
                else:
                    re[state]=recover
                for k, v in re.items():
                    totalrecovered = totalrecovered + int(v)

                print("total recovered Cases:",totalrecovered)
            if par=="death":
                if state in de:
                    de[state]=death
                else:
                    de[state]=death
                for k, v in de.items():
                    totaldeath = totaldeath + int(v)
                print("Total Death in",state,"is",totaldeath)

fetchData(state="Kerala",param="death")