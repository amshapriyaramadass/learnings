def minion_game(string):
    kevincount , struatcount = 0,0
    vowels = 'AEIOU'
    for i in range(len(string)):
        if string[i] in vowels:
            kevincount += (len(string)-i)
        else:
            struatcount += (len(string)-i)    

    if kevincount > struatcount:
        print("Kevin", kevincount)
    elif kevincount < struatcount:
        print("Struat",struatcount)  
    else:
        print("Draw")

    

if __name__ == '__main__':
    s = input()
    minion_game(s)

