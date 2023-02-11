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
    a=l_input()
    return n,k,a

def solve(n,k,a):
    MOD = 10**9+7
    a.sort()
    # comb(k-2, k-2) 
    comb = [1]
    # comb(k-1, k-2), ..., comb(n-2, k-2)
    if k == 2:
        for x in range(k, n):
            comb.append(1)
    else:
        # comb(x, y)
        for x in range(k-1, n-1):
            y = k-2
            inv = pow(x-y, MOD-2, MOD)
            tmp = (comb[-1]*x*inv)%MOD
            comb.append(tmp)
    # print(f'comb: {comb}')
    cum = list(accumulate(comb))

    ans=0
    # max
    for i in range(k-1, n):
        ans += (a[i]*cum[i-(k-1)])%MOD
        ans %= MOD
        # print(f'i: {i}, i-(k-1): {i-(k-1)}, ans: {ans}')
    # min
    for i in range(n-k+1):
        ans -=(a[i]*cum[-(i+1)])%MOD
        ans %= MOD
        # print(f'i: {i}, ans: {ans}')

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
