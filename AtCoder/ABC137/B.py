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
    k,x=m_input()
    return k,x

def main(k,x):
    left = max(-1000000, x - (k-1))
    right = min(1000000, x + (k-1))
    ans=list(range(left, right+1))
    return ans

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__=='__main__':
    k,x=readinput()
    ans=main(k,x)
    printans(ans)
