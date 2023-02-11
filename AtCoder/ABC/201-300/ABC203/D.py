import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from statistics import median_low
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
    n,k=m_input()
    amap = []
    for _ in range(n):
        amap.append(l_input())
    return n,k,amap

def main(n,k,amap):
    ans=INFTY
    for row_offset in range(n-k+1):
        for col_offset in range(n-k+1):
            region = []
            for row in range(k):
                region += amap[row+row_offset][col_offset:col_offset+k]
            ans = min(ans, median_low(region))
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,amap=readinput()
    ans=main(n,k,amap)
    printans(ans)
