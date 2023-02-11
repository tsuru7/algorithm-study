def readinput():
    a,b,c=map(int,input().split())
    return a,b,c

def main(a,b,c):
    if a > b:
        return 'Takahashi'
    elif b > a:
        return 'Aoki'
    else:
        if c == 0:
            return 'Aoki'
        else:
            return 'Takahashi'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c=readinput()
    ans=main(a,b,c)
    printans(ans)
