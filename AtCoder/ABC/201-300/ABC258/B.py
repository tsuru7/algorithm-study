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
    n=i_input()
    amat = [ input() for _ in range(n) ]
    return n,amat

def solve(n,amat):
    ans=0
    for row in range(n):
        for col in range(n):
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                tmp = int(amat[row][col])
                r = row
                c = col
                for i in range(n-1):
                    r += dr
                    c += dc
                    if r < 0:
                        r += n
                    elif r >= n:
                        r -= n
                    if c < 0:
                        c += n
                    elif c >= n:
                        c -= n
                    tmp *= 10
                    # print(f'r: {r}, c: {c}')
                    tmp += int(amat[r][c])
                ans = max(ans, tmp)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,amat=readinput()
    ans=solve(n,amat)
    printans(ans)
