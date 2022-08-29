import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import deque

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
def print_masu(masu):
    for row in masu:
        printd(row)
    printd()

def readinput():
    h, w, n, m = m_input()
    ab = []
    for _ in range(n):
        ab.append(l_input())
    cd = []
    for _ in range(m):
        cd.append(l_input())
    return h,w,n,m,ab,cd

def main(h,w,n,m,ab,cd):
    tate = [[] for _ in range(w)]
    yoko = [[] for _ in range(h)]
    masu = [[0]*w for _ in range(h)]

    print_masu(masu)

    for col in range(w):
        tate[col].append((-1, 'B'))
        tate[col].append((h, 'B'))
    for row in range(h):
        yoko[row].append((-1, 'B'))
        yoko[row].append((w, 'B'))

    for a,b in ab:
        a -= 1
        b -= 1
        tate[b].append((a, 'L'))
        yoko[a].append((b, 'L'))
    for c,d in cd:
        c -= 1
        d -= 1
        tate[d].append((c, 'B'))
        yoko[c].append((d, 'B'))

    def get_xy(tate):
        return tate[0]
    def get_item(tate):
        return tate[1]

    for col in range(w):
        tate[col].sort()

        val = 0
        prev_y = get_xy(tate[col][0])
        prev_item = get_item(tate[col][0])
        for i in range(1, len(tate[col])-1):

            now_y = get_xy(tate[col][i])
            now_item = get_item(tate[col][i])

            if prev_item == 'L' or now_item == 'L':
                val = 1
            else:
                val = 0

            for row in range(prev_y+1, now_y):
                masu[row][col] += val
            if now_item == 'L':
                val = 1
            else:
                val = 0
            masu[now_y][col] = val

            prev_y = now_y
            prev_item = now_item

        for row in range(prev_y+1, h):
            masu[row][col] += val

    print_masu(masu)

    for row in range(h):
        yoko[row].sort()

        val = 0
        prev_x = get_xy(yoko[row][0])
        prev_item = get_item(yoko[row][0])
        for i in range(1, len(yoko[row])-1):

            now_x = get_xy(yoko[row][i])
            now_item = get_item(yoko[row][i])

            if prev_item == 'L' or now_item == 'L':
                val = 1
            else:
                val = 0

            for col in range(prev_x+1, now_x):
                masu[row][col] += val
            if now_item == 'L':
                val = 1
            else:
                val = 0
            masu[row][now_x] = val

            prev_x = now_x
            prev_item = now_item

        for col in range(prev_x+1, w):
            masu[row][col] += val

    print_masu(masu)
    
    ans = 0
    for row in range(h):
        for col in range(w):
            if masu[row][col] > 0:
                ans += 1
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,n,m,ab,cd=readinput()
    ans=main(h,w,n,m,ab,cd)
    printans(ans)
