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
    m,n=m_input()
    k=i_input()
    smap = [input() for _ in range(m)]
    areas = [l_input() for _ in range(k)]
    return n,m,k,smap,areas

def solve(n,m,k,smap,areas):
    cmap = [[[0,0,0] for col in range(n+1)] for row in range(m+1)]
    for row in range(m):
        for col in range(n):
            c = smap[row][col]
            if c == 'J':
                cmap[row+1][col+1][0] = cmap[row+1][col][0]+1
                cmap[row+1][col+1][1] = cmap[row+1][col][1]
                cmap[row+1][col+1][2] = cmap[row+1][col][2]
            elif c == 'O':
                cmap[row+1][col+1][0] = cmap[row+1][col][0]
                cmap[row+1][col+1][1] = cmap[row+1][col][1]+1
                cmap[row+1][col+1][2] = cmap[row+1][col][2]
            else:
                cmap[row+1][col+1][0] = cmap[row+1][col][0]
                cmap[row+1][col+1][1] = cmap[row+1][col][1]
                cmap[row+1][col+1][2] = cmap[row+1][col][2]+1
    for row in range(m):
        for col in range(n):
            for i in range(3):
                cmap[row+1][col+1][i] += cmap[row][col+1][i]
    ans=[]
    for a, b, c, d in areas:
        tmp = [0,0,0]
        for i in range(3):
            tmp[i] += cmap[c][d][i]-cmap[a-1][d][i]-cmap[c][b-1][i]+cmap[a-1][b-1][i]
        ans.append(tmp)
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,m,k,smap,areas=readinput()
    ans=solve(n,m,k,smap,areas)
    printans(ans)
