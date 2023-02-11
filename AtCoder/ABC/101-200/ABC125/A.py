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
    a,b,t=m_input()
    return a,b,t

def main(a,b,t):
    ans=(t//a)*b
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,t=readinput()
    ans=main(a,b,t)
    printans(ans)
