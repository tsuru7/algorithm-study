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
    n=i_input()
    slist = [input() for _ in range(n)]
    return n,slist

def solve(n,slist):
    tmp = dict()
    ans=[]
    for s in slist:
        if s in tmp:
            ans.append(s+'('+str(tmp[s])+')')
            tmp[s] += 1
        else:
            ans.append(s)
            tmp[s] = 1
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,slist=readinput()
    ans=solve(n,slist)
    printans(ans)
