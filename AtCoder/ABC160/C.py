def readinput():
    k,n=map(int,input().split())
    a=list(map(int,input().split()))
    return k,n,a

def main(k,n,a):
    dmax=0
    for i in range(n-1):
        dmax=max(dmax,a[i+1]-a[i])
    dmax=max(dmax,k+a[0]-a[n-1])
    return k-dmax

if __name__=='__main__':
    k,n,a=readinput()
    ans=main(k,n,a)
    print(ans)
