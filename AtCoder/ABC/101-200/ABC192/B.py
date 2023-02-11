def readinput():
    s=input()
    return s

def main(s):
    for i, c in enumerate(s):
        if i % 2 == 0 and c.islower():
            continue
        elif i % 2 == 1 and c.isupper():
            continue
        else:
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
