def readinput():
    n,k=map(int,input().split())
    return n,k

def main(n,k):
    MOD = 10**9+7
    sum = 0
    for i in range(k, n+2):
        sum += i*(2*n-i+1)//2 - i*(i-1)//2 + 1
        sum = sum%MOD
    return sum

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    print(ans)
