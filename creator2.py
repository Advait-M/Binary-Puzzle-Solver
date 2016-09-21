# To understand recursion, see the bottom of this file 
import random
import BinarySolver as binsol
    
def createGrid(rows, columns):
    grid = []
    for m in range(0, rows):
        temp = [" "] * 8
        grid.append(temp)
    solvedGrid = grid[:]
    doAgain = False
    while not binsol.checkSolved(solvedGrid, rows, columns):
        doneAdd = False
        ins = 0
        done = True
        loop = False
        while not doneAdd:
            gridB = grid[:]
            newx = random.randint(0, columns-1)
            newy = random.randint(0, rows-1)
            if solvedGrid[newy][newx] == " ":
                gridB[newy][newx] = random.choice(["0", "1"])
                if binsol.checkValid(gridB, rows, columns):
                    solvedGridB = binsol.solve(gridB, rows, columns)
##                    print("asdasd")
##                    print(solvedGridB)
                    solvedGrid = solvedGridB
                    grid = gridB
                    doneAdd = True
            ins += 1
            if ins > rows*columns:
                loop = True
            if loop:
                break
##        print(grid)
##        print(solvedGrid)
##        print(binsol.checkSolved(solvedGrid, rows, columns))
        #print(solvedGrid)
        for m in solvedGrid:
            for n in m:
                if n == " ":
                    done = False
        if (done or loop) and not binsol.checkSolved(solvedGrid, rows, columns):
            doAgain = True
            break
    if doAgain:
        return createGrid(rows, columns)
    else:
        print(solvedGrid, "\n")
        return grid
def main(rows, columns):
    return createGrid(rows, columns)
if __name__ == "__main__":
    main(8, 8)

# To understand recursion, see the top of this file
