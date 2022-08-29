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
    n,m,l=m_input()
    p,q,r=m_input()
    return n,m,l,p,q,r

def main(n,m,l,p,q,r):
    ans = (n//p) * (m//q) * (l//r)
    ans = max(ans, (n//p) * (m//r) * (l//q))
    ans = max(ans, (n//r) * (m//p) * (l//q))
    ans = max(ans, (n//r) * (m//q) * (l//p))
    ans = max(ans, (n//q) * (m//r) * (l//p))
    ans = max(ans, (n//q) * (m//p) * (l//r))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,l,p,q,r=readinput()
    ans=main(n,m,l,p,q,r)
    printans(ans)
