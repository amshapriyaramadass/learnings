from itertools import combinations
from itertools import combinations_with_replacement

# if __name__ == "__main__":
#     string,number= input().split()
#     # c = combinations(sorted(string),int(number))
#     for i in range(1,int(number)+1):
#         for c in combinations(sorted(string),i):
#             print(''.join(c))


# from itertools import combinations

if __name__ == "__main__":
    string,number= input().split()
    c = combinations_with_replacement(sorted(string),int(number))
    print(*[''.join(i) for i in c],sep='\n')
    # for i in range(1,int(number)+1):
    #     for c in combinations(sorted(string),i):
    #         print(''.join(c))