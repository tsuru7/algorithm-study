# ABC114-C
# https://atcoder.jp/contests/ABC114/tasks/ABC114_C

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

def check753(n):
    if str(n).count('3') > 0 and str(n).count('5') > 0 and str(n).count('7') > 0:
        return True
    else:
        return False

def dfs(now, n):
    '''
    nowを元にして1桁増やしたnow*10+3, now*10+5, now*10+7を生成する
    '''
    ans = 0
    if now > n:
        return 0
    if now == n:
        if check753(now):
            return 1
        else:
            return 0
    
    if check753(now):
        ans += 1
    for d in [3, 5, 7]:
        ans += dfs(now*10+d, n)
    return ans

def solve(n):
    '''
    Nは高々9桁なので、3**9=19683通りしかないので全探索
    条件を満たす数かどうかを判定して個数を数える
    1桁の数字から順に再帰的に構成してゆく
    '''
    ans=dfs(0, n)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
