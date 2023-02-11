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
    a,b,k=m_input()
    return a,b,k

memo = None
def dfs(a, b):
    global memo
    # print(f'a: {a}, b: {b}, memo[a][b]: {memo[a][b]}, len(memo[a][b]): {len(memo[a][b])}')
    if memo[a][b] is not None:
        return memo[a][b]

    ans = []
    if a == 0:
        ans.append('b'*b)
    else:
        for aa in dfs(a-1, b):
            ans.append('a'+aa)
    if b == 0:
        ans.append('a'*a)
    else:
        for bb in dfs(a, b-1):
            ans.append('b'+bb)
    # print(f'ans: {ans}')
    memo[a][b] = ans
    return ans

def solve(a,b,k):
    global memo
    memo = [[None for _ in range(b+1)] for _ in range(a+1)]
    ans = dfs(a, b)
    ans = list(set(ans))
    ans.sort()
    # print(f'ans: {ans}')
    return ans[k-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,k=readinput()
    ans=solve(a,b,k)
    printans(ans)
