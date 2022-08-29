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
    n,k=m_input()
    abList = [l_input() for _ in range(n)]
    return n,k,abList

def solve(n,k,abList):
    ab = []
    for i in range(n):
        a, b = abList[i]
        ab.append(a-b)
        ab.append(b)
    ab.sort(reverse=True)
    return sum(ab[:k])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,abList=readinput()
    ans=solve(n,k,abList)
    printans(ans)
