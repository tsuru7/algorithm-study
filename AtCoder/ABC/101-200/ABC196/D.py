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
    h,w,a,b=m_input()
    return h,w,a,b

def findnext(row, col, used):
    h = len(used)
    w = len(used[0])
    # for c in range(col, w):
    #     if used[row][c] == ' ':
    #         return (row, c)
    # for r in range(row+1, h):
    #     for c in range(w):
    #         if used[r][c] == ' ':
    #             return (r, c)
    for r in range(h):
        for c in range(w):
            if used[r][c] == ' ':
                return (r, c)
    return (-1, -1)

def dfs(now, used, a, b):
    '''
    現在の敷き詰め状態がused、Aが残りa枚、Bが残りb枚のときに敷き詰める通り数を返す
    次の空きスペースは(row, col)
    '''
    h = len(used)
    w = len(used[0])
    row, col = now
    if row < 0 or col < 0:
        if a == 0 and b == 0:
            # print(*used, sep='\n')
            # print()
            return 1
        else:
            # print(*used, sep='\n')
            # print()
            return 0

    count = 0
    if a > 0:
        if row+1 < h and used[row+1][col] == ' ':
            used[row][col] = 'A'
            used[row+1][col] = '1'
            next = findnext(row, col, used)
            count += dfs(next, used, a-1, b)
            used[row][col] = ' '
            used[row+1][col] = ' '
        if col+1 < w and used[row][col+1] == ' ':
            used[row][col] = 'A'
            used[row][col+1] = '2'
            next = findnext(row, col, used)
            count += dfs(next, used, a-1, b)
            used[row][col] = ' '
            used[row][col+1] = ' '
    if b > 0:
        used[row][col] = 'B'
        next = findnext(row, col, used)
        count += dfs(next, used, a, b-1)
        used[row][col] = ' '

    return count



def solve(h,w,a,b):
    used = [[' ' for _ in range(w)] for _ in range(h)]
    # 左上から A縦、A横、Bを敷き詰めてゆき、敷き詰められる通り数をカウントする
    
    return dfs((0, 0), used, a, b)

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,a,b=readinput()
    ans=solve(h,w,a,b)
    printans(ans)
