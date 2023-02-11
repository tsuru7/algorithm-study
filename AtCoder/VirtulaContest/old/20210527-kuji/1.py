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
    a=l_input()
    return a

def main(a):
    a1 = min(a)
    a3 = max(a)
    a2 = sum(a) - a1 - a3
    if a3-a2 == a2-a1:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a=readinput()
    ans=main(a)
    printans(ans)
