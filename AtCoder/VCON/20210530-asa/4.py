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
    s=i_input()
    return s

def main(s):
    x1 = 0
    x2 = 0
    x3 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    if s <= 10**9:
        x2 = s
        y1 = 1
    else:
        q, r = divmod(s, 10**9)
        if r == 0:
            x2 = 10**9
            y1 = q
        else:
            x2 = 10**9
            y1 = q+1
            x1 = 10**9 - r
            y2 = 1
    # print(x2*y1-x1*y2)
    return x1, y1, x2, y2, x3, y3

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
