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
    n,m=m_input()
    sList = [input() for _ in range(n)]
    return n,m,sList

def solve(n,m,sList):
    tList = []
    for i in range(n):
        tmp = 0
        for j in range(m):
            sij = sList[i][j]
            if sij == 'o':
                tmp |= 1<<j
        tList.append(tmp)
    ans=0
    for i in range(n):
        for j in range(i+1, n):
            if tList[i] | tList[j] == (1<<m)-1:
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,sList=readinput()
    ans=solve(n,m,sList)
    printans(ans)
