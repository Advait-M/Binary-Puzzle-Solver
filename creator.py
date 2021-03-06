import random
import copy
possibleRows = [['1', '1', '0', '1', '0', '1', '0', '0'], ['1', '0', '1', '1', '0', '1', '0', '0'], ['1', '1', '0', '0', '1', '1', '0', '0'], ['1', '0', '1', '0', '1', '1', '0', '0'], ['0', '1', '1', '0', '1', '1', '0', '0'], ['1', '1', '0', '1', '0', '0', '1', '0'], ['1', '0', '1', '1', '0', '0', '1', '0'], ['1', '1', '0', '0', '1', '0', '1', '0'], ['1', '0', '1', '0', '1', '0', '1', '0'], ['0', '1', '1', '0', '1', '0', '1', '0'], ['1', '0', '0', '1', '1', '0', '1', '0'], ['0', '1', '0', '1', '1', '0', '1', '0'], ['1', '0', '1', '0', '0', '1', '1', '0'], ['0', '1', '1', '0', '0', '1', '1', '0'], ['1', '0', '0', '1', '0', '1', '1', '0'], ['0', '1', '0', '1', '0', '1', '1', '0'], ['0', '0', '1', '1', '0', '1', '1', '0'], ['1', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '1', '0', '1', '0', '0', '1'], ['0', '1', '1', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '1', '0', '0', '1'], ['0', '1', '0', '1', '1', '0', '0', '1'], ['1', '0', '1', '0', '0', '1', '0', '1'], ['0', '1', '1', '0', '0', '1', '0', '1'], ['1', '0', '0', '1', '0', '1', '0', '1'], ['0', '1', '0', '1', '0', '1', '0', '1'], ['0', '0', '1', '1', '0', '1', '0', '1'], ['0', '1', '0', '0', '1', '1', '0', '1'], ['0', '0', '1', '0', '1', '1', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '1'], ['0', '1', '0', '1', '0', '0', '1', '1'], ['0', '0', '1', '1', '0', '0', '1', '1'], ['0', '1', '0', '0', '1', '0', '1', '1'], ['0', '0', '1', '0', '1', '0', '1', '1']]
def onlyOne(grid, allRows, aColumns, booleanGrid):
    for m in booleanGrid:
        for n in m:
            if not n:
                return False
    return True
##    for i in range(0, len(allRows)):
##        if len(allRows[i]) != 1:
##            return False
##    return True
def checkValid(grid, complete):
    if complete:
        for m in range(0, rows):
            total0s = 0
            total1s = 0
            for n in range(0, columns):
                if grid[m][n] == "0":
                    total0s += 1
                elif grid[m][n] == "1":
                    total1s += 1
            if not total0s == total1s == 4:
                return False
        for y in range(0, rows):
            for x in range(0, columns):
                try: 
                    if grid[y][x] == grid[y+1][x] == grid[y+2][x]:
                        return False
                except IndexError:
                    pass
                try:
                    if grid[y][x] == grid[y][x+1] == grid[y][x+2]:
                        return False
                except IndexError:
                    pass
        if len(grid) != len([list(t) for t in set(tuple(element) for element in grid)]):
            return False
        curGrid = list(zip(*grid))
        for y in range(0, rows):
            curGrid[y] = list(curGrid[y])
        if len(curGrid) != len([list(t) for t in set(tuple(element) for element in curGrid)]):
            return False
        return True
    else:
        for m in range(0, rows):
            total0s = 0
            total1s = 0
            for n in range(0, columns):
                if grid[m][n] == "0":
                    total0s += 1
                elif grid[m][n] == "1":
                    total1s += 1
            if total0s > 4:
                return False
            if total1s > 4:
                return False
        for y in range(0, rows):
            for x in range(0, columns):
                try: 
                    if grid[y][x] == grid[y+1][x] == grid[y+2][x]:
                        if grid[y][x] != " ":
                            return False
                except IndexError:
                    pass
                try:
                    if grid[y][x] == grid[y][x+1] == grid[y][x+2]:
                        if grid[y][x] != " ":
                            return False
                except IndexError:
                    pass
        return True
def checkEmpty(grid, x, y):
    if grid[y][x] == " ":
        return True
    return False
def delete(allRows, toDel):
##    print("NEXT")
##    print(allRows)
##    print(toDel)
    for n in toDel:
##        print(n[0], n[1])
        del allRows[n[0]][n[1]]
        for i in allRows:
            print(len(i))
    return allRows
def createPuzzle(possibleRows, rows, columns):
    grid = []
    for m in range(0, rows):
        temp = [" "] * 8
        grid.append(temp)
##    aRows = []
    aRows = [possibleRows[:] for i in range(0, rows)]
    aColumns = [possibleRows[:] for i in range(0, columns)]
    booleanGrid = [[False for m in range(0, rows)] for n in range(0, columns)]
    print(booleanGrid)
##    for i in range(0, rows):
##        aRows.append(possibleRows)
    print("INIT")
    print(grid)
    print()
    print(aRows)
    print()
    print(aColumns)
    while not onlyOne(grid, aRows, aColumns, booleanGrid):
        doneAdd = False
        for i in range(0, len(aRows)):
            if len(aRows[i]) == 1:
                for j in range(0, rows):
                    booleanGrid[i][j] = True
        print("before")
        print(booleanGrid)
        temp = list(zip(*booleanGrid))
        for y in range(0, rows):
            temp[y] = list(temp[y])
        for i in range(0, len(aColumns)):
            if len(aColumns[i]) == 1:
                for j in range(0, columns):
                    temp[i][j] = True
        temp = list(zip(*temp))
        for y in range(0, rows):
            temp[y] = list(temp[y])
        booleanGrid = temp
        print(booleanGrid)
        while not doneAdd:
            gridB = copy.deepcopy(grid)
            aRowsB = copy.deepcopy(aRows)
            aColumnsB = copy.deepcopy(aColumns)
            newx = random.randint(0, columns-1)
            newy = random.randint(0, rows-1)
            while not checkEmpty(gridB, newx, newy):
                newx = random.randint(0, columns-1)
                newy = random.randint(0, rows-1)
            value = random.choice(["0", "1"])
            gridB[newy][newx] = value
            if checkValid(gridB, False):
##                for i in aRowsB:
##                    print(len(i))
                toDel = []
##                print(aRowsB)
##                print("asdasdsad")
                for i in range(len(aRowsB[newy])-1, -1, -1):
                    if aRowsB[newy][i][newx] != value:
                        del aRowsB[newy][i]
                for i in range(len(aColumnsB[newx])-1, -1, -1):
##                    print(aColumnsB[newx])
                    if aColumnsB[newx][i][newy] != value:
##                        print(newx, i, newy)
                        del aColumnsB[newx][i]
##                newARows = []
##                for q in range(0, len(aRowsB)):
##                    tmp = []
##                    for w in range(0, len(aRowsB[q])):
##                        if [q, w] not in toDel:
##                            tmp.append(aRowsB[q][w])
##                    newARows.append(tmp)
####                aRowsB = delete(aRowsB, toDel)
                notValid = False
                for i in aRowsB:
                    if len(i) == 0:
                        notValid = True
                if notValid:
                    break
##                print(toDel)
##                for n in toDel:
##                    print(n[0], n[1])
##                    del aRowsB[n[0]][n[1]]
##                    for i in aRowsB:
##                        print(len(i))
##                for i in newARows:
##                    print(len(i))
                grid = copy.deepcopy(gridB)
                aRows = copy.deepcopy(aRowsB)
                aColumns = copy.deepcopy(aColumnsB)
                doneAdd = True
##        print()
##        print(grid)
##        print("arows")
##        print("START")
##        print(grid)
##        print()
##        print(aRows)
##        print()
##        print(aColumns)
    print("final")
    print(grid)
    print()
    print(aRows)
    print()
    print(aColumns)
            
rows = 8
columns = 8
createPuzzle(possibleRows, rows, columns)
