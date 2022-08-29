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
    l=i_input()
    return l

def main(l):
    upper = 1
    under = 1
    for i in range(1, 12):
        upper = upper * (l-i)
        under = under * (12-i)
    return upper // under

def printans(ans):
    print(ans)

if __name__=='__main__':
    l=readinput()
    ans=main(l)
    printans(ans)
