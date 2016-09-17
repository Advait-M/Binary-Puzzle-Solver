from tkinter import*
root=Tk()
s = Frame(root,height=800, width=800)
s.grid()
buttonIDList = []
def submit():
    top = Toplevel()
    Button(top,text="Send", command= send).pack()

def updateButton(objID):
    num = objID.cget("text")
    if num == "0":
        newNum = "1"
    elif num == "1":
        newNum = " "
    else:
        newNum= "0"
    objID.config(text = newNum)
    BFrame.grid_propagate(False)

def makeButton(row,col):
    global BFrame
    if col %2==0:
        color = "red"
    else:
        color = "blue"
        
    BFrame = Frame(s,width=80,height=80, bg=color)
    BFrame.grid_propagate(False)
    BFrame.grid(row=row,column=col)
    buttonID = Button(BFrame,text=" ",font="Times 32",relief="groove", width = 3, height=1)
    buttonID.config(command= lambda:updateButton(buttonID))
    buttonIDList.append(buttonID)
    buttonID.grid()

def makeButtonMatrix():
    for row in range(8):
        for column in range(8):
            makeButton(row,column)

def send():
    count = 0
    bigList=[]
    tempList=[]
    print(len(buttonIDList))
    for i in buttonIDList:
        
        if count % 8==0 and count !=0:
            bigList.append(tempList)
            tempList = []
        tempList.append(i.cget("text"))
        count+=1
        print(count, tempList)
    bigList.append(tempList)
    print(count, bigList)
        
    
makeButtonMatrix()
submit()
