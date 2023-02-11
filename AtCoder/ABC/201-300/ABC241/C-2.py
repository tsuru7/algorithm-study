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
    smap = [ input() for _ in range(n) ]
    return n, smap

def solve(n, smap):
    for row in range(n-5):
        for col in range(n-5):

            ru = 0
            rd = 0
            for i in range(6):
                tate = 0
                yoko = 0
                for j in range(6):
                    if smap[row+i][col+j] == '#':
                        yoko += 1
                    if smap[row+j][col+i] == '#':
                        tate += 1
                if yoko >= 4 or tate >= 4:
                    return 'Yes'
                if smap[row+i][col+i] == '#':
                    rd += 1
                if smap[row+5-i][col+i] == '#':
                    ru += 1
            if ru >= 4 or rd >= 4:
                return 'Yes'

    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n, smap=readinput()
    ans=solve(n, smap)
    printans(ans)
