'''
Every Side of the intersection has 3 possible routes either left or straight or right where the left will be always green

                █|   |   |   |██|   |   |   |█
                █|   |   |   |██|   |   |   |█
                █|   |   |   |██|   |   |   |█
                █|   |   |   |██|   |   |   |█
                █|   |   |   |██|   |   |   |█
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█|   |   |   |██|   |   |   |█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

----------------                             ----------------

----------------                             ----------------

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

----------------                             ----------------

----------------                             ----------------

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                █|   |   |   |██|   |   |   |█
                █|   |   |   |██|   |   |   |█
                █|   |   |   |██|   |   |   |█
                █|   |   |   |██|   |   |   |█
                █|   |   |   |██|   |   |   |█
                █|   |   |   |██|   |   |   |█


Majority of the traffic is going straight with few cars left or right
majority traffic is for straight and less than half or at max half for right
Values are stored in 2D array
Har side ka array hai with 3 values
0 for left 1 for straight 2 for right
'''

from turtle import Turtle,Screen
import time
from Algos import ExtendedGetMaxCarIndex,Right,Opposite,Left,MaxVal,Sum
from ExtendedOutputDemo import GreenL,GreenM,GreenR,Yellow,Red,Base,Pole,Back,HeadText,Reset,RightOff


def ExtendedNormalTraffic(List):
    while(Sum(List[ExtendedGetMaxCarIndex(List)])>0):
        for i in range(0,4):
            Gtime=MaxVal(List[i])*2

            if(Sum(List[i])>0):
                GreenL(i+1,List[i][0],List[i][0],Gtime)
                List[i][0]=0
                GreenL(Right(i)+1,List[Right(i)][0],min(List[Right(i)][0],Gtime/2),Gtime)
                List[Right(i)][0]=List[Right(i)][0]-min(List[Right(i)][0],Gtime/2)
                GreenL(Opposite(i)+1,List[Opposite(i)][0],min(List[Opposite(i)][0],Gtime/2),Gtime)
                List[Opposite(i)][0] = List[Opposite(i)][0] -min(List[Right(i)][0],Gtime/2)
                MidInitial=List[i][1]

                if(List[i][1]>0):
                    GreenM(i+1,List[i][1],List[i][1],Gtime)
                    List[i][1]=0
                    Red(Left(i)+1)
                elif(List[i][1]==0):
                    GreenL(Left(i)+1,List[Left(i)][0],min(List[Left(i)][0],Gtime/2),Gtime)
                    List[Left(i)][0]=List[Left(i)][0]-min(List[Left(i)][0],Gtime/2)

                RightInitial=List[i][2]
                if(List[i][2]>0):
                    GreenR(i+1,List[i][2],List[i][2],List[i][2]*2)
                    List[i][2]=0
                    TimeLeft=Gtime-RightInitial*2
                    time.sleep(RightInitial*2)
                    RightOff(i+1)
                    if(TimeLeft>0):
                        GreenM(Opposite(i)+1,List[Opposite(i)][1],int(min(List[Opposite(i)][1],TimeLeft/2)),TimeLeft)
                        List[Opposite(i)][1]=List[Opposite(i)][1]-int(min(List[Opposite(i)][1],TimeLeft/2))
                        time.sleep(TimeLeft*2)
                elif(RightInitial==0):
                    GreenM(Opposite(i)+1, List[Opposite(i)][1], int(min(List[Opposite(i)][1], Gtime /2)), Gtime)
                    List[Opposite(i)][1] = List[Opposite(i)][1] - int(min(List[Opposite(i)][1], Gtime / 2))
                    time.sleep(Gtime*2)

                Yellow(i+1)
                Yellow(Right(i)+1)
                if(MidInitial==0):
                    Yellow(Left(i)+1)
                Yellow(Opposite(i)+1)
                time.sleep(2)

                Red(i+1)
                Red(Right(i)+1)
                if (MidInitial == 0):
                    Red(Left(i)+1)
                Red(Opposite(i)+1)


#def ExtendedCongestionTraffic(List):



screen=Screen()
screen.setup(1000,1000)
Base()
Pole()
Back()
HeadText()
ExtendedNormalTraffic([[6,6,3],[3,5,2],[2,6,3],[3,3,3]])

Reset()
screen.mainloop()

