import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque

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
    a=l_input()
    return n,a

def solve(n,a):
    order = range(n)[::-1]
    # print(f'order: {order}')
    ans = [0 for _ in range(n)]
    for shain in order:
        if shain == 0:
            break
        boss = a[shain-1]-1
        ans[boss] += ans[shain] + 1

    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
