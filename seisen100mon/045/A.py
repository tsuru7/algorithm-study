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
    queries = []
    n,m=m_input()
    while n != 0 or m != 0:
        clist = [i_input() for _ in range(m)]
        xlist = [i_input() for _ in range(n)]
        queries.append((clist, xlist))
        n,m=m_input()
    return queries

def solve(queries):
    ans = []
    for clist, xlist in queries:
        m = len(clist)
        n = len(xlist)
        dp = [ [INFTY]*m for _ in range(n) ]
        y = [ [0]*m for _ in range(n) ]
        jpres = [ [0]*m for _ in range(n) ]
        x1 = xlist[0]
        y0 = 128
        for j in range(m):
            cj = clist[j]
            y1 = y0 + cj
            if y1 > 255:
                y1 = 255
            if y1 < 0:
                y1 = 0
            dp[0][j] = (y1 - x1)**2
            y[0][j] = y1
        for i in range(1, n):
            xi = xlist[i]
            for j in range(m):
                cj = clist[j]
                dptmp = [0]*m
                ytmp = [0]*m
                for jpre in range(m):
                    spre = dp[i-1][jpre]
                    ypre = y[i-1][jpre]
                    yi = ypre + cj
                    if yi > 255:
                        yi = 255
                    if yi < 0:
                        yi = 0
                    stmp = spre + (yi-xi)**2
                    dptmp[jpre] = stmp
                    ytmp[jpre] = yi
                    # if stmp < dp[i][j]:
                    #     dp[i][j] = stmp
                    #     y[i][j] = yi
                stmp = INFTY
                for jpre in range(m):
                    if dptmp[jpre] < stmp:
                        stmp = dptmp[jpre]
                        jtmp = jpre
                # print(f'dptmp: {dptmp}')
                # print(f'ytmp: {ytmp}')
                dp[i][j] = dptmp[jtmp]
                y[i][j] = ytmp[jtmp]
                # print(f'i: {i}, j: {j}, jtmp: {jtmp}, dp[i][j]: {dp[i][j]}, y[i][j]: {y[i][j]}')
        # print(f'clist: {clist}')
        # print(f'dp: {dp}')
        # print(f'y: {y}')
        smin = INFTY
        for j in range(m):
            if dp[n-1][j] < smin:
                smin = dp[n-1][j]
        ans.append(smin)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    queries=readinput()
    ans=solve(queries)
    printans(ans)
