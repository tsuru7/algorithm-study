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
    a=l_input()
    x=i_input()
    return n,a,x

def main(n,a,x):
    count = 0
    suma = sum(a)
    if x >= suma:
        count = (x // suma)*n
        x = x % suma
    for i in range(n):
        x -= a[i]
        count += 1
        if x < 0:
            break

    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,x=readinput()
    ans=main(n,a,x)
    printans(ans)
