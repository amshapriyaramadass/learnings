#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    return (n*factorial(n-1)) if n!=0 else 1
    # x = 1
    # for i in range(1,n+1):
    #     x *= i
    # print(x)
    # return x
    

if __name__ == '__main__':
    

    n = int(input())

    result = factorial(n)

    print(str(result) + '\n')


