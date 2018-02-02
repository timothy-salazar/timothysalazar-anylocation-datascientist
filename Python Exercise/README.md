# Warwick - Python Programming Challenge

There are two Python Programming challenges you will complete. We hope you enjoy them!

## Rules

- Use Python 3.x

- Each challenge should be answered by a single Python executable named **python-{challengenumber}.py**

- All of your answers should include tests. Consider the unittest module.

### Challenge 1 - IP Address

An IP address consists of 4 numbers separated by periods. Each number can be 0 to 255. There are no periods at the start or end of a valid IP address.

Create a program that takes an IP address and prints out whether the received IP address is valid or invalid. If the IP address is valid, print out the the length of each segment and their numbers. If the IP address is invalid, let the program detail why the address was invalid and suggestions for fixing the address. 

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

Create a program that initializes a randomly generated black and white image of **nxk** dimensions where **n=len(row)** and **k=len(col)** and implements a 1-Manhattan blur transformation which causes any 1 in the image to cause the pixel to the left, right above and below a 1 to become a 1. 

The Manhattan distance is the distance between two points in a grid based on a strictly horizontal and/or vertical path (that is, along the grid lines). 

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

In the previous assignment we built a method that will produce the blurring with a Manhattan Distance of one.
Now instead of only blurring images that are within 1 pixel, we want to specify how far to blur pixels that are within a Manhattan Distance of what is specified. 

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

Refactor your program to implement a blurring of y-Manhattan distance, where y is any natural number. 
