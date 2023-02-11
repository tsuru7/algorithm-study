import sys
sys.setrecursionlimit(10**8)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    h,w,a,b=m_input()
    return h,w,a,b

def canPlaceB(row, col, room):
    if room[row][col] == 0:
        return True
    else:
        return False

def canPlaceAh(row, col, room):
    w = len(room[0])
    if room[row][col] == 0 and col+1 < w and room[row][col+1] == 0:
        return True
    else:
        return False

def canPlaceAv(row, col, room):
    h = len(room)
    if room[row][col] == 0 and row+1 < h and room[row+1][col] == 0:
        return True
    else:
        return False

def nextPlace(room, row, col):
    '''
    (row, col): 現在の位置から次の空きスペースの場所を探して返す
    空きスペースがなければ (-1, -1) を返す
    '''
    h = len(room)
    w = len(room[0])

    for c in range(col+1, w):
        if room[row][c] == 0:
            return (row, c)
    for r in range(row+1, h):
        for c in range(w):
            if room[r][c] == 0:
                return (r, c)
    return (-1, -1)

def dfs(room, row, col, a, b):
    '''
    room: 現在の部屋の状態
    (row, col): 次に畳を置く場所
    a, b: 残りの畳の枚数
    現在の部屋の状態からスタートして、何通りの畳の置き方があるかを返す
    '''
    # 再帰の終了条件
    # 畳を置くスペースがなくなったら 1 通りを返す
    if row < 0 and col < 0:
        return 1

    ans = 0
    if b > 0 and canPlaceB(row, col, room):
        room[row][col] = 1
        nrow, ncol = nextPlace(room, row, col)
        ans += dfs(room, nrow, ncol, a, b-1)
        room[row][col] = 0
    if a > 0 and canPlaceAh(row, col, room):
        room[row][col] = 1
        room[row][col+1] = 1
        nrow, ncol = nextPlace(room, row, col)
        ans += dfs(room, nrow, ncol, a-1, b)
        room[row][col] = 0
        room[row][col+1] = 0
    if a > 0 and canPlaceAv(row, col, room):
        room[row][col] = 1
        room[row+1][col] = 1
        nrow, ncol = nextPlace(room, row, col)
        ans += dfs(room, nrow, ncol, a-1, b)
        room[row][col] = 0
        room[row+1][col] = 0
    return ans

def solve(h,w,a,b):
    room = [[0 for _ in range(w)] for _ in range(h)]

    return dfs(room, 0, 0, a, b)

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,a,b=readinput()
    ans=solve(h,w,a,b)
    printans(ans)
