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
    t = input()
    return s,t

def solve(s,t):
    for i in range(len(s)):
        if t[i] == s[i]:
            continue
        else:
            if i+1 == len(s):
                return 'No'
            else:
                if t[i+1] == s[i] and t[i] == s[i+1] and t[i+2:] == s[i+2:]:
                    return 'Yes'
                else:
                    return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,t=readinput()
    ans=solve(s,t)
    printans(ans)
