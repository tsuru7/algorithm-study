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
    b=l_input()
    return n,a,b

def solve(n,a,b):
    dp = [INFTY for _ in range(n)]
    dp[0] = 0
    for i in range(1, n):
        ai = a[i-1]
        dp[i] = min(dp[i], dp[i-1] + ai)
        if i-2 >= 0:
            bi = b[i-2]
            dp[i] = min(dp[i], dp[i-2] + bi)
    
    i = n-1
    ans=[i]
    while i > 0:
        ai = a[i-1]
        if dp[i-1] == dp[i] - ai:
            i = i-1
        else:
            i = i-2
        ans.append(i)
    ans = [x+1 for x in ans[::-1]]
    return ans

def printans(ans):
    print(len(ans))
    print(*ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=solve(n,a,b)
    printans(ans)
