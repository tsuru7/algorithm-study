import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    n,p,q,r,s=m_input()
    a=l_input()
    return n,p,q,r,s,a

def solve(n,p,q,r,s,a):
    ans=[]
    p -= 1
    q -= 1
    r -= 1
    s -= 1
    for i in range(p):
        ans.append(a[i])
    for i in range(p, q+1):
        ans.append(a[r+i-p])
    for i in range(q+1, r):
        ans.append(a[i])
    for i in range(r, s+1):
        ans.append(a[i-r+p])
    for i in range(s+1, n):
        ans.append(a[i])
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,p,q,r,s,a=readinput()
    ans=solve(n,p,q,r,s,a)
    printans(ans)
