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
    n,m=m_input()
    amap = []
    for _ in range(n):
        amap.append(input())
    return n,m,amap

def main(n,m,amap):
    dp = []
    for _ in range(n):
        dp.append([INFTY]*m)
    nList = []
    for _ in range(11):
        nList.append([])
    for row in range(n):
        for col in range(m):
            box = amap[row][col]
            if box == 'S':
                idx = 0
            elif box == 'G':
                idx = 10
            else:
                idx = int(box)
            nList[idx].append((row, col))

    for idx in range(11):
        if len(nList[idx]) == 0:
            return -1
    
    row, col = nList[0][0]
    dp[row][col] = 0
    for idx in range(1, 11):
        for i, j in nList[idx]:
            for i0, j0 in nList[idx-1]:
                dp[i][j] = min(dp[i][j], dp[i0][j0] + abs(i-i0) + abs(j-j0))

    row, col = nList[10][0]
    ans=dp[row][col]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,amap=readinput()
    ans=main(n,m,amap)
    printans(ans)
