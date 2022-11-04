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
    h,w,m=m_input()
    bomb = [l_input() for _ in range(m)]
    return h,w,m,bomb

def solve(h,w,m,bomb):
    tate = [set() for _ in range(w)]
    yoko = [set() for _ in range(h)]
    tate_max = 0
    yoko_max = 0
    for i, (hi, wi) in enumerate(bomb):
        hi -= 1
        wi -= 1
        tate[wi].add(hi)
        yoko[hi].add(wi)
        tate_max = max(tate_max, len(tate[wi]))
        yoko_max = max(yoko_max, len(yoko[hi]))
    tate_max_idx = [wi for wi in range(w) if len(tate[wi]) == tate_max]
    yoko_max_idx = [hi for hi in range(h) if len(yoko[hi]) == yoko_max]

    ans=0
    for wi in tate_max_idx:
        for hi in yoko_max_idx:
            if wi in yoko[hi]:
                crossing = -1
            else:
                crossing = 0
            ans = max(ans, tate_max + yoko_max + crossing)
            if crossing == 0:
                return ans
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,m,bomb=readinput()
    ans=solve(h,w,m,bomb)
    printans(ans)
