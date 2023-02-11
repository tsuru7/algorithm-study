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
    return s

def dfs(s):
    ans = 0
    n = len(s)
    if n == 1:
        return ord(s[0]) - ord('A') + 1
    head = ord(s[0]) - ord('A')
    ans += 26**(n-1) * head
    ans += dfs(s[1:])
    return ans

def solve(s):
    n = len(s)
    ans=0
    for i in range(1, n):
        ans += 26**i
    ans += dfs(s)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
