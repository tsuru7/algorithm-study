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
    h,w,n,m=m_input()
    lamp = [l_input() for _ in range(n)]
    block = [l_input() for _ in range(m)]
    return h,w,n,m,lamp,block

def solve(h,w,n,m,lamp,block):
    light_map_yoko = [[0 for _ in range(w)] for _ in range(h)]
    light_map_tate = [[0 for _ in range(w)] for _ in range(h)]
    for c, d in block:
        c -= 1
        d -= 1
        light_map_yoko[c][d] = -INFTY
        light_map_tate[c][d] = -INFTY
    for a, b in lamp:
        a -= 1
        b -= 1
        if light_map_yoko[a][b] == 0:
            light_map_yoko[a][b] = 1
            for dc in [-1, 1]:
                col = b+dc
                while 0 <= col < w and light_map_yoko[a][col] == 0:
                    light_map_yoko[a][col] = 1
                    col += dc

        if light_map_tate[a][b] == 0:
            light_map_tate[a][b] = 1
            for dr in [-1, 1]:
                row = a + dr
                while 0 <= row < h and light_map_tate[row][b] == 0:
                    light_map_tate[row][b] = 1
                    row += dr

        

    ans=0
    for row in range(h):
        for col in range(w):
            if light_map_tate[row][col] + light_map_yoko[row][col] > 0:
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,n,m,lamp,block=readinput()
    ans=solve(h,w,n,m,lamp,block)
    printans(ans)
