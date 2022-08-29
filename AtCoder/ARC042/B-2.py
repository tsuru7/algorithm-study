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
    x, y = m_input()
    n=i_input()
    xylist = []
    for _ in range(n):
        xylist.append(l_input())
    return n,x,y,xylist

def distance(x0, y0, x1, y1, x2, y2):
    c0 = complex(x0, y0)
    c1 = complex(x1, y1)
    c2 = complex(x2, y2)
    c0 = c0 - c1
    c2 = c2 - c1
    c0 = c0 / (c2/abs(c2))
    return abs(c0.imag)

def main(n,x,y,xylist):
    ans=INFTY
    x0 = x
    y0 = y
    x1, y1 = xylist[0]
    for i in range(1, n):
        x2, y2 = xylist[i]
        ans = min(ans, distance(x0, y0, x1, y1, x2, y2))
        x1, y1 = x2, y2
    else:
        x2, y2 = xylist[0]
        ans = min(ans, distance(x0, y0, x1, y1, x2, y2))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,xylist=readinput()
    ans=main(n,x,y,xylist)
    printans(ans)
