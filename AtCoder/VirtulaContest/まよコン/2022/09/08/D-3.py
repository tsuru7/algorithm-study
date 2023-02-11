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
    a,b,k=m_input()
    return a,b,k

def dfs(now, ra, rb):
    if ra == 0 and rb == 0:
        return [now]
    ans = []
    if ra > 0:
        ans += dfs(now+'a', a-1, b)
    else:
        ans += [now+'b'*b]
    if rb > 0:
        ans += dfs(now+'b', a, b-1)
    else:
        ans += [now+'a'*a]
    return ans

def solve(a,b,k):
    ans=dfs('', a, b)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,k=readinput()
    ans=solve(a,b,k)
    printans(ans)
