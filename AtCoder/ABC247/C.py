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
    return n

memo_s = [ [] for _ in range(17) ]
def s(n):
    if n == 1:
        memo_s[1] = [1]
        return memo_s[1]
    if memo_s[n] == []:
        memo_s[n] = s(n-1) + [n] + s(n-1)
    return memo_s[n]

def solve(n):
    
    ans=s(n)
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
