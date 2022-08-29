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
    n,m=m_input()
    slist = []
    for _ in range(n):
        slist.append(input())
    return n,m,slist

def main(n,m,slist):
    even = 0
    odd = 0
    for s in slist:
        v = list(map(int, list(s)))
        if sum(v) % 2 == 0:
            even += 1
        else:
            odd += 1
    
    ans=even * odd
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,slist=readinput()
    ans=main(n,m,slist)
    printans(ans)
