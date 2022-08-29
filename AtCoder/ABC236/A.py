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
    s = input()
    a,b=m_input()
    return s,a,b

def solve(s,a,b):
    t = ''
    n = len(s)
    for i in range(n):
        if i != a-1 and i != b-1:
            t += s[i]
        elif i == a-1:
            t += s[b-1]
        else:
            t += s[a-1]
    return t

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,a,b=readinput()
    ans=solve(s,a,b)
    printans(ans)
