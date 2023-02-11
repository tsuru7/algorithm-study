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
    s = input()
    t = input()
    return s, t

def solve(s, t):
    lens = len(s)
    lent = len(t)
    pre = [True for _ in range(lent+1)]
    post = [True for _ in range(lent+1)]

    for i in range(lent)[::-1]:
        if s[lens-lent+i] == t[i] or s[lens-lent+i] == '?' or t[i] == '?':
            pre[i] = pre[i+1]
        else:
            pre[i] = False

    for i in range(lent):
        if s[i] == t[i] or s[i] == '?' or t[i] == '?':
            post[i+1] = post[i]
        else:
            post[i+1] = False

    ans = ['Yes' if post[i] and pre[i] else 'No' for i in range(lent+1)]

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    s, t=readinput()
    ans=solve(s, t)
    printans(ans)
