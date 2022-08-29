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
    n,m=m_input()
    wagomu = [l_input() for _ in range(m)]
    return n,m,wagomu

def solve(n,m,wagomu):
    triangle = [[0 for i in range(j+1)] for j in range(n)]
    for a, b, x in wagomu:
        a -= 1
        b -= 1
        # print(f'a: {a}, b: {b}, x: {x}')
        triangle[a][b] += 1
        if b+1 <= a:
            triangle[a][b+1] -= 1
        if a+x+1 < n:
            triangle[a+x+1][b] -= 1
            if b+x+2 <= a+x+1:
                triangle[a+x+1][b+x+2] += 1
        if a+x+2 < n:
            triangle[a+x+2][b+1] += 1
            if b+x+2 <= a+x+2:
                triangle[a+x+2][b+x+2] -= 1
        # print(*triangle, sep='\n')
        # print()


    # 左 -> 右
    for i in range(n):
        for j in range(1, i+1):
            triangle[i][j] += triangle[i][j-1]
    # print('左 -> 右')
    # print(*triangle, sep='\n')
    # print()
    # 右上 -> 左下
    for i in range(n):
        for j in range(i):
            triangle[i][j] += triangle[i-1][j]
    # print('右上 -> 左下')
    # print(*triangle, sep='\n')
    # print()
    # 左上 -> 右下
    for i in range(n):
        for j in range(1, i+1):
            triangle[i][j] += triangle[i-1][j-1]

    # print('左上 -> 右下')
    # print(*triangle, sep='\n')

    count = 0
    for i in range(n):
        for j in range(i+1):
            if triangle[i][j] > 0:
                count += 1
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,wagomu=readinput()
    ans=solve(n,m,wagomu)
    printans(ans)
