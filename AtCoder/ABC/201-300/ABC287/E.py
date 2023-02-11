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
    sList = [input() for _ in range(n)]
    return n,sList

def solve(n,sList):
    MOD = 2147483647
    hashsets = [set() for _ in range(5*10**5+10)]
    ans = 0
    for i in range(n):
        si = sList[i]
        lens = len(si)
        h = 0
        for j in range(lens):
            h *= 100
            h += ord(si[j])-ord('a')
            h %= MOD
            if h in hashsets[j]:
                ans = max(ans, j)
            hashsets[j].add(h)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,sList=readinput()
    ans=solve(n,sList)
    printans(ans)
