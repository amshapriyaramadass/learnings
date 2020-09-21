if __name__ == '__main__':
    n = int(input())
    name_num = dict(input().split() for _ in range(n))
    # namearr = {name: number for name,number in name_num}
# Sample Input

# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
# Sample Output

# sam=99912222
# Not found
# harry=12299933

    while True:
        try:
            name = input()
            if name in name_num:
                print(f'{name}={(name_num.get(name))}')
            else:
                print('Not found')   
        except EOFError:
            break

