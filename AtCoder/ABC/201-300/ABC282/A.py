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
    k=i_input()
    return k

def solve(k):
    ans=''
    for i in range(k):
        ans += chr(ord('A')+i)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    k=readinput()
    ans=solve(k)
    printans(ans)
