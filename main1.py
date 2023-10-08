string = ""
command = ""
exitcode = False
class question:
    def __init__(self, command) -> None:
        self.command = command
        self.question = ""
        self.question_number = 0
        self.optiona = ""
        self.optionb = ""
        self.optionc = ""
        self.optiond = ""
        self.position = 0
        self.position_end = 0
        global exitcode
    def findquestion(self):
   
        for i in range(len(command)):
            #print(command)
            #newcommand.find(str(i) + ".")
            #print(str(i) + ".")
            self.position = self.command.find(str(i) + ".")
            
            if self.position != -1:
                self.questionno = i
                #print("Position:"+str(i))
                return 0
            #print("Position:"+str(position))
        return -1
    def extractQ(self):
        #print(position)
        self.position_end = self.command.find("A.")
        #print("Position end:" + str(self.position_end))
        #print(posend)
        if self.position_end == -1:
            print("Error")
        else:
            self.question = self.command[self.position:self.position_end]
            #print(newcommand[position:posend])

    def extractoptions(self):
        #a
        temp = self.command.find("B.")
        self.optiona = self.command[self.position_end:temp]
        endd = self.command.find("C.")
        self.optionb = self.command[temp:endd]
        self.position_end = self.command.find("D.")
        self.optionc = self.command[endd:self.position_end]
        self.optiond = self.command[self.position_end:len(self.command)]

        #print(exitcode)
    def printall(self):
        print("Q:" + str(self.question))
        print("A: " + str(self.optiona))
        print("B: " + str(self.optionb))
        print("C: " + str(self.optionc))
        print("D: " + str(self.optiond))
        
    print("\n")
    def process(self):
        u = self.findquestion()
        if u == -1:
            return -1
        self.extractQ()
        self.extractoptions()
        self.printall()
        return 0
    
class questiondistributer:
    def __init__(self, command) -> None:
        self.foundlist = [0,0]
        self.command = command
        self.position = 0
        self.lastposition = 0
        self.question = ""
        self.position_end = 0
    def findnextquestion(self):
        for i in range(len(self.command)):
            self.position = self.command.find(str(i) + ".")
            if self.position != -1:
                self.foundlist.append(i)
                print("Found")
                for i in range(len(self.command)):
                    u = self.check(i)
                    if u == -1:
                        continue
                    self.position_end = self.command.find(str(i) + ".")
                    self.question = self.command[self.position:self.position_end]
                    self.lastposition = self.position
                    self.command = self.command[self.position_end:len(self.command)]
                    return 0
        return -1
    def check(self, u):
        inside = False
        for i in self.foundlist:
            if i == u:
                inside = True
        if inside:        
            return -1
        else:
            return 0
    def process(self):
        u = self.findnextquestion()
        if u == -1:
            print("completed")
            return -1
        """for i in range(5):
            u = self.findnextquestion()
            if u == -1:
                print("completed")
                return -1
            else:
                self.printall()"""
    def printall(self):
        print(self.question)

def __init__():
    global command
    command = input("Enter a string: ")
def __main__():
    __init__()
    """q = question(command)
    if q.process() == -1:
        print("Error")
    else:
        q.process()"""
    
    distributor = questiondistributer(command)
    distributor.process()
    questioner = question(command)
    questioner.process()
    #n = questiondistributer(command)
    #u = n.process()
    #if u == -1:
    #    print("Error")
__main__()
