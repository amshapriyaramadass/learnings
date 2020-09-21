#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path

#Sample Input
#
#8
#UDDDUDUU
#Sample Output

#1


#

def countingValleys(steps, path):
    sealevel = 0
    valeylevel = 0
    for path1 in path:
        if path1 == 'U':
            sealevel += 1
        else:
            sealevel -= 1
        if path1 == 'U' and sealevel == 0:
            valeylevel += 1
    return valeylevel                   

    # Write your code here

if __name__ == '__main__':
    
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)

   