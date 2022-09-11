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
    amap = [list(input()) for _ in range(h)]
    return h,w,amap

def solve(h,w,amap):
    ans = []
    for row in range(h):
        if amap[row].count('#') == 0:
            continue
        ans.append(amap[row])
    tmp = list(zip(*ans))
    ans = []
    for row in range(w):
        if tmp[row].count('#') == 0:
            continue
        ans.append(tmp[row])
    ans=list(zip(*ans))
    return ans

def printans(ans):
    for a in ans:
        print(''.join(a))

if __name__=='__main__':
    h,w,amap=readinput()
    ans=solve(h,w,amap)
    printans(ans)
