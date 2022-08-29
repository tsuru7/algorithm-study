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
    n,k=m_input()
    s=input()
    return n,k,s

def decode(x, n):
    ans = ''
    while x > 0:
        r = x % 26
        ans += chr(r+ord('a'))
        x //= 26
    ans = (ans+'a'*n)[:n]
    return ans[::-1]

def solve(n,k,s):
    dp = [[INFTY for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        si = s[i]
        for j in range(max(0, k+i-n), min(i+1, k)+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j-1]*26+ord(si)-ord('a'))


    return decode(dp[n][k], k)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,s=readinput()
    ans=solve(n,k,s)
    printans(ans)
