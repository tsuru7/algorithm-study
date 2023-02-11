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
    x=i_input()
    return x

def main(x):
    if x < 4:
        return 1
    
    ans=0
    i = 2
    while i*i <= x:
        for p in range(2, 1000):
            y = i**p
            if y > x:
                break
            ans = max(ans, y)
        i += 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    x=readinput()
    ans=main(x)
    printans(ans)
