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

def dfs(digits, n):
    """digitsとその派生文字列の中の753数の個数を返す再帰関数"""
    # print(f'digits: {digits}')
    if len(digits) > 0 and int(digits) > n:
        return 0
    ans = 0
    if '7' in digits and '5' in digits and '3' in digits:
        ans += 1
    for c in ['7', '5', '3']:
        ans += dfs(digits+c, n)
    return ans

def solve(n):
    digits = ''
    ans = dfs(digits, n)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
