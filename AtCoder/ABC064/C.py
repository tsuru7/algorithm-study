import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def main(n,a):
    GRAY = 399
    BROWN = 799
    GREEN = 1199
    CYAN = 1599
    BLUE = 1999
    YELLOW = 2399
    ORANGE = 2799
    RED = 3199
    OTHERS = 4800
    hist = [0]*9
    for v in a:
        if v <= GRAY:
            hist[0] += 1
        elif v <= BROWN:
            hist[1] += 1
        elif v <= GREEN:
            hist[2] += 1
        elif v <= CYAN:
            hist[3] += 1
        elif v <= BLUE:
            hist[4] += 1
        elif v <= YELLOW:
            hist[5] += 1
        elif v <= ORANGE:
            hist[6] += 1
        elif v <= RED:
            hist[7] += 1
        else:
            hist[8] += 1
    colors = 0
    for i in range(8):
        if hist[i] > 0:
            colors += 1
    return (max(1, colors), colors+hist[8])

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
