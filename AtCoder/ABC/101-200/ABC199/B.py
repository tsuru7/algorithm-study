import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    b=l_input()
    return n,a,b

def main(n,a,b):
    minx = 0
    maxx = INFTY
    for i in range(n):
        minx = max(minx, a[i])
        maxx = min(maxx, b[i])
    return max(0, maxx - minx + 1)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    printans(ans)
