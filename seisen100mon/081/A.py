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
    abList = [l_input() for _ in range(n)]
    return n,abList

def solve(n,abList):
    color = [0 for _ in range(10**6+2)]
    for a, b in abList:
        color[a] += 1
        color[b+1] -= 1
    for i in range(1, 10**6+1):
        color[i] += color[i-1]
    
    return max(color)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,abList=readinput()
    ans=solve(n,abList)
    printans(ans)
