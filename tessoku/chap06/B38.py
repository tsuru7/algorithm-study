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
    s = input()
    return n,s

def solve(n,s):
    updown = [0 for _ in range(n)]
    for i in range(n-1):
        si = s[i]
        if si == 'A':
            updown[i+1] = updown[i] + 1
        else:
            updown[i+1] = updown[i] - 1
    updown2 = [(updown[i], i) for i in range(n)]
    updown2.sort()
    grass = [0 for _ in range(n)]
    for i in range(n):
        idx = updown2[i][1]
        if idx == 0:
            grass[idx] = max(grass[idx], grass[idx+1]+1)
        elif idx == n-1:
            grass[idx] = max(grass[idx], grass[idx-1]+1)
        else:
            grass[idx] = max(grass[idx], max(grass[idx-1], grass[idx+1])+1)
    # print(grass)
    return sum(grass)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
