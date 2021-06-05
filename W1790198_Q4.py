countProgress=0
countTrailer=0
countRetriever=0
countExclude=0
mainCount=0

progression=0


marks=["120,00,00","100,20,00","100,20,00","80,20,20","60,40,20","40,40,40","20,40,60","20,20,80","20,00,100","00,00,120"]

def readMarks(marks):
    global mainCount,countProgress,countTrailer,countRetriever,countExclude,progression
    for i in range (1,len(marks)+1):
        items=marks[i-1]
        item=items.split(",")
        if int(item[0])==120:                     #progress
            progression="Progress"
            countProgress+=1
        elif int(item [0]) == 100 :                        #Module trailer
            progression="Progress - Module Trailer"
            countTrailer+=1
        elif (int(item[0]) <= 80)and (int(item[2]) <=60):     #module retrieve
            progression="Do Not Progress - Module Retriever"
            countRetriever+=1
        elif int(item[2])>=80:                        #exclude
            progression="Exclude"
            countExclude+=1
        print (item,"-",progression)
        mainCount+=1



def horizontalHistogram():
    print("")
    print ("-----HORIZONTAL HISTOGRAM-----")
    print ("Progress ",countProgress," :- ","*"*countProgress)
    print ("Trailer  ",countTrailer," :- ","*"*countTrailer)    
    print ("Retriever",countRetriever," :- ","*"*countRetriever)
    print ("Exclude  ",countExclude," :- ","*"*countExclude)
    print (mainCount,"outcomes in total")

def verticalHistogram():
    print("")
    print ("-----VERTICAL HISTOGRAM-----")
    global countProgress,countTrailer,countRetriever,countExclude
    print(f'{"Progress":4} {"Trailing":5} {"Retriever":6} {"Exclude":7}')
    while countProgress>0 or countTrailer>0 or countRetriever>0 or countExclude>0:
        if countProgress>0:
            print ("    *    ",end="")
            countProgress-=1
        else:
            print ("         ",end="")
            countProgress-=1
        if countTrailer>0:
            print ("    *    ",end="")
            countTrailer-=1
        else:
            print ("         ",end="")
            countTrailer-=1
        if countRetriever>0:
            print ("    *    ",end="")
            countRetriever-=1
        else:
            print ("         ",end="")
            countRetriever-=1
        if countExclude>0:
            print ("    *    ",end="")
            countExclude-=1
        else:
            print ("         ",end="")
            countExclude-=1
        print ("")
    print (mainCount,"outcomes in total")


def finalOutput():
    while True:
        readMarks(marks)
        horizontalHistogram()
        verticalHistogram()
        print("Program will exit now...")
        break

finalOutput()
