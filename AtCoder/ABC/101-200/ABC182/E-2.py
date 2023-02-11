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
    light_map = [[0 for _ in range(w)] for _ in range(h)]
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for a, b in lamp:
        a -= 1
        b -= 1
        light_map[a][b] = 1
    for c, d in block:
        c -= 1
        d -= 1
        light_map[c][d] = -INFTY
    res_maps = []
    tmp_map = [[0 for _ in range(w)] for _ in range(h)]
    for row in range(h):
        light_on = 0
        for col in range(w):
            if light_map[row][col] == 1:
                light_on = 1
            elif light_map[row][col] == -INFTY:
                light_on = 0
            tmp_map[row][col] = light_on
    res_maps.append(tmp_map)

    tmp_map = [[0 for _ in range(w)] for _ in range(h)]
    for row in range(h):
        light_on = 0
        for col in range(w)[::-1]:
            if light_map[row][col] == 1:
                light_on = 1
            elif light_map[row][col] == -INFTY:
                light_on = 0
            tmp_map[row][col] = light_on
    res_maps.append(tmp_map)

    tmp_map = [[0 for _ in range(w)] for _ in range(h)]
    for col in range(w):
        light_on = 0
        for row in range(h):
            if light_map[row][col] == 1:
                light_on = 1
            elif light_map[row][col] == -INFTY:
                light_on = 0
            tmp_map[row][col] = light_on
    res_maps.append(tmp_map)

    tmp_map = [[0 for _ in range(w)] for _ in range(h)]
    for col in range(w):
        light_on = 0
        for row in range(h)[::-1]:
            if light_map[row][col] == 1:
                light_on = 1
            elif light_map[row][col] == -INFTY:
                light_on = 0
            tmp_map[row][col] = light_on
    res_maps.append(tmp_map)

    ans=0
    for row in range(h):
        for col in range(w):
            for i in range(4):
                if res_maps[i][row][col] > 0:
                    ans += 1
                    break

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,n,m,lamp,block=readinput()
    ans=solve(h,w,n,m,lamp,block)
    printans(ans)
