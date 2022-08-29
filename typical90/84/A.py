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
    s = input()
    return n,s

def solve(n,s):
    cumo = [0 for _ in range(n+1)]
    cumx = [0 for _ in range(n+1)]
    for i in range(n):
        si = s[i]
        if si == 'o':
            cumo[i+1] = cumo[i] + 1
            cumx[i+1] = cumx[i]
        else:
            cumo[i+1] = cumo[i]
            cumx[i+1] = cumx[i] + 1
    ans=0
    for l in range(n):
        if s[l] == 'o':
            rmin = bisect_left(cumx, cumx[l]+1)
        else:
            rmin = bisect_left(cumo, cumo[l]+1)
        # print(f'l: {l}, rmin: {rmin}')
        ans += n+1-rmin

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
