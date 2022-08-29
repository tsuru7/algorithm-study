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
    n,m=m_input()
    lr = []
    for _ in range(m):
        lr.append(l_input())
    return n,m,lr

def main(n,m,lr):
    lmax = 0
    rmin = n
    for l, r in lr:
        lmax = max(lmax, l)
        rmin = min(rmin, r)
    ans=max(0, rmin-lmax+1)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,lr=readinput()
    ans=main(n,m,lr)
    printans(ans)
