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
    amat = [l_input() for _ in range(h)]
    return h,w,amat

def solve(h,w,amat):
    tate = [0 for _ in range(w)]
    yoko = [0 for _ in range(h)]
    for row in range(h):
        yoko[row] = sum(amat[row])
    for col in range(w):
        tmp = 0
        for row in range(h):
            tmp += amat[row][col]
        tate[col] = tmp
    ans=[]
    for row in range(h):
        ans.append([yoko[row]+tate[col]-amat[row][col] for col in range(w)])
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    h,w,amat=readinput()
    ans=solve(h,w,amat)
    printans(ans)
