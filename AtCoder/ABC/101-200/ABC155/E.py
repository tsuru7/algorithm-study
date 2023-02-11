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
    n=input()
    return n

def solve(n):
    l = len(n)
    pay = [0 for _ in range(l+1)]
    for i in range(l)[::-1]:
        di = int(n[i]) + pay[i+1]
        if di > 5:
            pay[i] += 1
            pay[i+1] -= 10 - di
        else:
            pay[i+1] += di

    print(f'pay: {pay}')
    ans=0
    maxabs = 0
    for i in range(l+1):
        ans += abs(pay[i])
        maxabs = max(maxabs, abs(pay[i]))
    print(f'maxabs: {maxabs}')
    return ans

def maisu(x):
    s = str(x)
    ans = 0
    for c in s:
        ans += int(c)
    return ans

def solve2(n):
    x = int(n)
    minmaisu = INFTY
    for d0 in range(2):
        for d1 in range(10):
            for d2 in range(10):
                for d3 in range(10):
                    for d4 in range(10):
                        for d5 in range(10):
                            for d6 in range(10):
                                y = d0*10**6+d1*10**5+d2*10**4+d3*10**3+d4*10**2+d5*10+d6
                                if y >= x:
                                    z = y - x
                                    if minmaisu > maisu(y)+maisu(z):
                                        minmaisu = maisu(y)+maisu(z)
                                        print(f'minmaisu: {minmaisu}, y: {y}, z: {z}')
    return minmaisu


def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)

    ans=solve2(n)
    printans(ans)