def readinput():
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    return n,m,x

def main(n,m,x):
    if m<=n:
        return 0
    xs=sorted(x)
    #print(xs)
    d=[]
    for i in range(m-1):
        d.append((xs[i+1]-xs[i],i+1))
    ds=sorted(d,reverse=True,key=lambda x:x[0])
    c=[0]*m
    for i in range(n-1):
        c[ds[i][1]]+=1
    #print(c)
    ans=0
    for i in range(1,m):
        if c[i]==0:
            ans+=xs[i]-xs[i-1]
    return ans

if __name__=='__main__':
    n,m,x=readinput()
    ans=main(n,m,x)
    print(ans)
