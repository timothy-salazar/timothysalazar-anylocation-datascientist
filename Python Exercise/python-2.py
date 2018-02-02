'''
### Challenge 2 - Two Dimensional Lists

Often, complicated problems can be broken down into a simple pictoral representation of data. For example, take the example of building a representation of an image on your computer. Images can be represented as a collection of pixels, where each pixel has a location and a color.

Let's think about the simplest representation of an image, a pure black and white image. A black and white image can be represented by a two-dimensional list of 0's and 1's. For example if we think about the representation of an image, an example of an image could look like this, where 0's represent the pixel being off and 1's represent the pixel being on.

**Black Diagonal Line in 3x3 white canvas**
```python
[
 [0,0,1],
 [0,1,0],
 [1,0,0]
]
```
Create a program that initializes a randomly generated black and white image of
**nxk** dimensions where **n=len(row)** and **k=len(col)** and implements a
1-Manhattan blur transformation which causes any 1 in the image to cause the
pixel to the left, right above and below a 1 to become a 1.

The Manhattan distance is the distance between two points in a grid based on a
strictly horizontal and/or vertical path (that is, along the grid lines).

**Example of 1-Manhattan Distance Blur Transformation**
```python
# Randomly Generated Image Before Transformation
[
 [1,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [0,0,0,0,0]
]
# After Transformation
[
 [1,1,0,0,0],
 [1,0,0,1,0],
 [0,0,1,1,1],
 [0,0,0,1,0]
]
```
'''
import random

def manhattan_blur(rand_m,n,k):
    castle = set()
    for i in range(n):
        for j in range(k):
            if rand_m[i][j] == 1:
                castle.add((i,j))
                for p in range(-1,3):   # before I came to my senses, this was a
                                        # NIGHTMARISH list comp.
                    a = i + (p + (-1)**(p+1))//2 if (-1<(i + (p + (-1)**(p+1))//2)<n) else i
                    #         ^ this gives us the sequence 0,-1,1,0
                    b = j + p//2 if (-1<(j + p//2)<k) else j
                    #        ^ this gives us 1,0,0,1. Together they give us
                    #        all the horizontally/vertically adjacent spots
                    # The ternary operators cover cases where we would otherwise
                    # generate indices that are out of range, producing (i,j)
                    # instead
                    castle.add((a,b))
                    # ^ putting the pair into a set, so we only have to deal with
                    # each pair of (row,col) once.
    manhattan = [[0]*k for _ in range(n)]
    for i in castle:
        manhattan[i[0]][i[1]] = 1
    return manhattan

def rand_nxk(n,k):
    rand_m = [random.choices([0,1],k=k) for i in range(n)]
    return rand_m

def main(n=None,k=None):
    if n == None:
        n = user_input('Value for n? -->')
        k = user_input('Value for k? -->')
    rand_m = rand_nxk(n,k)
    return manhattan_blur(rand_m,n,k)

if __name__ == '__main__':
    main()
















#
