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
    n,t=m_input()
    abList = [l_input() for _ in range(n)]
    return n,t,abList

def solve(n,t,abList):
    abList.sort(key=lambda x: x[1])
    dp = [[-INFTY for _ in range(t+1)] for _ in range(n+1)]
    eat = [[set() for _ in range(t+1)] for _ in range(n+1)]
    dp[0][0] = 0
    # print(*eat)
    for i in range(n):
        ai, bi = abList[i]
        for j in range(t+1):
            # 時刻 j で i-1 番目の料理まで食べ終わっている状態
            # i番目の料理を食べない場合
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            eat[i+1][j] = eat[i][j].copy()
            # i番目の料理を食べる場合
            if j-ai >= 0:
                if dp[i+1][j] < dp[i][j-ai]+bi:
                    dp[i+1][j] = dp[i][j-ai]+bi
                    eat[i+1][j] = eat[i][j-ai].copy()
                    eat[i+1][j].add(i)

        # print(f'eat[i+1]: {eat[i+1]}')
    ans = max(dp[n])
    print(f'ans1: {ans}')
    ans2 = 0
    order = set()
    for j in range(t):
        if ans2 < dp[n][j]:
            ans2 = dp[n][j]
            order = eat[n][j]
    # print(f'order: {order}')
    for i in range(n)[::-1]:
        if i not in order:
            _, bi = abList[i]
            ans2 += bi
            break
            
    return max(ans, ans2)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,t,abList=readinput()
    ans=solve(n,t,abList)
    printans(ans)
