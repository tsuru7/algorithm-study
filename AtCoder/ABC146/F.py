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
    n,m=m_input()
    s=input()
    return n,m,s

def solve(n,m,s):
    ans=[]
    now = n
    while now-m > 0:
        # print(f'now: {now}, ans: {ans}')
        for next in range(now-m, now):
            if s[next] == '0':
                ans.append(now-next)
                now = next
                break
        else:
            return [-1]
    ans.append(now)
    return ans[::-1]

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,m,s=readinput()
    ans=solve(n,m,s)
    printans(ans)
