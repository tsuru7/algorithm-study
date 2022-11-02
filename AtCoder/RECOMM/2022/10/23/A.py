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
    n,k=m_input()
    s = input()
    return n,k,s

def solve(n,k,s):
    region = []
    one = True
    count = 0
    for i in range(n):
        if s[i] == '0':
            if one:
                region.append(count)
                count = 1
                one = False
            else:
                count += 1
        else:
            if one:
                count += 1
            else:
                one = True
                region.append(count)
                count = 1
    region.append(count)
    if s[-1] == '0':
        region.append(0)

    # print(f'region: {region}')

    m = len(region)
    if m <= 2*k + 1:
        return n
    cum = [0] + list(accumulate(region))
    l = 1
    r = 2*k+1
    ans=0
    while r <= m:
        ans = max(ans, cum[r] - cum[l-1])
        l += 2
        r += 2
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,s=readinput()
    ans=solve(n,k,s)
    printans(ans)
