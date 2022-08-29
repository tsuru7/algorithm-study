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
    xmap = []
    for _ in range(n):
        xmap.append(input())
    return n,xmap

def main(n,xmap):
    ans=0
    for col in range(9):
        keep = False
        for row in range(n):
            if xmap[row][col] == 'x':
                keep = False
                ans += 1
            elif xmap[row][col] == 'o':
                if not keep:
                    keep = True
                    ans += 1
            else:
                keep = False
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xmap=readinput()
    ans=main(n,xmap)
    printans(ans)
