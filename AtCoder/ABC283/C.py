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
    return s

def solve(s):
    n = len(s)
    i = 0
    ans=0
    while i < n:
        if '1' <= s[i] <= '9':
            ans += 1
            i += 1
        else:
            if i+1 < n and s[i+1] == '0':
                ans += 1
                i += 2
            else:
                ans += 1
                i += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
