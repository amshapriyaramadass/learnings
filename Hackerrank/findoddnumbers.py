#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def oddNumbers(l, r):
    new_arr =[]
    for n in range(l,r+1):
        if n%2 !=0:
            new_arr.append(n)
    return new_arr
            

    # Write your code here

if __name__ == '__main__':
        
    l = int(input().strip())

    r = int(input().strip())

    result = oddNumbers(l, r)

    print('\n'.join(map(str, result)))
    
