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
    n=i_input()
    return n

def solve(n):
    MOD = 10**9 + 7
    f = [0 for _ in range(n+1)]
    f[0] = 0
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        f[i] = (f[i-1] + f[i-2]) % MOD
    return f[n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
