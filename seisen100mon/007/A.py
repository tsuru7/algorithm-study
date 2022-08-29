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
    pillars = [ l_input() for _ in range(n) ]
    return n,pillars

def isExist34(x1, y1, x2, y2, grid):
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x3 - dx
    y4 = y3 - dy
    if grid[x3][y3] == 1 and grid[x4][y4] == 1:
        return True
    
    x3 = x2 + dy
    y3 = y2 - dx
    x4 = x3 - dx
    y4 = y3 - dy
    if grid[x3][y3] == 1 and grid[x4][y4] == 1:
        return True

    return False

def isExist34_2(x1, y1, x2, y2, pillars_set):
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x3 - dx
    y4 = y3 - dy
    if encode(x3, y3) in pillars_set and encode(x4, y4) in pillars_set:
        return True
    
    x3 = x2 + dy
    y3 = y2 - dx
    x4 = x3 - dx
    y4 = y3 - dy
    if encode(x3, y3) in pillars_set and encode(x4, y4) in pillars_set:
        return True

    return False

def encode(x, y):
    # return ('00000'+str(x))[:5] + ('00000'+str(y))[:5]
    return x*10000+y

def solve(n,pillars):
    # grid = [ [0]*5001 for _ in range(5001) ]
    # for x, y in pillars:
    #     grid[x][y] = 1
    pillars_set = set()
    for x, y in pillars:
        pillars_set.add(encode(x, y))
        
    ans=0
    for i in range(n):
        x1, y1 = pillars[i]
        for j in range(i+1, n):
            x2, y2 = pillars[j]
            # if isExist34(x1, y1, x2, y2, grid):
            if isExist34_2(x1, y1, x2, y2, pillars_set):
                area = (x1-x2)**2+(y1-y2)**2
                ans = max(ans, area)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,pillars=readinput()
    ans=solve(n,pillars)
    printans(ans)
