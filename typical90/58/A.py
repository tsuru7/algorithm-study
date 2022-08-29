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
    n,k=m_input()
    return n,k

def func(x):
    xtmp = x
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    sum += xtmp
    return sum % 10**5

def solve(n,k):
    jmptbl = [-1 for _ in range(10**5)]
    order = []

    count = 0
    jmptbl[n] = count
    order.append(n)
    next = func(n)
    count += 1
    while jmptbl[next] < 0:
        jmptbl[next] = count
        order.append(next)
        next = func(next)
        count += 1
    head = jmptbl[next]
    loop = count - head

    if k <= head:
        return order[k]
    k -= head
    k %= loop
    return order[head+k]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
