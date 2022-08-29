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
    s = input()
    return n,s

def main(n,s):
    if s[n-1] ==  'o':
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    printans(ans)
