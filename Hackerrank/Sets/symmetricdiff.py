if __name__ == '__main__':
    n = int(input())
    xarr = set(map(int, input().split()))
    y = int(input())
    yarr = set(map(int, input().split()))

    print(*sorted((xarr.symmetric_difference(yarr))),sep='\n')

   