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
    return n

def main(n):
    a = [0]*(n+1)
    a[1] = 1
    for i in range(2, n+1):
        j = i
        if a[j] == 0:
            a[j] = 2
            value = 2
        else:
            value = a[j]
        value += 1
        j += i
        while j <= n:
            a[j] = max(value, a[j])
            j += i
    return a[1:]

def printans(ans):
    print(' '.join(map(str,ans)))

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
