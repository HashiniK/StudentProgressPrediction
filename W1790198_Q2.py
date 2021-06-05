# Name           : Hashini Kodithuwakku
# Email          : hashini.2019750@iit.ac.lk
# StudentID      : 2019750
# WestministerID : W1790198

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

passes=0
defers=0
fails=0

countProgress=0
countTrailer=0
countRetriever=0
countExclude=0
mainCount=0

progression=0

def horizontalHistogram():
    print("You have quit the program")
    print ("Progress ",countProgress," :- ","*"*countProgress)
    print ("Trailer  ",countTrailer," :- ","*"*countTrailer)    
    print ("Retriever",countRetriever," :- ","*"*countRetriever)
    print ("Exclude  ",countExclude," :- ","*"*countExclude)
    print (mainCount,"outcomes in total")


       
def GettingTheInput():
    global passes,defers,fails
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
    if passes+defers+fails!=120:
        print("Total incorrect")
        GettingTheInput()

#output
def GettingTheOutput():
    global mainCount,countProgress,countTrailer,countRetriever,countExclude, progression
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
        horizontalHistogram()
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

