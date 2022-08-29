import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    a = [i_input() for _ in range(n)]
    return n,a

def lis(a, used):
    dp = [(INFTY, -1) for _ in range(n)]
    prev = [-INFTY for _ in range(n)]
    maxlen = 0
    for i in range(n):
        if used[i]:
            continue
        ai = a[i]
        idx = bisect_left(dp, (ai, -1))
        if idx < n:
            dp[idx] = (ai, i)
            maxlen = max(maxlen, idx)
            if idx == 0:
                prev[i] = -1
            else:
                prev[i] = dp[idx-1][1]
    # print(f'a: {a}')
    # print(f'used: {used}')
    # print(f'prev: {prev}')
    # print(f'dp: {dp}')
    used[dp[maxlen][1]] = True
    p = prev[dp[maxlen][1]]
    while p != -1:
        used[p] = True
        p = prev[p]
    return maxlen

def solve(n,a):
    used = [False for _ in range(n)]
    color = 0
    tmp = lis(a, used)
    while tmp > 1:
        color += 1
        if sum(used) == n:
            break
        tmp = lis(a, used)
    else:
        color += 1 + n-sum(used)
    return color

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
