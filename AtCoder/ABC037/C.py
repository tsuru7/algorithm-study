def readinput():
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,k,a

def main(n,k,a):
    sum=0
    hi=1
    lo=1-k
    for i in range(1,n+1):
        sum+=a[i-1]*(min(n-k+1,hi)-max(0,lo))
        hi+=1
        lo+=1
    return sum

def main2(n,k,a):
    sum=0
    m=min(k-1,n-k)

    for i in range(1,m+1):
        sum+=a[i-1]*i
    for i in range(m+1,n-m):
        sum+=a[i-1]*(m+1)
    for i in range(n-m,n+1):
        sum+=a[i-1]*(n-i+1)
    return sum

def main3(n,k,a):
    s=[0]*(n+1)
    for i in range(n):
        s[i+1]=s[i]+a[i]
    #print(a,s)
    sum=0
    i=0
    while(i+k<=n):
        sum+=s[i+k]-s[i]
        i+=1
    return sum

if __name__=='__main__':
    n,k,a=readinput()
    ans=main3(n,k,a)
    print(ans)
