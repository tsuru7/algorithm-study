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
    count = 0
    facts = []
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        facts.append((2, count))
    p = 3
    x = n
    while p*p <= x:
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        if count > 0:
            facts.append((p, count))
        p += 2
    if n > 1:
        facts.append((n, 1))

    # print(f'facts: {facts}')

    count = 0
    for p, np in facts:
        count += np
    # print(f'count: {count}')

    ans=0
    while count > 1:
        if count % 2 == 1:
            count = count //2 + 1
        else:
            count = count //2
        ans += 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
