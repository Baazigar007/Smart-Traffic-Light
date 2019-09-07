
def GetMaxCarIndex(List):
    IndexVal=0
    Max=List[0]
    for i in range(1,4) :
        if(Max<List[i]):
            IndexVal=i
            Max=List[i]
    return IndexVal

def GetSMaxCarIndex(List):
    if(List[0]>List[1]):
        max=0
        secondmax=1
    else:
        max = 1
        secondmax = 0
    for i in range(2,4):
        if List[i] > List[max]:
            secondmax = max
            max = i
        else:
            if List[i] > List[secondmax]:
                secondmax = i
    return secondmax

def GetTMaxCarIndex(List):
    if (List[0] < List[1]):
        min = 0
        secondmin = 1
    else:
        min = 1
        secondmin = 0

    for i in range(2, 4):
        if List[i] < List[min]:
            secondmin = min
            min = i
        else:
            if List[i] <List[secondmin]:
                secondmin = i

    return secondmin

def GetMinCarIndex(List):
    IndexVal = 0
    Min = List[0]
    for i in range(1, 4):
        if (Min > List[i]):
            IndexVal = i
            Min = List[i]
    return IndexVal

def ExtendedGetMaxCarIndex(List):
    IndexVal=0
    Max=List[0][0]+List[0][1]+List[0][2]
    for i in range(1,4):
        if(Max<List[i][0]+List[i][1]+List[i][2]):
            IndexVal=i
            Max=List[i][0]+List[i][1]+List[i][2]
    return IndexVal

def Opposite(Val):
    return (Val+2)%4

def Left(Val):
    return (Val+1)%4

def Right(Val):
    return (Val+3)%4

def Sum(List):
    return List[0]+List[1]+List[2]

def MaxVal(List):
    Max=List[0]
    for i in range(1,3):
        if(List[i]>Max):
            Max=List[i]
    return Max

def Ones(List):
    count=0
    for i in range(0,4):
        if(List[i]==1):
            count=count+1
    return count

def Zeroes(List):
    count=0
    for i in range(0,4):
        if(List[i]==0):
            count=count+1
    return count

def NthZero(List):
    for i in range(0,4):
        if(List[i]==0):
            return i
    return 0


def Min(A,B):
    if(int(A)>int(B)):
        return B
    else:
        return A

def NonZero(List):
    for i in range(0,4):
        if(List[i]!=0):
            return i
    return 0

