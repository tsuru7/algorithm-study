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
    result = [1]*(n+1)
    for i in range(1, n+1):
        j = i*2
        while j <= n:
            if result[j] == result[i]:
                result[j] += 1
            j += i
    return result[1:]

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
