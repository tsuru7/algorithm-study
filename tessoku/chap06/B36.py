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
    n,k=m_input()
    s = input()
    return n,k,s

def solve(n,k,s):
    count = 0
    for i in range(n):
        if s[i] == '1':
            count += 1
    if (count - k) % 2 == 1:
        return 'No'
    else:
        return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,s=readinput()
    ans=solve(n,k,s)
    printans(ans)
