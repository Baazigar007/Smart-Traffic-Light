from Colors import bcolors

def Green (Num,Time,Cars):
    print(bcolors.OKGREEN,"\tSIDE ",Num," : ",Time," secs ( ",Cars," Cars)",bcolors.ENDC)

def Yellow(Num):
    print(bcolors.HEADER, "\tSIDE ", Num, " : 5 secs", bcolors.ENDC)

def Red(Num):
    print(bcolors.FAIl, "\tSIDE ", Num, bcolors.ENDC)