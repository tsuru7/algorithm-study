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

memo = dict()
def f(x):
    global dict
    if x in memo:
        return memo[x]
    ans = f(x//2) + f(x//3)
    memo[x] = ans
    return ans

def solve(n):
    global memo
    memo[0] = 1

    ans=f(n)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
