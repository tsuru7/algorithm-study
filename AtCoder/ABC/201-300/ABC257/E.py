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
    c=l_input()
    return n,c

memo = dict()
def dfs(x, cost, c, n):
    global memo
    if x in memo:
        return memo[x]
    ans = 0
    for i in range(9):
        if cost + c[i] > n:
            ans = max(ans, x)
        else:
            ans = max(ans, dfs(x*10+i+1, cost+c[i], c, n))
    memo[x] = ans
    return ans

def solve(n,c):
    ans = dfs(0, 0, c, n)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,c=readinput()
    ans=solve(n,c)
    printans(ans)
