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
    aMap = []
    for _ in range(n):
        aMap.append([False]*m)
    for i in range(n):
        l=l_input()
        k = l[0]
        for ii in range(k):
            j = l[ii+1]-1
            aMap[i][j] = True
    return n,m,aMap

def main(n,m,aMap):
    likes = [True]*m
    for i in range(n):
        for j in range(m):
            likes[j] = likes[j] and aMap[i][j]
    ans=0
    for i in range(m):
        if likes[i]:
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,aMap=readinput()
    ans=main(n,m,aMap)
    printans(ans)
