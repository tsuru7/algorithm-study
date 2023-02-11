from bisect import bisect_left, bisect_right

def readinput():
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,k,a

def main(n,k,a):
    MOD=10**9+7
    absa=[]
    for i in range(n):
        absa.append((abs(a[i], a[i])))
    a.sort()
    j=bisect_left(a,0)-1
    if j%2==1:

    ans=1
    for i in range(k):
        ans=ans*a[i]%MOD
    return ans

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    print(ans)
