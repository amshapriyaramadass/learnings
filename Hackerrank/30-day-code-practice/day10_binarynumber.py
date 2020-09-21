#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    x = "{0:b}".format(int(n))
    a = max(x.split('0')).count('1')
    print(a)