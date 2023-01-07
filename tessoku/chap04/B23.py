import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import sqrt

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
    xyList = [l_input() for _ in range(n)]
    return n,xyList

def visited_count(state):
    return (bin(state)[2:]).count('1')

def solve(n,xyList):
    ALL = 2**n
    dp = [[INFTY for _ in range(ALL)] for _ in range(n)]
    dp[0][1] = 0
    for ncity in range(1, n):
        for cur_state in range(ALL):
            if visited_count(cur_state) != ncity:
                continue
            for cur_city in range(n):
                if cur_state & (1<<cur_city) == 0:
                    continue
                cur_x, cur_y = xyList[cur_city]
                for next_city in range(n):
                    if cur_state & (1<<next_city) > 0:
                        continue
                    next_x, next_y = xyList[next_city]
                    etime = sqrt((cur_x - next_x)**2 + (cur_y - next_y)**2)
                    next_state = cur_state | (1<<next_city)
                    dp[next_city][next_state] = \
                        min(dp[next_city][next_state], dp[cur_city][cur_state] + etime)
    ans=INFTY
    x0, y0 = xyList[0]
    for cur_city in range(1, n):
        x, y = xyList[cur_city]
        etime = sqrt((x-x0)**2 + (y-y0)**2)
        ans = min(ans, dp[cur_city][-1]+etime)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xyList=readinput()
    ans=solve(n,xyList)
    printans(ans)
