# Sample Input
#   1+2j

#  Sample Output

#  2.23606797749979 
#  1.1071487177940904

import math
import cmath

if __name__ == '__main__':
    polarin = complex(input())
    x1 = pow(polarin.real,2)
    y1 = pow(polarin.imag,2)

    x = math.sqrt(x1+y1)

    print(x,math.atan2(polarin.imag, polarin.real),sep ='\n') 
    # easy way to get output use cmath.polar
    # print(*cmath.polar(polarin),sep ='\n')
  