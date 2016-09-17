import itertools
import numpy as np
def expandgrid(*itrs):
   product = list(itertools.product(*itrs))
   return {'Var{}'.format(i+1):[x[i] for x in product] for i in range(len(itrs))}
#print(list(itertools.permutations([0,0,0,0,1,1,1,1])))
print(list(itertools.permutations([0,0,0,0,1,1,1,1], 8)))
a = [0,1,0,1,0,1,0,1]
b = [5,7,9]
print(expandgrid(a, b))
def grids(n):
   a = []
   shift = np.arange(n*n).reshape(n, n)
   for j in range(2**(n*n)):
       a.append((j >> shift & 1).tolist())
   print(a)
grids(2)
