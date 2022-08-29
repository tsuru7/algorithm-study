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
    n,k=m_input()
    a=l_input()
    return n,k,a

def main(n,k,a):
    cumsum = [ [0,0] for _ in range(n) ]
    cumsum[0] = [a[0], 0]
    for i in range(1, n):
        cumsum[i] = [cumsum[i-1][0] + a[i], i]
    cumsum.insert(0, [0, -1])
    cumsum.sort()
    # print(f'cumsum: {cumsum}')
    cumsum1 = [ cumsum[i][0] for i in range(len(cumsum)) ]
    cumsum2 = [ cumsum[i][1] for i in range(len(cumsum)) ]
    # print(f'cumsum1: {cumsum1}')
    # print(f'cumsum2: {cumsum2}')
    ans=0
    for i in range(n+1):
        rsum = cumsum1[i]
        i2 = cumsum2[i]
        # print(f'rsum+k: {rsum+k}')
        j1 = bisect_left(cumsum1, rsum+k)
        if j1 == len(cumsum1) or cumsum1[j1] != rsum+k:
            continue
        j2 = bisect_right(cumsum1, rsum+k) - 1
        # print(f'j1: {j1}, j2: {j2}')
        for j in range(j1, j2+1):
            if cumsum2[j] >= i2:
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    printans(ans)
