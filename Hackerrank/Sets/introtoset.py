def average(array):
    print(array)
    x = set(array)
    print(x)
    s = (sum(x)/len(x))
    return s

    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)