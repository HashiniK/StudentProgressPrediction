passes=0
defers=0
fails=0

countProgress=0
countTrailer=0
countRetriever=0
countExclude=0
mainCount=0

progression=0

def verticalHistogram():
    global countProgress,countTrailer,countRetriever,countExclude
    print("You have quit the program")
    print("")
    print ("-----VERTICAL HISTOGRAM-----")
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


       
def GettingTheInput():
    global passes,defers,fails
    while True:
        while True:
            try:
                passes=int(input("Enter the number of credits for passes: "))
                if(passes)>=0 and (passes)<=120 and (passes) % 20 == 0:
                    break
                else:
                    print("Range Error!!")
            except ValueError:
                print("Please input an INTEGER!")
        while True:
             try:
                 defers=int(input("Enter the number of credits for defers: "))
                 if(defers)>=0 and (defers)<=120 and (defers) % 20 == 0:
                     break
                 else:
                     print("Range Error!!")
             except ValueError:
                 print("Please input an INTEGER!")
        while True:
            try:
                fails=int(input("Enter the number of credits for fails : "))
                if(fails)>=0 and (fails)<=120 and (fails) % 20 == 0:
                    break
                else:
                    print("Range Error!!")
            except ValueError:
                print("Please input an INTEGER!")
        if passes+defers+fails==120:
            break
        else:
            print("Total incorrect")
                 

#output
def GettingTheOutput():
    global mainCount,countProgress,countTrailer,countRetriever,countExclude
    global progression
    if passes==120:                     #progress
        progression="Progress"
        countProgress+=1
    elif passes == 100 :                        #Module trailer
        progression="Progress - Module Trailer"
        countTrailer+=1
    elif (passes <= 80)and (fails <=60):     #module retrieve
        progression="Do Not Progress - Module Retriever"
        countRetriever+=1
    elif fails>=80:                        #exclude
        progression="Exclude"
        countExclude+=1
    print(progression)
    mainCount+=1


def programQuit():
    global endConfirmation
    endConfirmation = input ("Press 'q' to exit and see the histogram or 'Enter' to keep running: ")
    if endConfirmation == "q":
        verticalHistogram()
        print("Program will exit now...")
    elif endConfirmation == "":
        finalOutput()
    else:
        print ("Input Incorrect! Please try again!")
        programQuit()

    

def finalOutput():
        GettingTheInput()
        GettingTheOutput()
        programQuit()


            
finalOutput()
