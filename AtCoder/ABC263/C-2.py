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
    n,m=m_input()
    return n,m

def dfs(l, n, m):
    ans = []
    if len(l) == n:
        return [l]
    if len(l) == 0:
        last_num = 0
    else:
        last_num = l[-1]
    for i in range(last_num+1, m+1):
        ans += dfs(l+[i], n, m)
    # print(f'ans: {ans}')
    return ans


def solve(n,m):
    ans=dfs([], n, m)
    return sorted(ans)

def printans(ans):
    # print(f'ans: {ans}')
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,m=readinput()
    ans=solve(n,m)
    printans(ans)
