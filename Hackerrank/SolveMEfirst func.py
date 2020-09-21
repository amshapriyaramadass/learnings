# def solveMeFirst(a,b):
# 	# Hint: Type return a+b below
#   return a+b


# num1 = int(input("Please enter num1:"))
# num2 = int(input("Please enter num2:"))
# res = solveMeFirst(num1,num2)
# print(res)


print("Hello, World!")

#!/bin/python

import math
import os
import random
import re
import sys

def main():

    n = int(input("Please enter number").strip())

    if n%2 == 0 and ( n in range (2,5)):
        print("not weird")

    elif n%2 == 0 and (n in range (6,21)):
        print('weird')   
    elif ((n % 2==0) and n > 20): 
        print("Not weird")
    elif (n%2!=0):
        print("weird")      

if __name__ == '__main__':
    main()
    
