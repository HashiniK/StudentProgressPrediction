passes=0
defers=0
fails=0
progression=''

def PassCredits():
    while True:
        try:
            global passes
            passes = int(input("Enter the number of credit amount of pass: "))     #try to get an integer value
            if passes < 0 or passes > 120 or passes %20 != 0:
                print("Incorrect Range!")
            else:
                break

        except ValueError:
            print("Please input a valid INTEGER!")


def DeferCredits():
    while True:
        try:
            global defers
            defers= int(input("Enter the number of credit amount of defer: "))
            if defers < 0 or defers > 120 or defers %20 != 0:
                print("Incorrect Range!")
            else:
                break

        except ValueError:
            print("Please input a valid INTEGER!")


def FailCredits():
    while True:
        try:
            global fails
            fails= int(input("Enter the number of credit amount of fails: "))
            if fails < 0 or fails > 120 or fails %20 != 0:
                print("Incorrect Range!")
            else:
                break

        except ValueError:
            print("Please input a valid INTEGER!")



def GettingTheInput():          #function to get the input
    while True:
        PassCredits()
        DeferCredits()
        FailCredits()                 
        while True:                 #loop for total
            if (passes+fails+defers)!= 120:
                print("Incorrect Total! Please enter the credits again \n")
                
            else:
                break
        break

#output
def GettingTheOutput():
    global progression
    if passes==120:                     #progress
        progression="Progress"
    elif passes == 100 :                        #Module trailer
        progression="Progress - Module Trailer"
    elif (passes <= 80)and (fails < 80):     #module retrieve
        progression="Do Not Progress - Module Retriever"
    elif (passes <= 40) and fails>=80:         #exclude
        progression="Exclude"
    print ("Your progression outcome is -  ",progression)
    print ("Amounts of credits for,","\n", "Passes-",passes,"\n", "Defers-",defers,"\n","Fails-",fails)



GettingTheInput()
GettingTheOutput()

