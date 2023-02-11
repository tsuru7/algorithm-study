import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate

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
    a=l_input()
    return n,m,a

def solve(n,m,a):
    ans = -INFTY
    acc = [0] + list(accumulate(a))
    # print(f'acc: {acc}')
    sum = 0
    for i in range(m):
        sum += acc[m] - acc[i]
    ans=max(ans, sum)
    # print(f'sum: {sum}')
    i = 0
    while m+i < n:
        sum -= acc[m+i]-acc[i]
        sum += a[m+i]*m
        ans = max(ans, sum)
        # print(f'sum: {sum}')

        i += 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a=readinput()
    ans=solve(n,m,a)
    printans(ans)
