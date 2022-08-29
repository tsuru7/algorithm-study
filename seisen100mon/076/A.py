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
    # cumsum = list(accumulate(a, initial=0))
    cumsum = [0]+list(accumulate(a))
    # print(f'cumsum: {cumsum}, len(cumsum): {len(cumsum)}')
    ans=[]
    for k in range(1, n+1):
        mx = 0
        l = 0
        r = l+k
        while r <= n:
            # print(f'l: {l}, r: {r}')
            mx = max(mx, cumsum[r]-cumsum[l])
            l += 1
            r += 1
        ans.append(mx)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
