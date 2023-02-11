def readinput():
    n,m=list(map(int,input().split()))
    a=[]
    for _ in range(m):
        a.append(int(input()))
    return n,a

def main(n,a):
    MOD=10**9+7

    nroute=[0]*(n+2)
    nroute[0]=0
    nroute[1]=1
    nroute[2]=1
    for i in range(3,n+2):
        nroute[i]=(nroute[i-1]+nroute[i-2])%MOD
    #print(nroute)
    
    subn=[]
    i=0
    for j in a:
        subn.append((i,j-1))
        i=j+1
    subn.append((i,n))
    #print(subn)

    nways=1
    for i,j in subn:
        l=j-i+1
        nways=nways*nroute[l]%MOD

    return nways

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)

