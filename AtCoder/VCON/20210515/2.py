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
    a,b,c=m_input()
    return a,b,c

def main(a,b,c):
    ph1 = min(a,b,c)
    ph2 = max(a,b,c)
    ph3 = a+b+c-ph1-ph2
    # print(ph1, ph2, ph3)
    if ph1 == 5 and ph2 == 7 and ph3 == 5:
        return 'YES'
    else:
        return 'NO'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c=readinput()
    ans=main(a,b,c)
    printans(ans)
