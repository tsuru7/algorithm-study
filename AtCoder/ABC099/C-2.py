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

memo = [INFTY for _ in range(100000+1)]
def dfs(x):
    money = [1, 6, 6**2, 6**3, 6**4, 6**5, 6**6, 9, 9**2, 9**3, 9**4, 9**5]
    if x in money:
        return 1
    if x == 0:
        return 0
    if memo[x] < INFTY:
        return memo[x]
    ans = INFTY
    for m in money:
        if x - m >= 0:
            ans = min(ans, dfs(x-m)+1)
    memo[x] = ans
    return ans

def solve(n):
    ans = dfs(n)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
