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
    l=l_input()
    return l

def solve(l):
    counter = Counter(l)
    mc = counter.most_common(2)
    key1, cnt1 = mc[0]
    key2, cnt2 = mc[1]
    # print(f'mc: {mc}')
    if cnt1 == 3 and cnt2 == 2:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    l=readinput()
    ans=solve(l)
    printans(ans)
