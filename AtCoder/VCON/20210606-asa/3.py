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
    n=i_input()
    x=l_input()
    return n,x

def main(n,x):
    ans=[]
    mid = n//2
    y = []
    for i in range(n):
        y.append((x[i],i))
    y.sort()
    mid1 = y[mid-1][0]
    mid2 = y[mid][0]
    ans = [0]*n
    for i in range(n):
        ix = y[i][1]
        if i < n//2:
            ans[ix] = mid2
        else:
            ans[ix] = mid1
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,x=readinput()
    ans=main(n,x)
    printans(ans)
