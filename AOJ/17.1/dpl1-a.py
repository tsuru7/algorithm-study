import sys
INFTY=sys.maxsize

def readinput():
    n,m=list(map(int,input().split()))
    c=list(map(int,input().split()))
    return n,m,c

def main(n,m,c):
    T=[INFTY]*(n+1)
    T[0]=0
    for i in range(m):
        for j in range(c[i], n+1):
            T[j]=min(T[j], T[j-c[i]]+1)
    return T[n]

if __name__=='__main__':
    n,m,c=readinput()
    ans=main(n,m,c)
    print(ans)
