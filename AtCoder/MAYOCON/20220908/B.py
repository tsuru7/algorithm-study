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
    return n

def solve(n):
    k = len(str(n))
    count = [0, 0, 0]
    while n > 0:
        d = n % 10
        t = d % 3
        count[t] += 1
        n = n // 10
    ans=abs(count[1] - count[2]) % 3
    if ans == k:
        return -1
    else:
        return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
