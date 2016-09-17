from numpy import loadtxt
f = open("output.txt", "r")
b = f.readline()
lines = loadtxt(f, comments="#", delimiter=",", unpack=False)
f.close()
print(b)
print(lines)
