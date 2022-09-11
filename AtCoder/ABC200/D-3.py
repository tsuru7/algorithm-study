import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
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
    n=i_input()
    a=l_input()
    return n,a

def bitpos(x):
    ans = []
    b = 0
    while 1<<b <= x:
        if x & 1<<b > 0:
            ans.append(b+1)
        b += 1
    return ans

def solve(n,a):
    count = defaultdict(list)
    m = min(n, 8)
    ALL = 2**m
    for x in range(1, ALL):
        tmp = 0
        for bit in range(m):
            if x & 1<<bit > 0:
                tmp += a[bit]
        tmp %= 200
        count[tmp].append(x)
    for k, v in count.items():
        if len(v) > 1:
            b = bitpos(v[0])
            c = bitpos(v[1])
            # print(f'b: {b}, c: {c}')
            return ['Yes', [len(b)]+b, [len(c)]+c]
    return ['No']

def printans(ans):
    if len(ans) == 1:
        print(ans[0])
    else:
        print(ans[0])
        print(*ans[1])
        print(*ans[2])

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
