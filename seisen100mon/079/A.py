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
    n,m,q=m_input()
    lrList = [l_input() for _ in range(m)]
    queries = [l_input() for _ in range(q)]
    return n,m,q,lrList,queries

def solve(n,m,q,lrList,queries):
    s = [set() for _ in range(n)]
    t = [set() for _ in range(n)]
    for idx, (l, r) in enumerate(lrList):
        l -= 1
        r -= 1
        s[l].add(idx)
        t[r].add(idx)
    scum = [set()]
    tcum = [set()]
    for i in range(n):
        scum.append(scum[-1].union(s[i]))
        tcum.append(tcum[-1].union(t[i]))
    # print(f'scum: {scum}')
    # print(f'tcum: {tcum}')
    ans=[]
    for p, q in queries:
        p -= 1
        q -= 1
        ans.append(len(tcum[q+1]-scum[p]))
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,q,lrList,queries=readinput()
    ans=solve(n,m,q,lrList,queries)
    printans(ans)
