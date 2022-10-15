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
    even = []
    odd = []
    for i in range(n):
        if a[i] % 2 == 0:
            even.append(a[i])
        else:
            odd.append(a[i])
    ans=-1
    if len(even) >=2:
        even.sort(reverse=True)
        ans = max(ans, even[0]+even[1])
    if len(odd) >= 2:
        odd.sort(reverse=True)
        ans = max(ans, odd[0]+odd[1])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
