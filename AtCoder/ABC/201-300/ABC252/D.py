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
    multi = dict()
    for k, v in counter.items():
        if v > 1:
            multi[k] = v
    ncombi = 0
    for k, v in multi.items():
        ncombi += v*(v-1)//2
    
    # print(f'multi: {multi}, ncombi: {ncombi}')

    ans = 0
    for i in range(n):
        tmp = 0
        ai = a[i]
        counter[ai] -= 1
        tmp += (n-i-1-counter[ai])*(n-i-2-counter[ai])//2
        # print(f'tmp: {tmp}')
        if ai in multi:
            ncombi -= multi[ai]*(multi[ai]-1)//2
            multi[ai] -= 1
            ncombi += multi[ai]*(multi[ai]-1)//2
            if multi[ai] == 0:
                multi.pop(ai)
            # print(f'ncombi: {ncombi}')
        tmp -= ncombi
        if ai in multi:
            tmp += multi[ai]*(multi[ai]-1)//2
        # print(f'i: {i}, tmp: {tmp}')
        ans += tmp
    return ans

def solve2(n,a):
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    tmp += 1
        # print(f'i: {i}, tmp: {tmp}')
        ans += tmp
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
    # ans=solve2(n,a)
    # printans(ans)
