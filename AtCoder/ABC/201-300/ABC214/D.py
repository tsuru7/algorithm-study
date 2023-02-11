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
    uvList = []
    wList = []
    for _ in range(n-1):
        u, v, w = m_input()
        uvList.append([u,v])
        wList.append(w)
    return n,uvList,wList

def main(n,uvList,wList):
    wList.sort()
    ans=0
    for i, w in enumerate(wList):
        ans += w*(i+1)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,uvList,wList=readinput()
    ans=main(n,uvList,wList)
    printans(ans)
