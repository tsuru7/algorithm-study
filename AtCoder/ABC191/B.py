def readinput():
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    return n,x,a

def main(n,x,a):
    aa = []
    for v in a:
        if v == x:
            continue
        aa.append(v)
    return aa

def printans(ans):
    print(' '.join(map(str,ans)))

if __name__=='__main__':
    n,x,a=readinput()
    ans=main(n,x,a)
    printans(ans)
