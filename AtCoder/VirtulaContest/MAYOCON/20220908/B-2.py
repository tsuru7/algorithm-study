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
    return n

def solve(n):
    keta = len(str(n))
    digit = [0 for _ in range(keta)]
    x = n
    for i in range(keta):
        digit[i] = x % 10
        x //= 10
    ALL = 2**keta
    for x in range(ALL-1):
        digit2 = digit.copy()
        count = 0
        for i in range(keta):
            b = 1<<i
            if x & b > 0:
                digit2[i] = 0
                count += 1
        if sum(digit2) % 3 == 0:
            return count

    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
