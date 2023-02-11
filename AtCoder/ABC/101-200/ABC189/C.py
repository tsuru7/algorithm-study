def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    maxsum = 0
    for l in range(n):
        mina = a[l]
        for r in range(l, n):
            mina = min(mina, a[r])
            maxsum = max(maxsum, mina*(r+1-l))
            
    return maxsum

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
