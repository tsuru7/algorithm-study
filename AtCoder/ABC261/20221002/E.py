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
    n,c=m_input()
    taList = [l_input() for _ in range(n)]
    return n,c,taList

def solve(n,c,taList):
    xtbl0 = [[0 for _ in range(30)] for _ in range(n+1)]
    xtbl1 = [[1 for _ in range(30)] for _ in range(n+1)]
    for i in range(1, n+1):
        t, a = taList[i-1]
        for j in range(30):
            if t == 1:
                if a & 1<<j > 0:
                    xtbl0[i][j] = xtbl0[i-1][j] & 1
                    xtbl1[i][j] = xtbl1[i-1][j] & 1
                else:
                    xtbl0[i][j] = 0
                    xtbl1[i][j] = 0
            elif t == 2:
                if a & 1<<j > 0:
                    xtbl0[i][j] = 1
                    xtbl1[i][j] = 1
                else:
                    xtbl0[i][j] = xtbl0[i-1][j]
                    xtbl1[i][j] = xtbl1[i-1][j]
            else:
                if a & 1<<j > 0:
                    xtbl0[i][j] = xtbl0[i-1][j] ^ 1
                    xtbl1[i][j] = xtbl1[i-1][j] ^ 1
                else:
                    xtbl0[i][j] = xtbl0[i-1][j] ^ 0
                    xtbl1[i][j] = xtbl1[i-1][j] ^ 0

    x = c
    ans=[]
    for i in range(1, n+1):
        tmp = 0
        for j in range(30)[::-1]:
            tmp <<= 1
            if x & 1<<j > 0:
                tmp += xtbl1[i][j]
            else:
                tmp += xtbl0[i][j]
        ans.append(tmp)
        x = tmp

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,c,taList=readinput()
    ans=solve(n,c,taList)
    printans(ans)
