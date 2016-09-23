import itertools
class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

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
    return True



a = list(perm_unique([1,1,1,1,0,0,0,0]))
##print(a)
columns = 8
for m in range(0, len(a)):
    a[m] = list(a[m])
    for n in range(len(a[m])):
        a[m][n] = str(a[m][n])
        
for i in range(len(a)-1, -1, -1):
    for x in range(0, columns):
        try:
            if a[i][x] == a[i][x+1] == a[i][x+2]:
                del a[i]
                break
        except IndexError:
            pass
print()
print(a)
##f = open("output.txt", "w")
##b = list(itertools.permutations(a,1))
##print()
##print(b)
##f.write(b)
##f.close()
##print("done")
