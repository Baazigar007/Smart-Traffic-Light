from Colors import bcolors
import time
from Algos import GetMaxCarIndex
from Calci import Interval

def NormalTrafficT(List):
    Gtime=30
    for i in range(0,4):
        if(List[i]>0):
            print (bcolors.OKGREEN,"GREEN LIGHT FOR SIDE (",List[i]," Cars) : ",i+1,bcolors.ENDC )
        time.sleep(Gtime/10)

#NormalTraffic([0,32,12,32])

def CongestedTrafficT(List):
    Gtime=30
    #MinIndex=GetMinCarIndex(List)
    for i in range(0,4):
        if(List[i]<10) and (List[i]>0):
            Gtime=int(List[i]*3/2)
            print(bcolors.OKGREEN, "GREEN LIGHT FOR SIDE (", List[i], " Cars) :SIDE: ", i + 1, ":CARS:",List[i], ":TIME:", Gtime, bcolors.ENDC)
            time.sleep(Gtime/10)
            List[i]=0
    MaxIndex=GetMaxCarIndex(List)
    while(List[MaxIndex]>0):
        Gtime=Interval(List)
        PassableCars=min(List[MaxIndex],round((Gtime*2)/3))
        #Green(MaxIndex,Gtime,PassableCars)
        print(bcolors.OKGREEN,"GREEN LIGHT FOR SIDE (",List[MaxIndex]," Cars) :SIDE: ",MaxIndex+1 ,":CARS:",PassableCars,":TIME:",Gtime,bcolors.ENDC )
        List[MaxIndex]=List[MaxIndex]-PassableCars
        time.sleep(Gtime/10)
        MaxIndex=GetMaxCarIndex(List)
