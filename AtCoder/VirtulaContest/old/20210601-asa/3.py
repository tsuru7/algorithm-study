import sys
sys.setrecursionlimit(10**5)
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
    w,h,n=m_input()
    xyalist = []
    for _ in range(n):
        xyalist.append(l_input())
    return w,h,n,xyalist

def main(w,h,n,xyalist):
    upper = h
    lower = 0
    left = 0
    right = w
    for x, y, a in xyalist:
        if a == 1:
            left = max(left, x)
        elif a == 2:
            right = min(right, x)
        elif a == 3:
            lower = max(lower, y)
        elif a == 4:
            upper = min(upper, y)
    if upper < lower or right < left:
        return 0
    ans = (upper - lower) * (right - left)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    w,h,n,xyalist=readinput()
    ans=main(w,h,n,xyalist)
    printans(ans)
