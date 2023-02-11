import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    n,k=m_input()
    return n,k

def solve(n,k):
    MOD = 10**9+7
    m = min(n-1, k)
    comb0 = [0 for _ in range(m+1)]
    comb1 = [0 for _ in range(m+1)]
    comb0[0] = 1
    comb1[0] = 1

    for i in range(1, m+1):
        invi = pow(i, MOD-2, MOD)
        comb0[i] = comb0[i-1]*(n-i+1)*invi
        comb1[i] = comb1[i-1]*(n-i)*invi
        comb0[i] %= MOD
        comb1[i] %= MOD
    
    ans=0
    for i in range(m+1):
        ans += comb0[i]*comb1[i]
        ans %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
