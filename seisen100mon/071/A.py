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
    n,q=m_input()
    a=l_input()
    c=l_input()
    return n,q,a,c

def solve(n,q,a,c):
    MOD = 10**9+7
    cum = [0 for _ in range(n)]
    for i in range(1, n):
        cum[i] = cum[i-1] + pow(a[i-1], a[i], MOD)
    # print(f'cum: {cum}')
    ans=0
    c.append(1)
    now = 0
    for i in range(q+1):
        next = c[i]-1
        ans += abs(cum[next]-cum[now])
        ans %= MOD
        # print(f'now: {now}, next: {next}, ans: {ans}')
        now = next
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,q,a,c=readinput()
    ans=solve(n,q,a,c)
    printans(ans)
