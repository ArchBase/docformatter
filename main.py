
"""Open Source Project , Author :Akshay A archbase557@gmail.com

released:as-is code snippet"""


command = ""
newcommand = ""
questionno = 0
position = 0
question = ""
endd = 0
posend = 50

optiona = ""
optionb = ""
optionc = ""
optiond = ""
print("WARNING:BY USING THIS SOFTWARE YOU AGREE TO THE TERMS AND CONDITIONS FOR THIS PROGRAM\n\n\n")
def update():
    global newcommand,position,endd,questionno,posend,command
    #position=0
    #endd=0
    #posend=len(command)
    newcommand = command[posend+1:len(command)]

def printall():
    global question,optiona,optionb,optionc,optiond,newcommand,questionno
    print("Q:" + str(question))
    print("A: " + str(optiona))
    print("B: " + str(optionb))
    print("C: " + str(optionc))
    print("D: " + str(optiond))
    
    print("\n")

def extractoptions():
    #a
    global optiona,optionb,optionc,optiond,endd,questionno,posend,command
    temp = newcommand.find("B.")
    optiona = newcommand[endd:temp]
    endd = newcommand.find("C.")
    optionb = newcommand[temp:endd]
    temp = newcommand.find("D.")
    optionc = newcommand[endd:temp]

    position = 0
    for i in range(len(command)):
        if i > questionno:
            position = newcommand.find(str(i) + ".")
            print(position)
            if position != -1:
                optiond = newcommand[temp:position-1]
                posend = position-1
                break
def findquestion():
    print("New: " + str(newcommand))
    global questionno,command,position
    for i in range(len(command)):
        #newcommand.find(str(i) + ".")
        #print(str(i) + ".")
        position = newcommand.find(str(i) + ".")
        questionno = i
        if position != -1:
            #print("Position:"+str(position))
            return 0
        #print("Position:"+str(position))
    return -1

def extractQ():
    global endd,position,question
    #print(position)
    posend = newcommand.find("A.")
    endd = posend
    #print(posend)
    if posend == -1:
        print("Error")
    else:
        question = newcommand[position:posend]
        #print(newcommand[position:posend])
command = input("enter a string:")
newcommand = command
posend = len(command)
while True:
    u = findquestion()
    if u == -1:
        print("Question out of stack")
        break
    extractQ()
    #print(question)
    extractoptions()
    
    printall()
    update()