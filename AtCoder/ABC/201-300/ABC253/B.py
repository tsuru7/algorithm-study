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
    smap = [ input() for _ in range(h) ]
    return h,w,smap

def solve(h,w,smap):
    found = 0
    point = []
    for row in range(h):
        for col in range(w):
            if smap[row][col] == 'o':
                point.append((row, col))
    row1, col1 = point[0]
    row2, col2 = point[1]

    ans= abs(row1-row2)+abs(col1-col2)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,smap=readinput()
    ans=solve(h,w,smap)
    printans(ans)
