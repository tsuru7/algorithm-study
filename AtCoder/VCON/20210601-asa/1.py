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
    lucas = [0]*(86+1)
    lucas[0] = 2
    lucas[1] = 1
    for i in range(2, n+1):
        lucas[i] = lucas[i-1] + lucas[i-2]
    ans=lucas[n]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
