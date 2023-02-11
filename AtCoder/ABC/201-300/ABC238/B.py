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
    a=l_input()
    return n,a

def solve(n,a):
    kirikomi = [0]
    k = 0
    for i in range(n):
        k += a[i]
        k %= 360
        kirikomi.append(k)
    kirikomi.append(360)
    kirikomi = list(set(kirikomi))
    kirikomi.sort()
    ans = 0
    for i in range(1, len(kirikomi)):
        ans = max(ans, kirikomi[i] - kirikomi[i-1])
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
