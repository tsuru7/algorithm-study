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
    bmat = [l_input() for _ in range(h)]
    return h,w,amat,bmat

def solve(h,w,amat,bmat):
    ans = 0
    for row in range(h-1):
        for col in range(w-1):
            d = bmat[row][col] - amat[row][col]
            for dr, dc in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                amat[row+dr][col+dc] += d
            ans += abs(d)

    for row in range(h):
        if amat[row] != bmat[row]:
            return ['No']
    return ['Yes', ans]

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    h,w,amat,bmat=readinput()
    ans=solve(h,w,amat,bmat)
    printans(ans)
