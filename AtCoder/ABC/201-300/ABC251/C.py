import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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
    stlist = []
    for _ in range(n):
        s, t = input().split()
        stlist.append((s, t))
    return n,stlist

def solve(n,stlist):
    ans=0
    best = 0
    done = set()
    for i, st in enumerate(stlist):
        s, t = st
        if s in done:
            continue
        if best < int(t):
            best = int(t)
            ans = i
        done.add(s)
    return ans+1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,stlist=readinput()
    ans=solve(n,stlist)
    printans(ans)
