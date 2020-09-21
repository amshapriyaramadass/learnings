from itertools import permutations

if __name__ == "__main__":
    string,number= input().split()
    print(string,number)
    p = permutations(sorted(string),int(number))
    print(*[''.join(i) for i in p],sep ='\n')