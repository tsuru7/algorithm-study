import sys
sys.setrecursionlimit(10**5)
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
    n,m=m_input()
    slist = []
    for _ in range(n):
        slist.append(input())
    return n,m,slist

def main(n,m,slist):
    n_even = 0 # 1の数が偶数箇所
    n_odd = 0
    for s in slist:
        counter = Counter(s)
        if counter['1'] % 2 == 0:
            n_even += 1
        else:
            n_odd += 1
    ans=n_even * n_odd
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,slist=readinput()
    ans=main(n,m,slist)
    printans(ans)
