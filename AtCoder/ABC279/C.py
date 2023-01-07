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
    h,w=m_input()
    sList = [input() for _ in range(h)]
    tList = [input() for _ in range(h)]
    return h,w,sList,tList

def solve(h,w,sList,tList):
    ssList = list(map(list, zip(*sList[::-1])))
    ttList = list(map(list, zip(*tList[::-1])))
    ssList.sort()
    ttList.sort()
    for row in range(w):
        if ssList[row] == ttList[row]:
            continue
        else:
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,sList,tList=readinput()
    ans=solve(h,w,sList,tList)
    printans(ans)
