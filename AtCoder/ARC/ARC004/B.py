import sys
sys.setrecursionlimit(10**5)
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
    dlist = []
    for _ in range(n):
        dlist.append(i_input())
    return n,dlist

def main(n,dlist):
    dist_max = sum(dlist)
    dmax = max(dlist)
    rest = sum(dlist) - dmax
    dist_min = max(0, dmax-rest)
    return dist_max, dist_min

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,dlist=readinput()
    ans=main(n,dlist)
    printans(ans)
