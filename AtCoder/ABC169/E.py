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
    if n % 2 == 1:
        abList.sort()
        min_med = abList[n//2][0]
        abList.sort(key=lambda x: x[1])
        max_med = abList[n//2][1]
        return max_med - min_med + 1
    else:
        abList.sort()
        min_med = abList[n//2-1][0] + abList[n//2][0]
        abList.sort(key=lambda x: x[1])
        max_med = abList[n//2-1][1] + abList[n//2][1]
        return max_med - min_med + 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,abList=readinput()
    ans=solve(n,abList)
    printans(ans)
