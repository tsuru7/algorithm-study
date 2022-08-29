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
    diff = [a[0]]
    fuben = 0
    for i in range(1, n):
        diff.append(a[i]-a[i-1])
        fuben += abs(diff[-1])
    print(f'diff: {diff}')
    ans=[]
    for l, r, v in queries:
        l -= 1
        r -= 1
        if l > 0:
            fuben_l = abs(diff[l] - diff[l-1])
        else:
            fuben_l = 0
        if r+1 < n:
            fuben_r = abs(diff[r+1] - diff[r])
        else:
            fuben_r = 0
        fuben -= fuben_l+fuben_r

        diff[l] += v
        if l > 0:
            fuben += abs(diff[l]-diff[l-1])
        if r+1 < n:
            diff[r+1] -= v
            fuben += abs(diff[r+1]-diff[r])
        ans.append(fuben)
        print(f'diff: {diff}')
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=solve(n,q,a,queries)
    printans(ans)
