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
    a=l_input()
    q=i_input()
    m=l_input()
    return n,a,q,m

def solve(n,a,q,m):
    acclist = [0]*2001
    for bit in range(2**n):
        acc = 0
        b = 1
        for i in range(n):
            if bit & b == b:
                acc += a[i]
            b <<= 1
        if acc <= 2000:
            acclist[acc] += 1
    ans=[]
    for mi in m:
        if acclist[mi] > 0:
            ans.append('yes')
        else:
            ans.append('no')
        
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,q,m=readinput()
    ans=solve(n,a,q,m)
    printans(ans)
