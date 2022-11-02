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
    ans=INFTY
    b = 0
    while b**3 <= n:
        ac = 10**6
        wa = -1
        while ac - wa > 1:
            wj = (ac + wa) // 2
            x = (wj + b)*(wj**2 + b**2)
            if x >= n:
                ac = wj
            else:
                wa = wj
        ans = min(ans, (ac+b)*(ac**2 + b**2))
        b += 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
