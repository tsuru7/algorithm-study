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
    ans=1
    maxcount = 0
    for i in range(1, n+1):
        count = 0
        x = i
        while x > 0:
            if x % 2 == 0:
                count += 1
            x = x // 2
        if count > maxcount:
            maxcount = count
            ans = i
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
