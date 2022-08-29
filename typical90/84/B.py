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
    s=input()
    return n,s

def solve(n,s):
    comp = []
    pre = s[0]
    count = 1
    for i in range(1, n):
        now = s[i]
        if now == pre:
            count += 1
        else:
            comp.append((pre, count))
            count = 1
        pre = now
    if count > 1:
        comp.append((pre, count))
    tmp = 0
    for _, count in comp:
        tmp += count*(count-1)//2
    ans = n*(n-1)//2 - tmp
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
