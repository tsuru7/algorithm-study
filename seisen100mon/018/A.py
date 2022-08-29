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
    s = l_input()
    q = i_input()
    t = l_input()
    return n,s,q,t

def judge():
    return True

def solve(n,s,q,t):
    s.insert(0, -INFTY)
    s.append(INFTY)
    ans=0
    for ti in t:
        ac = 0
        wa = len(s)-1
        while wa - ac > 1:
            wj = (ac+wa)//2
            if s[wj] <= ti:
                ac = wj
            else:
                wa = wj
        if s[ac] == ti:
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s,q,t=readinput()
    ans=solve(n,s,q,t)
    printans(ans)
