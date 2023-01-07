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
    a=l_input()
    q = i_input()
    queries = [i_input() for _ in range(q)]
    return n,a,q,queries

def solve(n,a,q,queries):
    a.sort()
    ans=[]
    for x in queries:
        ac = -1
        wa = n
        while wa - ac > 1:
            wj = (ac+wa)//2
            if a[wj] < x:
                ac = wj
            else:
                wa = wj
        ans.append(ac+1)
    
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,q,queries=readinput()
    ans=solve(n,a,q,queries)
    printans(ans)
