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
    n,k=m_input()
    slist = []
    for _ in range(n):
        slist.append(input())
    return n,k,slist

def main(n,k,slist):
    slist.sort()
    
    ans=0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,slist=readinput()
    ans=main(n,k,slist)
    printans(ans)
