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
    s=l_input()
    return n,s

def solve(n,s):

    ans=[s[0]]
    for i in range(1, n):
        ai = s[i] - s[i-1]
        ans.append(ai)
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
