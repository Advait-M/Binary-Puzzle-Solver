from tkinter import*
root=Tk()

m1 = PanedWindow(height=640, width=800)
m1.grid()

s = Frame(m1, bg="light grey")
m1.add(s)

controlPanel = Frame (m1)
m1.add(controlPanel)
x=[[' ', ' ', '0', ' ', ' ', ' ', ' ', '0'], [' ', ' ', ' ', ' ', ' ', '0', '0', ' '], ['1', ' ', '1', '1', ' ', '1', ' ', ' '], [' ', ' ', ' ', ' ', '0', ' ', ' ', ' '], [' ', '0', ' ', ' ', ' ', ' ', ' ', '0'], [' ', '1', ' ', ' ', ' ', '1', ' ', ' '], [' ', ' ', ' ', ' ', '0', ' ', ' ', ' '], ['1', ' ', '0', ' ', '0', ' ', ' ', '0']]


buttonIDList = []

Button(controlPanel,text="Export",font="Times 24" ,command= lambda:export()).pack()
Button(controlPanel,text="Import",font="Times 24" ,command= lambda:imp(x)).pack()

def imp(array):
    indent=0
    for row in range(len(array)):
        for i in range(len(array[row])):
            buttonIDList[indent].config(text=array[row][i])
            indent+=1
            

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

def main():
    for row in range(8):
        for column in range(8):
            makeButton(row,column)

def export():
    count = 0
    bigList=[]
    tempList=[]
##    print(len(buttonIDList))
    for i in buttonIDList:
        
        if count % 8==0 and count !=0:
            bigList.append(tempList)
            tempList = []
        tempList.append(i.cget("text"))
        count+=1
##        print(count, tempList)
    bigList.append(tempList)
    print(bigList)
    return bigList

if __name__ == "__main__":
    main()
        
    
