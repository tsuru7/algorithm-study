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
    smap = [ input() for _ in range(n) ]
    return n,smap

def check_yoko(smap):
    n = len(smap)
    for row in range(n):
        cumsum = [0]*(n+1)
        cumsum[0] = 0
        for col in range(1, n+1):
            cumsum[col] = cumsum[col-1] + ( 1 if smap[row][col-1] == '#' else 0 )
        # print(f'cumsum: {cumsum}')
        left = 0
        right = 6
        while right <= n:
            if cumsum[right] - cumsum[left] >= 4:
                return True
            left += 1
            right += 1

    return False

def check_naname(smap):
    n = len(smap)
    for row in range(n-6):
        cumsum = [0]*(n-row+1)
        cumsum[0] = 0
        for col in range(1, n-row+1):
            cumsum[col] = cumsum[col-1] + ( 1 if smap[row+col-1][col-1] == '#' else 0 )
        left = 0
        right = 6
        while right <= n-row:
            if cumsum[right] - cumsum[left] >= 4:
                return True
            left += 1
            right += 1

    return False

def solve(n,smap):
    if check_yoko(smap):
        return 'Yes'
    if check_naname(smap):
        return 'Yes'
    tmap = [ x for x in zip(*smap) ]
    if check_naname(tmap):
        return 'Yes'
    
    smap = [ x for x in zip(*smap[::-1])]
    if check_yoko(smap):
        return 'Yes'
    if check_naname(smap):
        return 'Yes'
    tmap = [ x for x in zip(*smap) ]
    if check_naname(tmap):
        return 'Yes'

    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,smap=readinput()
    ans=solve(n,smap)
    printans(ans)
