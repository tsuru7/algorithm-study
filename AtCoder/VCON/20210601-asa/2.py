import sys
sys.setrecursionlimit(10**5)
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
    tlist = []
    for _ in range(n):
        tlist.append(i_input())
    return n,tlist

def main(n,tlist):
    tlist.sort()
    ans=tlist[0]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,tlist=readinput()
    ans=main(n,tlist)
    printans(ans)
