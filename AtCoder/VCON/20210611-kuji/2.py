import sys
sys.setrecursionlimit(10**5)
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
    h,w,x,y=m_input()
    slist = []
    for _ in range(h):
        slist.append(input())
    return h,w,x,y,slist

def main(h,w,x,y,slist):
    x -= 1
    y -= 1
    row = x-1
    upper = 0
    while row >= 0:
        if slist[row][y] == '.':
            upper += 1
            row -= 1
        else:
            break
    row = x+1
    lower = 0
    while row < h:
        if slist[row][y] == '#':
            break
        lower += 1
        row += 1
    col = y-1
    left = 0
    while col >= 0:
        if slist[x][col] == '#':
            break
        left += 1
        col -= 1
    col = y+1
    right = 0
    while col < w:
        if slist[x][col] == '#':
            break
        right += 1
        col += 1
    ans = upper + lower + left + right + 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,x,y,slist=readinput()
    ans=main(h,w,x,y,slist)
    printans(ans)
