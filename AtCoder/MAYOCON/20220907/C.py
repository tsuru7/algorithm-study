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
    n=i_input()
    h=l_input()
    return n,h

def solve(n,h):
    count = 0
    for height in range(1, max(h)+1)[::-1]:
        water = False
        for flower in range(n):
            if water == False and h[flower] == height:
                water = True
                count += 1
            elif water == True and h[flower] < height:
                water = False
            if water:
                h[flower] -= 1
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,h=readinput()
    ans=solve(n,h)
    printans(ans)
