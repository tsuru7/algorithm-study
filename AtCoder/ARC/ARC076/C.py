def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n, m=m_input()
    return n,m

def fact(n, MOD):
    ans = 1
    while n > 0:
        ans = (ans * n)%MOD
        n -= 1
    return ans
    
def main(n,m):
    MOD = 10**9+7
    if n==m+1 or m==n+1:
        ans = (fact(n,MOD) * fact(m,MOD))%MOD
    elif n==m:
        ans = (fact(n,MOD) * fact(m,MOD))%MOD
        ans = (ans*2)%MOD
    else:
        ans = 0

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m=readinput()
    ans=main(n,m)
    printans(ans)
