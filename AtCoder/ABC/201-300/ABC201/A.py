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
    a1,a2,a3=m_input()
    return a1,a2,a3

def main(a1,a2,a3):
    amin = min(a1, a2, a3)
    amax = max(a1, a2, a3)
    amid = a1+a2+a3-amin-amax
    if amax-amid == amid-amin:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a1,a2,a3=readinput()
    ans=main(a1,a2,a3)
    printans(ans)
