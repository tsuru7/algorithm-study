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
    dp[0][0] = 0
    for state in range(ALL):
        for cur_city in range(n):
            # cur_city が未訪問だったら(dp[cur_city][state] が初期値から更新されていなかったら)スキップ
            if dp[cur_city][state] == INFTY:
                continue
            cur_x, cur_y = xyList[cur_city]
            for next_city in range(n):
                if state & (1<<next_city) > 0:
                    continue
                next_state = state | (1<<next_city) # next_state は必ず state より大きな値になる ⇒ 配るDP
                next_x, next_y = xyList[next_city]
                etime = sqrt((cur_x - next_x)**2 + (cur_y - next_y)**2)
                dp[next_city][next_state] = min(dp[next_city][next_state], dp[cur_city][state] + etime)
    # print(*dp, sep='\n')
    return dp[0][-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xyList=readinput()
    ans=solve(n,xyList)
    printans(ans)
