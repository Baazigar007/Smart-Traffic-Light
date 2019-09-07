from Colors import bcolors
import time
from Algos import GetMaxCarIndex,Ones,NthZero,GetSMaxCarIndex,GetTMaxCarIndex,GetMinCarIndex,Zeroes,NonZero
from Calci import Interval
from turtle import Turtle,Screen
from OutputDemo3 import Base,Back,Pole,Red,Yellow,Green,HeadText,Reset

def NormalTrafficVar(List):
    for i in range(0,4):
        Gtime = 20
        if (List[i] > 0):
            Green(i + 1, List[i], List[i], Gtime)
            for j in range(0, 4):
                if (j == i):
                    continue
                else:
                    Red(j + 1)
        time.sleep(Gtime / 10)
        Yellow(i + 1)
        time.sleep(2)
        Red(i+1)

def CongestedTrafficVar(List):
    CheckList = [0, 0, 0, 0]
    LowCount = 0

    for i in range(0, 4):
        if (List[i] <= 4) and (List[i] > 0):
            Gtime = 10
            Green(i + 1, List[i], List[i], Gtime)
            CheckList[i] = 1
            LowCount = LowCount + 1
            for j in range(0, 4):
                if (j == i):
                    continue
                else:
                    Red(j + 1)
            time.sleep(Gtime / 10)
            Yellow(i + 1)
            time.sleep(2)
            Red(i + 1)
            List[i] = 0

    MaxIndex = GetMaxCarIndex(List)
    while (List[MaxIndex] > 0):
        # Just one intersection left
        if (Zeroes(List) == 3):
            Req = NonZero(List)
            Gtime = List[Req] * 2
            PassableCars = List[Req]
            Green(Req + 1, List[Req], PassableCars, Gtime)
            for j in range(0, 4):
                if (j == Req):
                    continue
                else:
                    Red(j + 1)
            time.sleep(Gtime / 10)
            Yellow(Req + 1)
            time.sleep(2)
            List[Req] = 0
            CheckList[Req] = 1
            break

        if (Ones(CheckList) == 3):
            Req = NthZero(CheckList)
            Gtime = min(Interval(List[Req]), List[Req] * 2)
            if (Gtime == 0):
                Gtime = 10
            PassableCars = int(Gtime / 2)
            Green(Req + 1, List[Req], PassableCars, Gtime)
            for j in range(0, 4):
                if (j == Req):
                    continue
                else:
                    Red(j + 1)
            time.sleep(Gtime / 10)
            Yellow(Req + 1)
            time.sleep(2)
            List[Req] = List[Req] - PassableCars
            for i in range(0, 4):
                if (i == Req):
                    CheckList[i] = 1
                else:
                    CheckList[i] = 0

        if(CheckList[MaxIndex]==1):
            MaxIndex=GetSMaxCarIndex(List)
        if(CheckList[MaxIndex]==1):
            MaxIndex=GetTMaxCarIndex(List)

        Gtime = min(Interval(List),List[MaxIndex]*2)
        PassableCars = min(List[MaxIndex], int(Gtime / 2))
        Green(MaxIndex + 1, List[MaxIndex], PassableCars, Gtime)
        CheckList[MaxIndex] = 1
        for j in range(0, 4):
            if (j == MaxIndex):
                continue
            else:
                Red(j + 1)
        time.sleep(Gtime / 10)
        Yellow(MaxIndex + 1)
        time.sleep(2)
        List[MaxIndex] = List[MaxIndex] - PassableCars
        MaxIndex = GetMaxCarIndex(List)

    time.sleep(1)
