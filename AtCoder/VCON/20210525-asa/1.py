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
    v,t,s,d=m_input()
    return v,t,s,d

def main(v,t,s,d):
    if v*t <= d <= v*s:
        return 'No'
    else:
        return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    v,t,s,d=readinput()
    ans=main(v,t,s,d)
    printans(ans)
