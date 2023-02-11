import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import Counter

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
    counter = Counter(a)
    tmp = list(counter.items())
    tmp.sort()
    cumcnt = []
    cnt = 0
    for k, v in tmp:
        cumcnt.append((k, cnt+v))
        cnt += v
    # print(f'cumcnt: {cumcnt}')
    ans=0
    for j in range(1, len(cumcnt)-1):
        ans += cumcnt[j-1][1]*(cumcnt[j][1]-cumcnt[j-1][1])*(n-cumcnt[j][1])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
