#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.


if __name__ == '__main__':

    n,k = map(int,input().split())

   
    p = n*k % 9
    print(p if p else 9)

