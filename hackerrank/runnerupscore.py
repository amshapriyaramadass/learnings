if __name__ == '__main__':
    n = int(input())
    arr = ()
    arr = map(int, input().split())
    print(arr)
    
    newary = sorted(arr)
    list1 =list( dict.fromkeys(newary))
    print(list1[len(list1)-2])

