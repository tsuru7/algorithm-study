import sys
sys.setrecursionlimit(10**5)
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
    s, t = input().split()
    return n,s,t

def main(n,s,t):
    ans=''
    for i in range(n):
        ans += s[i]
        ans += t[i]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s,t=readinput()
    ans=main(n,s,t)
    printans(ans)
