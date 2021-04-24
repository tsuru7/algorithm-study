def readinput():
    n,m=list(map(int,input().split()))
    return n,m

def main(n,m):
    MOD=10**9+7
    ans=1
    if m>n:
        for i in range(n):
            ans=ans*(m-i)%MOD
            ans=ans*(m-i-1)%MOD
    else:
        for i in range(n-1):
            ans=ans*(m-i)%MOD
            ans=ans*(m-i-1)%MOD
    return ans

if __name__=='__main__':
    n,m=readinput()
    ans=main(n,m)
    print(ans)
