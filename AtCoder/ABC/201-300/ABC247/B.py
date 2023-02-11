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
    stlist = [input().split() for _ in range(n)]
    return n,stlist

def solve(n,stlist):
    for i in range(n):
        found_s = False
        found_t = False
        si, ti = stlist[i]
        for j in range(n):
            if j == i:
                continue
            sj, tj = stlist[j]
            if sj == si or tj == si:
                found_s = True
            if tj == ti or sj == ti:
                found_t = True
            if found_s and found_t:
                return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,stlist=readinput()
    ans=solve(n,stlist)
    printans(ans)
