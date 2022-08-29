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
    dist = [l_input() for _ in range(10)]
    amap = [l_input() for _ in range(h)]
    return h,w,dist,amap

def solve(h,w,dist,amap):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    ans=0
    for row in range(h):
        for col in range(w):
            aij = amap[row][col]
            if aij != -1 and aij != 1:
                ans += dist[aij][1]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,dist,amap=readinput()
    ans=solve(h,w,dist,amap)
    printans(ans)
