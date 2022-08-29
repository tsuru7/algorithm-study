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
    bmat = []
    for _ in range(n):
        bmat.append(l_input())
    return n,m,bmat

def main(n,m,bmat):
    for row in range(n-1):
        if bmat[row+1][0] != bmat[row][0] + 7:
            return 'No'
        if (bmat[row][0]-1)//7 != (bmat[row][m-1]-1)//7:
            return 'No'
        for col in range(m-1):
            if bmat[row][col+1] != bmat[row][col] + 1:
                return 'No'
    row = n-1
    if (bmat[row][0]-1)//7 != (bmat[row][m-1]-1)//7:
        return 'No'
    for col in range(m-1):
        if bmat[row][col+1] != bmat[row][col] + 1:
            return 'No'

    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,bmat=readinput()
    ans=main(n,m,bmat)
    printans(ans)
