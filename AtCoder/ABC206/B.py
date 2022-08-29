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
    n=i_input()
    return n

def main(n):
    sum = 0
    day = 0
    while sum < n:
        day += 1
        sum += day
    return day

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
