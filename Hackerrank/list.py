if __name__ == '__main__':
    output_list = []
    N = int(input())
    for i in range(N):
        l = list((input().split()))
        print(l)
        print(l[0])
        if l[0] == "append":
            output_list.append(int(l[1]))
        elif l[0] == "insert":   
            output_list.insert(int(l[1]),int(l[2]))
        elif l[0] == "remove":
            output_list.remove(int(l[1]))
        elif l[0]  == "sort":
            output_list = sorted(output_list)
        elif l[0]  == "print":
            print(output_list)
        elif l[0]  == "pop":
            output_list.pop()
        elif l[0] == "reverse":
            output_list.reverse()


   #  Another way of doing this 
    # n = input()
    # l = []
    # for _ in range(n):
    #     s = raw_input().split()
    #     cmd = s[0]
    #     args = s[1:]
    #     if cmd !="print":
    #         cmd += "("+ ",".join(args) +")"
    #         eval("l."+cmd)
    #     else:
    #         print l


