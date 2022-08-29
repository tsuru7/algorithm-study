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
    p=l_input()
    return n,p

def main(n,p):
    count = 0
    for i in range(1, n+1):
        if i != p[i-1]:
            count += 1
    if count == 0 or count == 2:
        return 'YES'
    else:
        return 'NO'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    printans(ans)
