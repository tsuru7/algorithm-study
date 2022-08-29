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
    nlist = []
    n=i_input()
    while n > 0:
        nlist.append(n)
        n = i_input()
    return nlist

def solve():
    min2 = lambda x, y: x if x <= y else y

    # nmax = max()
    nmax = 10**6
    
    n = nmax
    dp = [INFTY]*(n+1)
    dp[0] = 0
    dpo = [INFTY]*(n+1)
    dpo[0] = 0

    i = 1
    w = i*(i+1)*(i+2)//6
    while w <= nmax:
        for j in range(n+1):
            if j-w >= 0:
                tmp = dp[j-w]+1
                if tmp < dp[j]:
                    dp[j] = tmp

        if w % 2 != 0:
            for j in range(n+1):
                if j-w >= 0:
                    tmp = dpo[j-w]+1
                    if tmp < dpo[j]:
                        dpo[j] = tmp

        i += 1
        w = i*(i+1)*(i+2)//6

    ans=[]
    n = int(input())
    while n != 0:
        print(dp[n], dpo[n])
        n = int(input())
    return

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    # nlist=readinput()
    solve()
    # printans(ans)
