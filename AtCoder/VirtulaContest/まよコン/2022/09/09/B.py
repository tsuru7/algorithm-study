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
    n=i_input()
    a=l_input()
    return n,a

def solve(n,a):
    acc1 = list(accumulate(a))
    # print(f'a: {a}')
    # print(f'acc1: {acc1}')
    b = [a[i]*a[i] for i in range(n)]
    acc2 = list(accumulate(b))
    # print(f'b: {b}')
    # print(f'acc2: {acc2}')
    ans=0
    for i in range(1, n):
        ans += i*a[i]*a[i] -2*a[i]*acc1[i-1] + acc2[i-1]
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
