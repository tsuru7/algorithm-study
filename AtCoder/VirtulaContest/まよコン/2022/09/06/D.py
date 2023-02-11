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
    s = [input() for _ in range(n)]
    t = [input() for _ in range(n)]
    return n,s,t

def shift(xx):
    x = xx.copy()
    n = len(x)
    upad = n
    lpad = n
    for row in range(n):
        col = 0
        while col < n and x[row][col] == '.':
            col += 1
        lpad = min(lpad, col)
    for col in range(n):
        row = 0
        while row < n and x[row][col] == '.':
            row += 1
        upad = min(upad, row)
    # print(f'upad: {upad}, lpad: {lpad}')
    x = x[upad:]
    for i in range(upad):
        x.append('.'*n)
    for row in range(n):
        x[row] = x[row][lpad:] + '.'*lpad
    return x

def rotate(x):
    y = []
    for col in range(n):
        tmp = ''
        for row in range(n)[::-1]:
            tmp += x[row][col]
        y.append(tmp)
    return y

def solve(n,s,t):
    s_shift = shift(s)
    # print('s_shift')
    # print(*s_shift, sep='\n')

    t_shift = shift(t)
    if t_shift == s_shift:
        return 'Yes'
    # L90
    t1 = rotate(t)
    t1_shift = shift(t1)
    if t1_shift == s_shift:
        return 'Yes'
    t2 = rotate(t1)
    t2_shift = shift(t2)
    if t2_shift == s_shift:
        return 'Yes'
    t3 = rotate(t2)
    t3_shift = shift(t3)
    if t3_shift == s_shift:
        return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s,t=readinput()
    ans=solve(n,s,t)
    printans(ans)
