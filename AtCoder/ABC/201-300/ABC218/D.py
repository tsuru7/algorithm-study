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
    xyList = []
    for _ in range(n):
        xyList.append(l_input())
    return n,xyList

def main(n,xyList):
    xDict = dict()
    for x, y in xyList:
        # print(f'x: {x}, y: {y}, xDict: {xDict}')
        if x in xDict.keys():
            xDict[x].add(y)
        else:
            xDict[x] = {y}
    xList = list(xDict.keys())
    nx = len(xList)
    ans=0
    for i in range(nx-1):
        xi = xList[i]
        for j in range(i+1, nx):
            xj = xList[j]
            inter = xDict[xi] & xDict[xj]
            ans += len(inter)*(len(inter)-1)//2

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xyList=readinput()
    ans=main(n,xyList)
    printans(ans)
