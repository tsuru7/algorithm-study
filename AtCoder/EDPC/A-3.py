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
    h=l_input()
    return n,h

memo = None

def cost(i):
    global memo

    if memo[i] != INFTY:
        return memo[i]

    if i == 0:
        memo[0] = 0
        return memo[0]
    elif i == 1:
        memo[1] = cost(0)+abs(h[0]-h[1])
        return memo[1]
    # elif i == 2:
    #     return min(cost(0)+abs(h[0]-h[2]), cost(1)+abs(h[1]-h[2]))
    else:
        memo[i] = min(cost(i-1)+abs(h[i]-h[i-1]), cost(i-2)+abs(h[i]-h[i-2]))
        return memo[i]

def main(n,h):
    global memo
    memo = [INFTY]*n

    return cost(n-1)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,h=readinput()
    ans=main(n,h)
    printans(ans)
