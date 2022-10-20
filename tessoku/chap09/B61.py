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
    friends = [0 for _ in range(n+1)]
    for _ in range(m):
        a, b = m_input()
        friends[a] += 1
        friends[b] +=1
    return n,friends

def solve(n,friends):
    ans = 1
    nmax = friends[1]
    for i in range(2, n+1):
        if nmax < friends[i]:
            nmax = friends[i]
            ans = i
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,friends=readinput()
    ans=solve(n,friends)
    printans(ans)
