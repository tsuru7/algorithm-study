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
    H,W=m_input()
    h,w = m_input()
    return H,W,h,w

def main(H,W,h,w):
    ans=(H-h)*(W-w)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    H,W,h,w=readinput()
    ans=main(H,W,h,w)
    printans(ans)
