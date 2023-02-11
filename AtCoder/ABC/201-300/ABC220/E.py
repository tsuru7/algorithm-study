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
    n,d=m_input()
    return n,d

def f(n,d):
    if d == 0:
        return 0
    if d > (n-1)*2:
        return 0
    count = 0
    # rootを通るケース
    r = max(0, d - (n-1))
    for i in range(r, d+1):
        if i == 0 or i == d:
            count += f(n-1, d-1)
        else:
            count += f(n-1, i-1) * f(n-1, d-i-1)
    # rootを通らないケース
    count += f(n-1, d) * 2
    return count

def main(n,d):

    ans=f(n,d)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d=readinput()
    ans=main(n,d)
    printans(ans)
