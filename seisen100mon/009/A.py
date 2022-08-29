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
    m=i_input()
    objects = [ l_input() for _ in range(m) ]
    n = i_input()
    stars = [ l_input() for _ in range(n) ]
    return m,objects,n,stars

def encode(x, y):
    return x*10000000+y

def solve(m,objects,n,stars):
    starset = set()
    for x, y in stars:
        starset.add(encode(x, y))
    for i in range(n):
        dx = stars[i][0] - objects[0][0]
        dy = stars[i][1] - objects[0][1]
        for j in range(m):
            ox, oy = objects[j]
            if encode(ox+dx, oy+dy) not in starset:
                break
        else:
            # print(f'i: {i}, dx: {dx}, dy: {dy}')
            return (dx, dy)

def printans(ans):
    print(*ans)

if __name__=='__main__':
    m,objects,n,stars=readinput()
    ans=solve(m,objects,n,stars)
    printans(ans)
