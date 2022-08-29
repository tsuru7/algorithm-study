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
    queries = []
    n, w, d = m_input()
    while not (n == w == d == 0):
        psList = [l_input() for _ in range(n)]
        queries.append((n,w,d,psList))
        n, w, d = m_input()
    return queries

def solve(queries):
    ans=[]
    for n, w, d, psList in queries:
        cakes = [(w, d)]
        for p, s in psList:
            p -= 1
            w, d = cakes.pop(p)
            s %= (w+d)
            if s < w:
                w1 = s
                w2 = w - s
                d1 = d2 = d
            else:
                s -= w
                d1 = s
                d2 = d - s
                w1 = w2 = w
            if d1*w1 < d2*w2:
                cakes.append((w1, d1))
                cakes.append((w2, d2))
            else:
                cakes.append((w2, d2))
                cakes.append((w1, d1))
        ans.append(sorted([w*d for w, d in cakes]))
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    queries=readinput()
    ans=solve(queries)
    printans(ans)
