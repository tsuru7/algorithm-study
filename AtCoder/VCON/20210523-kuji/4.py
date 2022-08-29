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
    n,x,m=m_input()
    return n,x,m

def main(n,x,m):
    if x == 0:
        return 0
    if x == 1:
        return n
    if n <= m:
        ans = 0
        a = x
        ans = a
        for i in range(1, n):
            a = a**2 % m
            ans += a
        return ans
    # n > m
    dist = [0]*(m+1)
    a = x
    dist[a] = 1
    for i in range(2, n+1):
        a = a**2 % m
        if dist[a] != 0:
            s = dist[a]
            l = i - s
            break
        dist[a] = i
    # loopが見つかった loop長 l
    # [s..s+l-1]がloopになっている
    # print(f'l: {l}, s: {s}, dist: {dist}')
    a = x
    acc1 = 0
    if s > 1:
        acc1 = a
        for i in range(2, s):
            a = a**2 % m
            acc1 += a
    acc2 = 0
    for i in range(s, s+l):
        a = a**2 % m
        acc2 += a
    q, r = divmod(n-s+1, l)
    acc2 *= q
    acc3 = 0
    for i in range(s, s+r):
        a = a**2 % m
        acc3 += a
    # print(f'acc1: {acc1}, acc2: {acc2}, acc3: {acc3}')
    return acc1 + acc2 + acc3

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,m=readinput()
    ans=main(n,x,m)
    printans(ans)
