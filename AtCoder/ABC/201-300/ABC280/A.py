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
    h,w=m_input()
    sList = [input() for _ in range(h)]
    return h,w,sList

def solve(h,w,sList):
    ans=0
    for row in range(h):
        for col in range(w):
            if sList[row][col] == '#':
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,sList=readinput()
    ans=solve(h,w,sList)
    printans(ans)
