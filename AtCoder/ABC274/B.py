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
    cmap = [input() for _ in range(h)]
    return h,w,cmap

def solve(h,w,cmap):
    ans=[]
    for col in range(w):
        tmp = 0
        for row in range(h):
            if cmap[row][col] == '#':
                tmp += 1
        ans.append(tmp)
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    h,w,cmap=readinput()
    ans=solve(h,w,cmap)
    printans(ans)
