import math

def Mean(List):
    Sum=0
    for i in range(0,4):
        Sum=Sum+List[i]
    return Sum/4

def Variance(List):
    Sum=0
    MeanVal=Mean(List)
    for i in range(0,4):
        Sum=Sum+pow(List[i]-MeanVal,2)
    return Sum/4

def STDev(List):
    return math.sqrt(Variance(List))

def Interval(List):
    VarianceVal=Variance(List)
    if VarianceVal<200:
        return 40
    elif VarianceVal<400:
        return 50
    elif VarianceVal<900:
        return 60

'''
SLABS
Normal       - 00-10  -->30
Congestion_2 - 30-50  -->40
Congestion_3 - 50-70  -->50
Congestion_4 - 70-100 -->60

'''

def IntervalSlab(Val):
    if(Val>0 and Val<=10):
        return 20
    elif(Val>10 and Val<=40):
        return 40
    else:
        return 60
