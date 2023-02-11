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
    # find head part
    result = [0] * (m+1)
    a = x
    acc = a
    result[a] = 1
    loop = False
    for i in range(2, n+1):
        a = a**2 % m
        if result[a] != 0:
            loop = True
            s = result[a]
            l = i - s
            break
        acc += a
        result[a] = i
    if not loop:
        return acc
    
    if s == 1:
        head = 0
    else:
        a = x
        acc = a
        for i in range(2, s):
            a = a**2 % m
            acc += a
        head = acc
    
    q, r = divmod(n-s+1, l)
    a = x
    acc = a
    for i in range(2, s+l):
        a = a**2 % m
        acc += a
    body = (acc - head)*q

    if r == 0:
        tail = 0
    else:
        a = x
        acc = a
        for i in range(2, s+r):
            a = a**2 % m
            acc += a
        tail = acc - head
    # print(f'head: {head}, body: {body}, tail: {tail}')
    return head + body + tail

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,m=readinput()
    ans=main(n,x,m)
    printans(ans)
