import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate
from collections import defaultdict

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
    n,x,y=m_input()
    a=l_input()
    return n,x,y,a

def solve(n,x,y,a):
    b = list(accumulate(a))
    dpo = [set() for _ in range(n+1)]
    dpe = [set() for _ in range(n+1)]
    # 偶数回目
    dpe[0] = {0}
    for i in range(2, n+1):
        for yj in dpe[i-2]:
            dpe[i].add(yj+a[i-1])
            dpe[i].add(yj-a[i-1])
    m = n//2 * 2
    if y not in dpe[m]:
        return 'No'

    # 奇数回目
    dpo[1] = {a[0]}
    for i in range(3, n+1):
        for xj in dpo[i-2]:
            dpo[i].add(xj+a[i-1])
            dpo[i].add(xj-a[i-1]) 
    m = (n-1)//2 * 2 + 1
    if x not in dpo[m]:
        return 'No'
    
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,a=readinput()
    ans=solve(n,x,y,a)
    printans(ans)
