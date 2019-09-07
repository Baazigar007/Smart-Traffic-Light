import random
from Algos import ExtendedGetMaxCarIndex
from turtle import Turtle, Screen
from ExtendedOutputDemo import Base,Back,Pole,HeadText,Reset
from ExtendedIntersectionControl import ExtendedNormalTraffic , ExtendedCongestionTraffic

NormVal=18

Intersection1L = random.randrange(0,30)
Intersection1M = random.randrange(0,30)
Intersection1R = random.randrange(0,30)
Intersection2L = random.randrange(0,30)
Intersection2M = random.randrange(0,30)
Intersection2R = random.randrange(0,30)
Intersection3L = random.randrange(0,30)
Intersection3M = random.randrange(0,30)
Intersection3R = random.randrange(0,30)
Intersection4L = random.randrange(0,30)
Intersection4M = random.randrange(0,30)
Intersection4R = random.randrange(0,30)

List=[[Intersection1L,Intersection1M,Intersection1R],
      [Intersection2L,Intersection2M,Intersection2R],
      [Intersection3L,Intersection3M,Intersection3R],
      [Intersection4L,Intersection4M,Intersection4R]]


for i in range (0,4):
        print("Intersection ",i+1,"-",List[i][0],",",List[i][1],",",List[i][2])

MaxIndex = ExtendedGetMaxCarIndex(List)

screen=Screen()
screen.setup(1000,1000)
Base()
Pole()
Back()
HeadText()

if List[MaxIndex]<=NormVal :
    #print ("Normal Flow of traffic ")
    ExtendedNormalTraffic(List)
else :
    #print ("Congested flow of traffic ")
    ExtendedCongestionTraffic(List)

Reset()
screen.mainloop()


