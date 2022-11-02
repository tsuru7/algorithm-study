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
    d = i_input()
    queries = [l_input() for _ in range(d)]
    return n,a,d,queries

def solve(n,a,d,queries):
    count = [[0 for _ in range(n+1)] for _ in range(101)]
    for i in range(1, n+1):
        ai = a[i-1]
        for j in range(1, 101):
            if j == ai:
                count[j][i] = count[j][i-1] + 1
            else:
                count[j][i] = count[j][i-1]

    ans=[]
    for l, r in queries:
        for j in range(1, 101)[::-1]:
            if count[j][n] - count[j][r] > 0 or count[j][l-1] > 0:
                ans.append(j)
                break
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,d,queries=readinput()
    ans=solve(n,a,d,queries)
    printans(ans)
