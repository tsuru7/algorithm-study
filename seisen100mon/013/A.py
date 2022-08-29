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
    r,c=m_input()
    smap = [ l_input() for _ in range(r) ]
    return r,c,smap

def solve(r,c,smap):
    ans = 0
    for bit in range(2**r):
        tmp = 0
        for col in range(c):
            count = 0
            for row in range(r):
                b = 1 << row
                if bit & b == b:
                    flip = 1
                else:
                    flip = 0
                count += smap[row][col] ^ flip
            tmp += max(count, r-count)
        ans = max(ans, tmp)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    r,c,smap=readinput()
    ans=solve(r,c,smap)
    printans(ans)
