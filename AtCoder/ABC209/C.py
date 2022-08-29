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
    c=l_input()
    return n,c

def main(n,c):
    c.sort()
    MOD = 10**9+7
    ans=c[0]
    for i in range(1, n):
        ans = ( ans * ( max(0, c[i]-i) % MOD ) ) % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,c=readinput()
    ans=main(n,c)
    printans(ans)
