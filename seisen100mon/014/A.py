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
    n,k=m_input()
    a=l_input()
    return n,k,a

def solve(n,k,a):
    ans=INFTY
    for bit in range(2**n):
        visible = 0
        cost = 0
        height = 0
        for i in range(n):
            if height < a[i]:
                visible += 1
                height = a[i]
                continue

            b = 1 << i
            if bit & b == b:
                cost += height+1 - a[i]
                height += 1
                visible += 1
        if visible >= k:
            ans = min(ans, cost)


    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
