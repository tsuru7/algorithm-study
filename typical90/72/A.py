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
    h,w=m_input()
    cmap = [input() for _ in range(h)]
    return h,w,cmap

def dfs(row, col, used):
    h = len(used)
    w = len(used[0])
    ans = -1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= row+dr < h and 0 <= col+dc < w:
            if used[row+dr][col+dc] == 0:
                # 次のマスが始点だった
                ans = max(ans, used[row][col]+1)
                # print(f'loop found, loop len: {used[row][col]+1}')
            elif used[row+dr][col+dc] > 0:
                # 次のマスが始点以外の訪問済み、または山のマスだった
                continue
            elif used[row+dr][col+dc] < 0:
                # 次のマスが未訪問のマスだった
                used[row+dr][col+dc] = used[row][col] + 1
                ans = max(ans, dfs(row+dr, col+dc, used))
                used[row+dr][col+dc] = -1
    return ans


def solve(h,w,cmap):
    used = [[-1 for _ in range(w)] for _ in range(h)]
    for row in range(h):
        for col in range(w):
            if cmap[row][col] == '#':
                used[row][col] = INFTY
    raillen = -1
    for srow in range(h):
        for scol in range(w):
            if used[srow][scol] == INFTY:
                continue
            used[srow][scol] = 0
            raillen = max(raillen, dfs(srow, scol, used))
            used[srow][scol] = -1
    if raillen >= 3:
        return raillen
    else:
        return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,cmap=readinput()
    ans=solve(h,w,cmap)
    printans(ans)
