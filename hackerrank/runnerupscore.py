if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    newary = sorted(arr)
    list1 =list( dict.fromkeys(newary))
    print(list1[len(list1)-2])

