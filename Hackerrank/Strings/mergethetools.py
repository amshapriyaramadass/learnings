def merge_the_tools(string, k):
  # your code goes here
    n = int(len(string)/k)
    t1 =[]
    # for i in range(n):

    #     a = i*k
    #     b = (i*k)+k
    #     t1.append(string[a:b])
    #     print("".join(list(dict.fromkeys(t1[i]))))
    for x in range(0,len(string),k):     
        print(''.join(list(OrderedDict.fromkeys(string[x:x+k]))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    