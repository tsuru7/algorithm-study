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

def dfs(s, a, b):
    if a == 0 and b == 0:
        return [s]
    ans = []
    if a > 0:
        ans.append(dfs(s+'a', a-1, b))
    else:
        ans.append(s+'b'*b)
    if b > 0:
        ans.append(dfs(s+'b', a, b-1))
    else:
        ans.append(s+'a'*a)
    return ans

def solve(a,b,k):
    ans=dfs('', a, b)
    print(f'ans: {ans}')

    ans.sort()
    return ans[k-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,k=readinput()
    ans=solve(a,b,k)
    printans(ans)
