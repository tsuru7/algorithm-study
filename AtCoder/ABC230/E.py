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

def main(n):
    ans=0
    pairs1 = []
    pairs2 = []
    i = 1
    while i*i <= n:
        pairs1.append((i, n//i))
        if i != n//i:
            pairs2.append((n//i, i))
        i += 1
    pairs = pairs1 + pairs2[::-1]
    # pairs.sort()
    x, ax = pairs[0]
    ans += ax
    for i in range(1, len(pairs)):
        y, ay = pairs[i]
        x, ax = pairs[i-1]
        ans += ay*(y-x)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
