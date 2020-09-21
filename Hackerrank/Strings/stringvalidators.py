if __name__ == '__main__':
    s = input()
    l = list(s)
    print(l)

    print(len([a for a in l if a.isalnum()])>0)
    print(len([a for a in l if a.isalpha()])>0)
    print(len([a for a in l if a.isdigit()])>0)
    print(len([a for a in l if a.islower()])>0)
    print(len([a for a in l if a.isupper()])>0)



    
