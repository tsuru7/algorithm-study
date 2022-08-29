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
    queries = [l_input() for _ in range(q)]
    return n,q,a,queries

def solve(n,q,a,queries):
    delta = [a[0]] + [a[i+1]-a[i] for i in range(n-1)]
    # print(f'delta: {delta}')

    fuben = 0
    for i in range(n-1):
        fuben += abs(delta[i+1])
    ans=[]
    for l,r,v in queries:
        l -= 1
        r -= 1
        if l > 0:
            fuben_l = abs(delta[l])
        delta[l] += v
        if l > 0:
            fuben += abs(delta[l]) - fuben_l

        if r+1 < n:
            fuben_r = abs(delta[r+1])
            delta[r+1] -= v
            fuben += abs(delta[r+1]) - fuben_r

        # print(f'delta: {delta}')

        ans.append(fuben)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=solve(n,q,a,queries)
    printans(ans)
