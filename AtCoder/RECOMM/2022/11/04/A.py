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
    amap = [l_input() for _ in range(h)]
    return h,w,amap

def solve(h,w,amap):
    move = []
    for col in range(w):
        for row in range(h-1):
            if amap[row][col] % 2 == 1:
                amap[row][col] -= 1
                amap[row+1][col] += 1
                move.append([row+1, col+1, row+2, col+1])
    for col in range(w-1):
        if amap[h-1][col] % 2 == 1:
            amap[h-1][col] -= 1
            amap[h-1][col+1] += 1
            move.append([h, col+1, h, col+2])
    return [[len(move)]] + move

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    h,w,amap=readinput()
    ans=solve(h,w,amap)
    printans(ans)
