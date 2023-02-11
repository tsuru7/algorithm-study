import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    ans=[]
    for i in range(1, n):
        l = 0
        while l+i < n and s[l] != s[l+i]:
            l += 1
        ans.append(l)
        
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
