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
    nxlist = []
    n, x = m_input()
    while n != 0 or x != 0:
        nxlist.append([n, x])
        n, x = m_input()
    return nxlist

def solve(nxlist):
    ans = []
    for n, x in nxlist:
        count = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                k = x - (i + j)
                if k > j and k <= n:
                    count += 1
        ans.append(count)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    nxlist=readinput()
    ans=solve(nxlist)
    printans(ans)
