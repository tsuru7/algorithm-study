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
    n,k=m_input()
    return n,k

def solve(n,k):
    tbl = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        tmp = 0
        x = i
        while x > 0:
            tmp += x % 10
            x //= 10
        tbl[i] = i-tmp
    dbl = [tbl]
    for i in range(1, 30):
        dbl.append([0 for _ in range(n+1)])
        for j in range(1, n+1):
            dbl[i][j] = dbl[i-1][dbl[i-1][j]]

    ans = []
    for i in range(1, n+1):
        now = i
        for j in range(30)[::-1]:
            if k & (1<<j) > 0:
                now = dbl[j][now]
        ans.append(now)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
