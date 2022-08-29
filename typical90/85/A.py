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
    k=i_input()
    return k

def get_divisors(k):
    divisors = []
    i = 1
    while i*i <= k:
        if k % i == 0:
            q = k // i
            divisors.append(q)
            if q != i:
                divisors.append(i)
        i += 1
    return divisors

def solve(k):
    divisors = get_divisors(k)
    divisors.sort()
    ans=0
    for i in range(len(divisors)):
        b = divisors[i]
        for j in range(i+1):
            a = divisors[j]
            c, r = divmod(k,a*b)
            if r == 0 and c >= b:
                ans += 1
                # print(f'a: {a}, b: {b}, c: {c}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    k=readinput()
    ans=solve(k)
    printans(ans)
