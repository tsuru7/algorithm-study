def readinput():
    a,b=map(int,input().split())
    return a,b

def main(a,b):
    if a>=13:
        return b
    elif a>=6:
        return b//2
    else:
        return 0

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    print(ans)
