from bisect import bisect_left, bisect_right

def readinput():
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,k,a

def main(n,k,a):
    s=[0]*(n+1)
    for i in range(1,n+1):
        s[i]=s[i-1]+a[i-1]

    count=0
    j=bisect_right(s,k)-1
    for i in range(n):
        while j<=n and s[j]-s[i]<k:
            j+=1
        else:
            if j>n:
                break
        count+=n-j+1
    return count

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    print(ans)
