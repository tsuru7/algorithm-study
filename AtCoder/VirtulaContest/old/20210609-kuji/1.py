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
    n,s,d=m_input()
    xylist = []
    for _ in range(n):
        xylist.append(l_input())
    return n,s,d,xylist

def main(n,s,d,xylist):
    for x, y in xylist:
        if x < s and y > d:
            return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s,d,xylist=readinput()
    ans=main(n,s,d,xylist)
    printans(ans)
