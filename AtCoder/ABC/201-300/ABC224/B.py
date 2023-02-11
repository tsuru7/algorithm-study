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
    amat = []
    for _ in range(h):
        amat.append(l_input())
    return h,w,amat

def main(h,w,amat):
    for i1 in range(h-1):
        for i2 in range(i1+1, h):
            for j1 in range(w-1):
                for j2 in range(j1+1, w):
                    if amat[i1][j1] + amat[i2][j2] > amat[i2][j1] + amat[i1][j2]:
                        return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,amat=readinput()
    ans=main(h,w,amat)
    printans(ans)
