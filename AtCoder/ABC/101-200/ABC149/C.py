def readinput():
    n=int(input())
    return n

def main(n):
    if n==2:
        return 2
    
    nmax=2*10**5
    isprime=[1]*(nmax)
    isprime[0]=0
    isprime[1]=0
    m=4
    while(m<nmax):
        isprime[m]=0
        m+=2
    
    for i in range(3,nmax,2):
        if isprime[i]==0:
            continue
        else:
            if i>=n:
                return i
        m=2*i
        while(m<nmax):
            isprime[m]=0
            m+=i
    return -1

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
