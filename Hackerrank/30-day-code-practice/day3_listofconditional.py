#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n%2 == 0 and (5 > n > 20):
        print("Not Weird")
    else:
        print("Weird")   
    # elif ((n % 2==0) and n > 20): 
    #     print("Not weird")
    # elif (n%2!=0):
    #     print("weird")      