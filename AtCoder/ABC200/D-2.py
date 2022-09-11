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
    return n,a

def solve(n,a):
    dp = [[0 for _ in range(200)] for _ in range(n+1)]
    p = [[set() for _ in range(200)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        ai = a[i]
        for j in range(200):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] = min(3, dp[i+1][j])
            dp[i+1][(j+ai)%200] += dp[i][j]
            dp[i+1][(j+ai)%200] = min(3, dp[i+1][(j+ai)%200])
            if dp[i][j] > 0:
                p[i+1][j].add(j)
                p[i+1][(j+ai)%200].add(i)

    print(*dp)

    for i in range(200):
        if i == 0:
            base = 1
        else:
            base = 0
        if dp[n][i] < 2 + base:
            continue

        # print(f'i: {i}, p: {p}')
        b = []
        m = n
        now = i
        prev = list(p[m][now])[base]
        print(f'prev: {prev}')
        while prev > 0:
            if prev != now:
                b.append(prev)
            now = prev
            m -= 1
            prev = list(p[m][now])[base]
        print(f'b: {b}')

        c = []
        now = n
        prev = list(p[now])[-1]
        while prev > 0:
            if prev != now:
                c.append(prev)
            now = prev
            prev = list(p[now])[-1]
        return (['Yes', [len(b)]+b[::-1], [len(c)]+c[::-1]])
            
    return ['No']

def printans(ans):
    if ans[0] == 'No':
        print('No')
    else:
        print('Yes')
        print(*ans[1])
        print(*ans[2])

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
