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

def solve(n):
    '''
    終わりから考える。
    最後の1回は出た目がそのままスコア⇒最後の1回の期待値は3.5 = f(1)
    最後から2回目についてはいくつの目の時、次に進むのが最適か
    　次に進むと期待値が3.5なので、出た目が3.5未満なら次へ進むのが最適
    　残り2回の期待値は 1 * 1/6 + 2 * 1/6 + 3* 1/6 + 3.5 * 3/6 = f(2)
    ,,,
    最後からi回目について
    　次に進むと期待値が f(i-1) なので出た目が f(i-1) 未満なら次に進むのが最適
    　tmp = 0
      for j in range(1, 7):
        tmp += j if j > f(i-1) else f(i-1)
      f(i) /= 6 
    '''
    dp = [0.0 for _ in range(n+1)]
    dp[1] = 3.5
    for i in range(2, n+1):
        for j in range(1, 7):
            dp[i] += j if j > dp[i-1] else dp[i-1]
        dp[i] /= 6.0

    return dp[n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
