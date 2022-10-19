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
    paper = [l_input() for _ in range(n)]
    return n,paper

def solve(n,paper):
    plane = [[0 for _ in range(1502)] for _ in range(1502)]
    for a, b, c, d in paper:
        plane[a][b] += 1
        plane[a][d] -= 1
        plane[c][b] -= 1
        plane[c][d] += 1
    for row in range(1501):
        for col in range(1500):
            plane[row][col+1] += plane[row][col]
    for col in range(1501):
        for row in range(1500):
            plane[row+1][col] += plane[row][col]
    
    # for row in range(10):
    #     print(*plane[row][:10])
    ans=0
    for row in range(1501):
        for col in range(1501):
            if plane[row][col] > 0:
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,paper=readinput()
    ans=solve(n,paper)
    printans(ans)
