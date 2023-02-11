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
    n,k=m_input()
    c=l_input()
    return n,k,c

def main(n,k,c):
    colors = defaultdict(int)
    count = 0
    for i in range(k):
        ci = c[i]
        if colors[ci] == 0:
            count += 1
        colors[ci] += 1
    ans = count
    # print(f'colors: {colors}')
    i = 1
    j = i + k
    # print(f'i: {i}, j: {j}')
    while j < n:
        cj = c[j]
        if colors[cj] == 0:
            count += 1
        colors[cj] += 1
        ci = c[i-1]
        colors[ci] -= 1
        if colors[ci] == 0:
            count -= 1
        ans = max(ans, count)
        i += 1
        j += 1
        # print(f'colors: {colors}')
        # print(f'j: {j}')

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,c=readinput()
    ans=main(n,k,c)
    printans(ans)
