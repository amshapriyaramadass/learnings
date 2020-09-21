from itertools import product
# #################################################
# computes the cartesian product of input iterables.
# #################################################

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*product(a,b))

    # #####################################
    # SAmple input  
    # 1 2
    # 3 4
    # Sample Output 
    # (1,3) (1,4) (2,3) (2,4)  
    # #################################