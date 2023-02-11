import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
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
    movies = [l_input() for _ in range(n)]
    return n,movies

def solve(n,movies):
    movies.sort(key=lambda x: x[1])
    ans=0
    now = 0
    for l, r in movies:
        if l >= now:
            ans += 1
            now = r
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,movies=readinput()
    ans=solve(n,movies)
    printans(ans)
