import random
from Algos import GetMaxCarIndex
from TrafficControlVar import NormalTrafficVar,CongestedTrafficVar
from turtle import Turtle, Screen
from OutputDemo3 import Base,Back,Pole,HeadText,Reset
from SlabTrafficControl import NormalTrafficS,CongestedTrafficS
from TrafficControl import NormalTrafficT,CongestedTrafficT
from Basic_Processing import main

#Assuming that 20 cars can cross the intersection in 40 seconds
'''
Average width of an intersction is 15m and average speed of a vehicle while crossing the intersection is 10km/h that is 
approximately 2.7 sec and takes approximately 6 sec to cross the intersection . Considdering the sides have 3 lanes thus 
thus providing 6 sec in totoal for the firdt row to cross with 2 sec of contribution by each car

'''
NormVal=10
'''
Intersection1=input("Vehicles on intersection 1 :")
Intersection2=input("Vehicles on intersection 2 :")
Intersection3=input("Vehicles on intersection 3 :")
Intersection4=input("Vehicles on intersection 4 :")
'''

'''
Intersection1=random.randrange(0,100)
Intersection2=random.randrange(0,100)
Intersection3=random.randrange(0,100)
Intersection4=random.randrange(0,100)
'''

List=main()
for i in range(0,4):
    List[i]=List[i]*random.randrange(1,4)
#List=[50,10,17,4]
MaxIndex=int(GetMaxCarIndex(List))

for i in range(0,4):
    print ("\tIntersection ",i+1," - ",List[i]," Cars")
print("\n")
#print ("Most cars in ",Index," Side")

screen=Screen()
screen.setup(1000,1000)

Base()
Pole()
Back()
HeadText()
'''
FOR TEXT OUTPUT ::

if List[MaxIndex]<=NormVal :
    #print ("Normal Flow of traffic ")
    NormalTraffic(List)
else :
    #print ("Congested flow of traffic ")
    CongestedTraffic(List)
'''

'''
FOR VARIANCE METHOD OUTPUT WITH GRAPHICS ::

if List[MaxIndex]<=NormVal :
    #print ("Normal Flow of traffic ")
    NormalTrafficG(List)
else :
    #print ("Congested flow of traffic ")
    CongestedTrafficG(List)
'''

'''
FOR SLAB METHOD WITH GRAPHICS ::
'''

if List[MaxIndex]<=NormVal :
    #print ("Normal Flow of traffic ")
    NormalTrafficS(List)
else :
    #print ("Congested flow of traffic ")
    CongestedTrafficS(List)



'''
SLABS
Normal       - 00-10  -->20 secs
Congestion_2 - 10-40  -->40 secs
Congestion_3 - 40-60  -->60 secs
60++ Cam limit 
'''
'''
if List[MaxIndex]<=NormVal :
    #print ("Normal Flow of traffic ")
    NormalTrafficVar(List)
else :
    #print ("Congested flow of traffic ")
    CongestedTrafficVar(List)'''
''''''
Reset()
screen.mainloop()

