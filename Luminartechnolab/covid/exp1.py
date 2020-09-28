f=open("covid_19_india.csv",encoding='utf-8-sig')
covid={}
def fetchdata(**kwargs):



for lines in f:
    sno,date,time,state,ConfirmedIndianNational,ConfirmedForeignNational,cured,deaths,confirmed=lines.rstrip("\n").split(",")
    #print(state)

    covid[sno]={"state":state,"confirmednational":ConfirmedIndianNational,"confirmedforeign":ConfirmedForeignNational,"cured":cured,"deaths":deaths,"confirmed":confirmed}

for k,v in covid.items():
    print(k,v)
    break
fetchData(state="Kerala")