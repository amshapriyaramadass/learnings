import numpy as np

def arrays(arr):
    # complete this function
    # use numpy.array
    a = np.array(arr,dtype='f')
    return(a[::-1])
 

if __name__ =="__main__":
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)

