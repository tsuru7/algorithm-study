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
    amat = [ l_input() for _ in range(n) ]
    return n,m,amat

def solve(n,m,amat):
    ans=0
    for song1 in range(m):
        for song2 in range(song1+1, m):
            point = 0
            for stu in range(n):
                point += max(amat[stu][song1], amat[stu][song2])
            ans = max(ans, point)
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,amat=readinput()
    ans=solve(n,m,amat)
    printans(ans)
