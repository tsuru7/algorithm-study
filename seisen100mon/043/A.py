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
    smap = [ input() for _ in range(5) ]
    return n,smap

def solve(n,smap):
    cmap = [ [0]*3 for _ in range(n) ]
    for i in range(n):
        for j in range(5):
            if smap[j][i] == 'R':
                cmap[i][0] += 1
            elif smap[j][i] == 'B':
                cmap[i][1] += 1
            elif smap[j][i] == 'W':
                cmap[i][2] += 1
    
    dp = [ [INFTY]*3 for _ in range(n) ]
    for i in range(3):
        dp[0][i] = 5 - cmap[0][i]
    # print(f'cmap: {cmap}')
    for i in range(1, n):
        for j in range(3):
            for jj in range(3):
                if jj == j:
                    continue
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][jj])
            dp[i][j] += (5-cmap[i][j])
    # print(f'dp: {dp}')
    return min(dp[-1])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,smap=readinput()
    ans=solve(n,smap)
    printans(ans)
