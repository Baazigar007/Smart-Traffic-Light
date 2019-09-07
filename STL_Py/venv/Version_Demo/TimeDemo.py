import timeit

start = timeit.timeit()
end = timeit.timeit()
while round((start-end)*10,3)<0.2:
    if (start-end)<1:
        print("1")
    else:
        print ("2")
    end = timeit.timeit()
#def  NormalLights(List):
