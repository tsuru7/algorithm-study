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
    x,y=m_input()
    return x,y

def main(x,y):
    ans=0
    if x == 1:
        ans += 300000
    elif x == 2:
        ans += 200000
    elif x == 3:
        ans += 100000
    if y == 1:
        ans += 300000
    elif y == 2:
        ans += 200000
    elif y == 3:
        ans += 100000
    if x == 1 and y == 1:
        ans += 400000
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,y=readinput()
    ans=main(x,y)
    printans(ans)
