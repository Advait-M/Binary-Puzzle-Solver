rows = 8
grid = []
# Function to calculate length of a line segment.
def length(x1, y1, x2, y2):
    l = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return l
# Function to calculate slope of a line segment
def slope(x1, y1, x2, y2):
    try:
        m = (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        m = "undefined"
    return m

def checkSolved(grid, rows, columns):
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
    return True

def switch(x):
    return {
        "0": "1",
        "1": "0",
    }[x]

for i in range(0, rows):
    temp = list(input())
    grid.append(temp)
    columns = len(temp)
curGrid = grid
actualOrientation = True
for i in range(0, 50):
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
                    
print(curGrid)
print("c", checkSolved(curGrid, rows, columns))
print()