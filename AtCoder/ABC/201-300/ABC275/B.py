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
    a,b,c,d,e,f=m_input()
    return a,b,c,d,e,f

def solve(a,b,c,d,e,f):
    MOD = 998244353
    a %= MOD
    b %= MOD
    c %= MOD
    d %= MOD
    e %= MOD
    f %= MOD
    abc = a*b*c
    abc %= MOD
    def_ = d*e*f
    def_ %= MOD
    ans = abc - def_
    ans %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,d,e,f=readinput()
    ans=solve(a,b,c,d,e,f)
    printans(ans)
