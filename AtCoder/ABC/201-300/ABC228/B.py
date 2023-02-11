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
    n, x=m_input()
    a=l_input()
    return n,x,a

def main(n,x,a):
    x -= 1
    known = [False]*n
    ans=0
    known[x] = True
    ans = 1
    now = x
    # print(f'known: {known}, now: {now}')

    for i in range(n):
        next = a[now]-1
        if known[next]:
            break
        ans += 1
        now = next
        known[now] = True
        # print(f'known: {known}, now: {now}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,a=readinput()
    ans=main(n,x,a)
    printans(ans)
