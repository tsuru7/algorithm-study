import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
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
    s = input()
    return n,s

def solve(n,s):
    limits1 = [1 for _ in range(n)]
    limits2 = [1 for _ in range(n)]
    for i in range(n-1):
        si = s[i]
        if si == 'A':
            limits1[i+1] = limits1[i] + 1
    for i in range(n-1)[::-1]:
        si = s[i]
        if si == 'B':
            limits2[i] = limits2[i+1] + 1
    ans = 0
    for i in range(n):
        ans += max(limits1[i], limits2[i])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
