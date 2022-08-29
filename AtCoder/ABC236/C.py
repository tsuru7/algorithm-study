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
    s = input().split()
    t = input().split()
    return n,m,s,t

def solve(n,m,s,t):
    ans=[]
    j = 0
    i = 0
    while j < m:
        while t[j] != s[i]:
            ans.append('No')
            i += 1
        ans.append('Yes')
        i += 1
        j += 1
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,s,t=readinput()
    ans=solve(n,m,s,t)
    printans(ans)
