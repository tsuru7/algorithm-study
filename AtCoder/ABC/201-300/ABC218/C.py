import sys
sys.setrecursionlimit(10**6)
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

def readinput():
    n=i_input()
    smap = deque()
    for _ in range(n):

        smap.append(deque(list(input())))
    tmap = deque()
    for _ in range(n):
        tmap.append(deque(list(input())))
    return n,smap,tmap

def rotate(mat):
    n = len(mat)
    ans = deque()
    for _ in range(n):
        ans.append(deque(['']*n))

    # print(f'ans: {ans}')
    # print(f'mat: {mat}')

    for row in range(n):
        for col in range(n):
            # print(f'col: {col}, row: {row}, n-1-row: {n-1-row}')
            ans[col][n-1-row] = mat[row][col]
    # print(f'ans(ret): {ans}')
    return ans

def shift(mat):
    n = len(mat)
    mat1 = mat.copy()
    count = 0
    while count < n:
        if mat1[0] != deque(['.']*n):
            break
        tmp = mat1.popleft()
        mat1.append(tmp)
        count += 1
    mat2 = rotate(mat1)

    # print('mat2')
    # printMat(mat2)

    count = 0
    while count < n:
        if mat2[0] != deque(['.']*n):
            break
        tmp = mat2.popleft()
        mat2.append(tmp)
        count += 1
    return mat2

def printMat(mat):
    print('-'*10)
    n = len(mat)
    for i in range(n):
        s = ''.join(mat[i])
        print(s)
    print()


def isEqual(smap, tmap):
    n = len(smap)
    for i in range(n):
        for j in range(n):
            if smap[i][j] != tmap[i][j]:
                return False
    return True

def main(n,smap,tmap):
    tmap = shift(tmap)
    # print('tmap(shift)')
    # printMat(tmap)
    for i in range(4):
        smap = shift(smap)
        # printMat(smap)
        if isEqual(smap, tmap):
            return 'Yes'
        # smap = rotate(smap)
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,smap,tmap=readinput()
    ans=main(n,smap,tmap)
    printans(ans)
