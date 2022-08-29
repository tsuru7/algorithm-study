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
    queries = [ i_input() for _ in range(q) ]
    return n,q,queries

def solve(n,q,queries):
    ball = [ i for i in range(n+1) ]
    index = [ i for i in range(n+1) ]
    for x in queries:
        pos = index[x]
        if pos != n:
            r = ball[pos+1]
            ball[pos], ball[pos+1] = ball[pos+1], ball[pos]
            index[x] = pos+1
            index[r] = pos
        else:
            l = ball[pos-1]
            ball[pos], ball[pos-1] = ball[pos-1], ball[pos]
            index[x] = pos-1
            index[l] = pos
    return ball[1:]

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,q,queries=readinput()
    ans=solve(n,q,queries)
    printans(ans)
