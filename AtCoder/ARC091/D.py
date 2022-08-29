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
    n,k=m_input()
    return n,k

def main(n,k):
    if k == 0:
        return n**2
    ans=0
    for b in range(k+1, n+1):
        q, r = divmod(n, b)
        m = b - k
        ans += q*m
        if r >= k:
            ans += r-k+1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    printans(ans)
