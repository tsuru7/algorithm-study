import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    r,b=m_input()
    x,y=m_input()
    return r,b,x,y

# def judge(n, r, b, x, y):
#     if (y*n-b) % (y-1) == 0:
#         low = max(0, (y*n-b)//(y-1))
#     else:
#         low = max(0, (y*n-b)//(y-1) + 1)
#     high = min(n, (r-n)//(x-1))
#     return low <= high

def judge(n, r, b, x, y):
    # まず花束を n 個作るには r と b が n 本ずつ必ず必要
    r -= n
    b -= n
    if r < 0 or b < 0:
        return False
    # 残ったバラから赤を x-1 本取るか青を y-1 本取るたびに花束が作れる
    return r//(x-1) + b//(y-1) >= n

def main(r,b,x,y):
    ok = 0
    ng = 10**18+1
    while ng - ok > 1:
        now = (ok+ng)//2
        if judge(now, r, b, x, y):
            ok = now
        else:
            ng = now
    return ok

def printans(ans):
    print(ans)

if __name__=='__main__':
    r,b,x,y=readinput()
    ans=main(r,b,x,y)
    printans(ans)
