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
    s, t, x=m_input()
    return s, t, x

def main(s, t, x):
    if s < t:
        if s <= x and x <= t-1:
            return 'Yes'
        else:
            return 'No'
    else:
        if s <= x or x <= t-1:
            return 'Yes'
        else:
            return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s, t, x=readinput()
    ans=main(s, t, x)
    printans(ans)
