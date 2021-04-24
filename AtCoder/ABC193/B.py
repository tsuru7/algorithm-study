def readinput():
    n=int(input())
    apx = []
    for _ in range(n):
        a,p,x=map(int,input().split())
        apx.append((a,p,x))
    return n,apx

def main(n,apx):
    INFTY = 10**9+1
    mincost = INFTY
    for a, p, x in apx:
        if x > a:
            mincost = min(mincost, p)
    if mincost == INFTY:
        return -1
    else:
        return mincost

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,apx=readinput()
    ans=main(n,apx)
    printans(ans)
