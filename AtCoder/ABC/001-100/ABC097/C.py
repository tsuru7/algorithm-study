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
    s = input()
    k=i_input()
    return s,k

def solve(s,k):
    n = len(s)
    ansset = set()
    for i in range(n):
        for j in range(i, min(i+k, n)):
            ansset.add(s[i:j+1])
    anslist = list(ansset)
    anslist.sort()
    return anslist[k-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,k=readinput()
    ans=solve(s,k)
    printans(ans)
