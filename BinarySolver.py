def switch(x):
    return {
        "0": "1",
        "1": "0",
    }[x]
def checkValid(grid, rows, columns):
    for m in range(0, rows):
        total0s = 0
        total1s = 0
        for n in range(0, columns):
            if grid[m][n] == "0":
                total0s += 1
            elif grid[m][n] == "1":
                total1s += 1
        if total0s > 4 or total1s > 4:
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
    if len(grid) != len([list(t) for t in set(tuple(element) for element in grid)]):
        return False
    curGrid = list(zip(*grid))
    for y in range(0, rows):
        curGrid[y] = list(curGrid[y])
    if len(curGrid) != len([list(t) for t in set(tuple(element) for element in curGrid)]):
        return False
    for m in range(0, columns):
        total0s = 0
        total1s = 0
        for n in range(0, rows):
            if grid[m][n] == "0":
                total0s += 1
            elif grid[m][n] == "1":
                total1s += 1
        if total0s > 4 or total1s > 4:
            return False
    return True
    
def checkSolved(grid, rows, columns, complete = True):
    for m in range(0, rows):
        total0s = 0
        total1s = 0
        for n in range(0, columns):
            if grid[m][n] == "0":
                total0s += 1
            elif grid[m][n] == "1":
                total1s += 1
        if complete:
            if not total0s == total1s == 4:
                return False
        if not complete:
            if total0s > 4:
                return False
            if total1s > 4:
                return False
    for y in range(0, rows):
        for x in range(0, columns):
            try: 
                if grid[y][x] == grid[y+1][x] == grid[y+2][x]:
                    if grid[y][x] != " " and not complete:
                        return False
                    else:
                        return False
            except IndexError:
                pass
            try:
                if grid[y][x] == grid[y][x+1] == grid[y][x+2]:
                    if grid[y][x] != " " and not complete:
                        return False
                    else:
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
    for m in range(0, columns):
        total0s = 0
        total1s = 0
        for n in range(0, rows):
            if grid[m][n] == "0":
                total0s += 1
            elif grid[m][n] == "1":
                total1s += 1
        if total0s > 4 or total1s > 4:
            return False
    return True

def solve(grid, rows, columns):
    curGrid = grid
    actualOrientation = True
    lastFour = []
    while True:
        curGrid = list(zip(*curGrid))
        actualOrientation = not actualOrientation
        for y in range(0, rows):
            curGrid[y] = list(curGrid[y])
        for y in range(0, rows):
            if curGrid[y].count("0") == 4:
                for x in range(0, columns):
                    if curGrid[y][x] == " ":
                        curGrid[y][x] = "1"
                        
            if curGrid[y].count("1") == 4:
                for x in range(0, columns):
                    if curGrid[y][x] == " ":
                        curGrid[y][x] = "0"
            for x in range(0, columns):
                if curGrid[y][x] != " ":
                    opp = switch(curGrid[y][x])
                    if x > 1 and curGrid[y][x] == curGrid[y][x-1]:
                        if x >= 2 and grid[y][x-2] == " ":
                            curGrid[y][x-2] = opp
                        if x < rows-1 and curGrid[y][x+1] == " ":
                            curGrid[y][x+1] = opp
                    if y > 1 and curGrid[y][x] == curGrid[y-1][x]:
                        if y >= 2 and curGrid[y-2][x] == " ":
                            curGrid[y-2][x] = opp
                        if y < columns-1 and curGrid[y+1][x] == " ":
                            curGrid[y+1][x] = opp
                    if y < columns-2 and curGrid[y+1][x] == " " and curGrid[y][x] == curGrid[y+2][x]:
                        curGrid[y+1][x] = opp
                    if x < rows-2 and curGrid[y][x+1] == " " and curGrid[y][x] == curGrid[y][x+2]:
                        curGrid[y][x+1] = opp
        if len(lastFour) >= 4:
            lastFour.insert(0, curGrid)
            lastFour = lastFour[0:4]
        else:
            lastFour.append(curGrid)
        breakNow = False
        try: 
            if lastFour[0] == lastFour[2] and lastFour[1] == lastFour[3]:
                breakNow = True
        except IndexError:
            pass
        if breakNow:
            break
    if not actualOrientation:
        curGrid = list(zip(*curGrid))
        actualOrientation = not actualOrientation
        for y in range(0, rows):
            curGrid[y] = list(curGrid[y])
    return(curGrid)

def main(grid):
    rows = 8
    columns = 8
    curGrid = solve(grid, rows, columns)
##    print(curGrid)
    print("c", checkSolved(curGrid, rows, columns))
##    print()
    return curGrid
##if __name__ == "__main__":
##    main(grid)
