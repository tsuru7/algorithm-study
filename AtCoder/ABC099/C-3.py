import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(4096*1024)
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

def coinlist(n):
    ans = [1]
    x = 6
    while x <= n:
        ans.append(x)
        x *= 6
    x = 9
    while x <= n:
        ans.append(x)
        x *= 9
    return ans

memo = None
def f(x, coins):
    global memo
    print(sys.getrecursionlimit())

    print(f'[f] x: {x}')
    if x in coins:
        return 1
    if memo[x] < INFTY:
        return memo[x]
    ans = INFTY
    for coin in coins:
        if x - coin > 0:
            ans = min(ans, 1+f(x-coin, coins))
    memo[x] = ans
    print(f'x: {x}, memo[x]: {memo[x]}')
    return ans

def solve(n):
    global memo
    coins = coinlist(n)
    print(f'coins: {coins}')
    ans=INFTY
    memo = [INFTY for _ in range(n)]
    for coin in coins:
        if n-coin > 0:
            ans = min(ans, 1+ f(n-coin, coins))
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':

    # print(sys.getrecursionlimit())

    n=readinput()
    ans=solve(n)
    printans(ans)
