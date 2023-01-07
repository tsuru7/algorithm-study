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
    a=l_input()
    return n,a

def solve(n,a):
    count = dict()
    for i in range(n):
        tmp = a[i] - (i + 1)
        if tmp in count:
            count[tmp].append(i)
        else:
            count[tmp] = [i]
    
    # print(f'count: {count}')

    ans=0
    for i in range(n):
        tmp = -(i + 1) - a[i]
        if tmp in count:
            idx = bisect_right(count[tmp], i)
            ans += len(count[tmp]) - idx

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
