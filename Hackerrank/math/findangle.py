import math
import cmath

if __name__ == '__main__':
    len1 = int(input())
    len2 = int(input())

    print(str(int(round(math.degrees(math.atan2(len1, len2))))) + '°')
