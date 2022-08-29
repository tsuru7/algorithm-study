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
    lrlist = [ l_input() for _ in range(n) ]
    return n,lrlist

def solve(n,lrlist):
    hist = [0]*(2*10**5+1)
    for l, r in lrlist:
        hist[l] += 1
        hist[r] -= 1
    llist = []
    rlist = []
    count = 0
    flag = False
    for i in range(1, 2*10**5+1):
        count += hist[i]
        if count > 0:
            if not flag:
                llist.append(i)
                flag = True
        if count == 0:
            if flag:
                rlist.append(i)
                flag = False

    ans=[]
    for l, r in zip(llist, rlist):
        ans.append((l, r))
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,lrlist=readinput()
    ans=solve(n,lrlist)
    printans(ans)
