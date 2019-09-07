'''
SLABS
Normal       - 00-10  -->20 secs
Congestion_2 - 10-40  -->40 secs
Congestion_3 - 40-60  -->60 secs
'''

from Colors import bcolors
import time
from Algos import GetMaxCarIndex,Ones,NthZero,GetSMaxCarIndex,GetTMaxCarIndex,GetMinCarIndex,Zeroes,NonZero
from turtle import Turtle,Screen
from OutputDemo3 import Base,Back,Pole,Red,Yellow,Green,HeadText,Reset
from Calci import IntervalSlab

def NormalTrafficS(List):
    #Normal Slab
    for i in range(0, 4):
        Gtime=20
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

def CongestedTrafficS(List):
    CheckList = [0, 0, 0, 0]
    LowCount = 0

    #Corner Case
    for i in range(0, 4):
        if (List[i] <= 3) and (List[i] > 0):
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
            Gtime = max(List[Req]*2,10)
            PassableCars = min(List[Req],int(Gtime/2))
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
        #Just one side left and others have checklist true
        if (Ones(CheckList) == 3):
            Req = NthZero(CheckList)
            Gtime = min(IntervalSlab(List[Req]),List[Req]*2)
            if (Gtime == 0):
                Gtime = 10
            PassableCars = int(Gtime/2)
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

        #Check for Cycle
        if (CheckList[MaxIndex] == 1):
            MaxIndex = GetSMaxCarIndex(List)
        if (CheckList[MaxIndex] == 1):
            MaxIndex = GetTMaxCarIndex(List)

        #Normal Body
        Gtime = min(IntervalSlab(List[MaxIndex]), List[MaxIndex] * 2)
        Gtime=max(10,Gtime)
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

