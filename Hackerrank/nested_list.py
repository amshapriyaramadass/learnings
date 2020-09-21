
if __name__ == '__main__':

    n = int(input())
    arr = [[input(), float(input())] for _ in range(n)]
    
    second_highest=sorted(list(set([marks for name,marks in arr])))[1]
    # print(second_highest)
    print('\n'.join([a for a,b in sorted(arr) if b == second_highest]))

    
