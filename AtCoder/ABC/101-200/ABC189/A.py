def readinput():
    s=input()
    return s

def main(s):
    if s[0] == s[1] and s[0] == s[2]:
        return 'Won'
    else:
        return 'Lost'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
