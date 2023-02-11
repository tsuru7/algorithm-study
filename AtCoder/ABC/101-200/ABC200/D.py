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
    a=l_input()
    return n,a

def main(n,a):
    dp = [[0]*200 for _ in range(n)]
    memo = []
    dp[0][a[0]%200] = 1
    for i in range(1, n):
        r = a[i-1] % 200
        for j in range(200):
            dp[i][j] += dp[i-1][j]
            dp[i][j] += ( dp[i-1][(j-r)%200] + 1)
            if dp[i][j] > 0:
                memo.append(i-1)
            if dp[i][j] >= 2:
                return ['Yes', memo, memo[:-1]]
        print(dp[i])
    return ['No']

def printans(ans):
    if ans[0] == 'No':
        print(ans[0])
    else:
        print(ans[0])
        print(len(ans[1]), ' '.join(map(str,ans[1])))
        print(len(ans[2]), ' '.join(map(str,ans[2])))

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
