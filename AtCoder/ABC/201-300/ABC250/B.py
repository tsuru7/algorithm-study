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
    n,a,b=m_input()
    return n,a,b

def solve(n,a,b):
    smap = []
    for row_o in range(n):
        for row_i in range(a):
            color = 0
            s = ''
            for col_o in range(n):
                color = ( col_o + row_o ) % 2
                if color == 0:
                    s += '.'*b
                else:
                    s += '#'*b
            smap.append(s)
    return smap

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,a,b=readinput()
    ans=solve(n,a,b)
    printans(ans)
