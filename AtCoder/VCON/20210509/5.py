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
    n,m=m_input()
    a=l_input()
    return n,m,a

def main(n,m,a):
    sum = 0
    for i in range(n):
        sum += a[i]
    count = 0
    for i in range(n):
        if 4*m*a[i] >= sum:
            count += 1
    if count >= m:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    printans(ans)
