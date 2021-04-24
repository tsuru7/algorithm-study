def readinput():
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    c=list(map(int,input().split()))
    return n,k,p,c

def main(n,k,p,c):
    sums=[0]*(2*n)
    j=0
    for i in range(2*n):
        j=p[j]-1
        if i==0:
            sums[i]=c[j]
        else:
            print(i,j)
            sums[i]=sums[i-1]+c[j]
    print(sums)
    sumc=sums[n-1]
    r=k%n
    q=k//n
    maxsum1=0
    maxsum2=0
    for i in range(n):
        for j in range(min(n,k)):
            maxsum1=max(maxsum1,sums[i+j]-sums[i])
        for j in range(r):
            maxsum2=max(maxsum2,sums[i+j]-sums[i])
    if sumc<=0:
        return maxsum1
    else:
        return max(sumc*q+maxsum2,sumc*(q-1)+maxsum1,maxsum1)
        
def main2(n,k,p,c):
    


if __name__=='__main__':
    n,k,p,c=readinput()
    ans=main(n,k,p,c)
    print(ans)
