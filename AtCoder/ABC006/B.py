def readinput():
    n=int(input())
    return n

def main(n):
    a=[0]*(10**6)
    a[0]=0
    a[1]=0
    a[2]=1
    for i in range(3,n):
        a[i]=(a[i-3]+a[i-2]+a[i-1])%10007
    return a[n-1]

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
