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
    n = input()
    k = i_input()
    return n,k

def solve(n,k):
    d = list(n)
    l = len(n)
    # dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(l+1)]
    dpeq = [[0 for _ in range(k+1)] for _ in range(l+1)]
    dpsm = [[0 for _ in range(k+1)] for _ in range(l+1)]
    dpeq[0][0] = 1
    for i in range(1, l+1):
        di = int(d[i-1])
        for j in range(k+1):
            # equal -> equal
            if di == 0:
                # di = 0
                if j > 0:
                    dpeq[i][j] += dpeq[i-1][j]
            else:
                # di > 0
                if j+1 <= k:
                    dpeq[i][j+1] += dpeq[i-1][j]
            # equal -> small
            if di == 0:
                # di = 0のケースはない
                pass
            else:
                # di > 0, 0 < ei < di
                if j+1 <= k:
                    dpsm[i][j+1] += dpeq[i-1][j]*(di-1)
                # di > 0, ei = 0
                # if j > 0:
                dpsm[i][j] += dpeq[i-1][j]
            # small -> small
            if j+1 <= k:
                dpsm[i][j+1] += dpsm[i-1][j]*9
            # if j > 0:
            dpsm[i][j] += dpsm[i-1][j]

    # print(f'dp: {dp}')

    return dpeq[l][k] + dpsm[l][k]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
