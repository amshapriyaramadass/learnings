#!/bin/python3

import math
import os
import random
import re
import sys

# Context
# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
#  Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

#  Sample output = 19

Input Format

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    count1 =[]
    for i in range(0,4):
        for j in range(0,4):
            total = sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3]) 
            count1.append(total)
           

    print(max(count1))        

     
          



