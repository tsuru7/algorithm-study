import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import deque
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
    n,m=m_input()
    alist = []
    for _ in range(m):
        alist.append(i_input())
    return n,m,alist

def main(n,m,alist):
    all = set(range(1, n+1))
    alist = alist[::-1]
    ans = []
    for a in alist:
        if a in all:
            ans.append(a)
            all.remove(a)
        # print(f'ans: {ans}, all: {all}')
    remains = list(all)
    remains.sort()
    for r in remains:
        ans.append(r)
    return ans

def main2(n,m,alist):
    hist = [0]*(n+1)
    for i in range(m):
        hist[alist[i]] = i+1
    updates = []
    remains = []
    for i in range(1, n+1):
        if hist[i] > 0:
            updates.append((hist[i], i))
        else:
            remains.append(i)
    updates.sort(reverse=True)
    ans = []
    for u in updates:
        ans.append(u[1])
    ans += remains

    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,m,alist=readinput()
    ans=main2(n,m,alist)
    printans(ans)
