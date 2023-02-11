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
    x1, y1, x2, y2=m_input()
    return x1, y1, x2, y2

def solve(x1, y1, x2, y2):
    set1 = set()
    set2 = set()
    for dx, dy in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
        set1.add((x1+dx, y1+dy))
        set2.add((x2+dx, y2+dy))
    if len(set1 & set2) != 0:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    x1, y1, x2, y2=readinput()
    ans=solve(x1, y1, x2, y2)
    printans(ans)
