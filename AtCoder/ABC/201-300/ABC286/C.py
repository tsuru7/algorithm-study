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
    n,a,b=m_input()
    s=input()
    return n,a,b,s

def solve(n,a,b,s):
    ss = s+s
    ans=INFTY
    for i in range(n):
        head = i
        tail = n -1 + i
        count = 0
        while tail >= head:
            if ss[head] != ss[tail]:
                count += 1
            head += 1
            tail -= 1
        ans = min(ans, i*a + count*b)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,s=readinput()
    ans=solve(n,a,b,s)
    printans(ans)
