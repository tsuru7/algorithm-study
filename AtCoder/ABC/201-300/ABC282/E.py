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

def pow_k(x, n, m):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
            K %= m
        x *= x
        x %= m
        n //= 2

    return (K * x) % m

def readinput():
    n,m=m_input()
    a=l_input()
    return n,m,a

def solve(n,m,a):
    candidates = []
    for i in range(n):
        ai = a[i]
        for j in range(i+1, n):
            aj = a[j]
            tmp1 = pow_k(ai, aj, m)
            tmp2 = pow_k(aj, ai, m)
            candidates.append((tmp1+tmp2) % m)
    candidates.sort(reverse=True)
    ans = sum(candidates[:n-1])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a=readinput()
    ans=solve(n,m,a)
    printans(ans)
