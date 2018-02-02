'''
In the previous assignment we built a method that will produce the blurring with
a Manhattan Distance of one.
Now instead of only blurring images that are within 1 pixel, we want to specify
how far to blur pixels that are within a Manhattan Distance of what is
specified.

**Example of 2-Manhattan Distance Blur Transformation**
```python
# Randomly Generated Image Before Transformation
[
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,1,0,0,0],
 [0,0,0,0,0]
]
# After Transformation
[
 [0,1,0,0,0],
 [1,1,1,0,0],
 [1,1,1,1,0],
 [1,1,1,0,0]
]
```

Refactor your program to implement a blurring of y-Manhattan distance, where y
is any natural number.
'''

import random
from collections import deque

class manhattanBlurCalc():
    def __init__(self,n,k,depth):
        self.castle = set()
        self.n = n
        self.k = k
        self.depth = depth

    def l1_calcs(self,i,j,l1_depth=0):
        self.castle.add((i,j))
        if l1_depth == self.depth:
            return
        else:
            l1_depth += 1
        for p in range(-1,3):
            i_comp = i + (p + (-1)**(p+1))//2
            a = i_comp if (-1<i_comp<self.n) else i
            b = j + p//2 if (-1<(j + p//2)<self.k) else j
            self.l1_calcs(a,b,l1_depth = l1_depth)


    def manhattan_blur(self):
        for i in range(self.n):
            for j in range(self.k):
                if self.rand_m[i][j] == 1:
                    self.l1_calcs(i,j)
        manhattan = [[0]*self.k for _ in range(self.n)]
        for i in self.castle:
            manhattan[i[0]][i[1]] = 1
        return manhattan

    def rand_nxk(self,n,k):
        rand_m = [random.choices([0,1],k=k) for i in range(n)]
        self.rand_m = rand_m

    def input_nxk(self,rand_m):
        self.rand_m = rand_m

def main():
    m = manhattanBlurCalc(4,5,2) # using the example 2d list - 4x5, depth 2
    m.input_nxk([[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0]])
    new_nxk = m.manhattan_blur()
    assert new_nxk == [[0,1,0,0,0],[1,1,1,0,0],[1,1,1,1,0],[1,1,1,0,0]]
    print('success!')



if __name__ == '__main__':
    main()
