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
    h,w,n,m=m_input()
    lamp = [l_input() for _ in range(n)]
    block = [l_input() for _ in range(m)]
    return h,w,lamp,block

def solve(h,w,lamp,block):
    map_1 = [[0 for _ in range(w)] for _ in range(h)]
    map_2 = [[0 for _ in range(w)] for _ in range(h)]
    map_3 = [[0 for _ in range(w)] for _ in range(h)]
    map_4 = [[0 for _ in range(w)] for _ in range(h)]
    for a, b in lamp:
        a -= 1
        b -= 1
        map_1[a][b] = 1
        map_2[a][b] = 1
        map_3[a][b] = 1
        map_4[a][b] = 1
    for c, d in block:
        c -= 1
        d -= 1
        map_1[c][d] = -INFTY
        map_2[c][d] = -INFTY
        map_3[c][d] = -INFTY
        map_4[c][d] = -INFTY
    for row in range(h):
        for col in range(w-1):
            if map_1[row][col] == 1 and map_1[row][col+1] == 0:
                map_1[row][col+1] = 1
        for col in range(1, w)[::-1]:
            if map_2[row][col] == 1 and map_2[row][col-1] == 0:
                map_2[row][col-1] = 1
    for col in range(w):
        for row in range(h-1):
            if map_3[row][col] == 1 and map_3[row+1][col] == 0:
                map_3[row+1][col] = 1
        for row in range(1, h)[::-1]:
            if map_4[row][col] == 1 and map_4[row-1][col] == 0:
                map_4[row-1][col] = 1
    
    ans=0
    for row in range(h):
        for col in range(w):
            if map_1[row][col] + map_2[row][col] + map_3[row][col] + map_4[row][col] > 0:
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,lamp,block=readinput()
    ans=solve(h,w,lamp,block)
    printans(ans)
