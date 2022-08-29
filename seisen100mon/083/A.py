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
    n,m=m_input()
    p=l_input()
    fare = [l_input() for _ in range(n-1)]
    return n,m,p,fare

def solve(n,m,p,fare):
    count = [0 for _ in range(n)]
    for i in range(1, m):
        now = p[i-1]-1
        next = p[i]-1
        if now > next:
            now, next = next, now
        # print(f'now: {now}, next: {next}')
        count[now] += 1
        count[next] -= 1
    
    # print(f'count: {count}')
    for i in range(1, n-1):
        count[i] += count[i-1]
    # print(f'count: {count}')
    ans=0
    for i in range(n-1):
        a, b, c = fare[i]
        ans += min(a*count[i], b*count[i]+c)
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,p,fare=readinput()
    ans=solve(n,m,p,fare)
    printans(ans)
