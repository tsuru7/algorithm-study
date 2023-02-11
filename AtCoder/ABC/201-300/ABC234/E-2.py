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
    x=i_input()
    return x

def check(x):
    n = len(str(x))
    if n == 1:
        return True
    y = x
    d1 = x % 10
    y //= 10
    d2 = y % 10
    dif = d2 - d1
    y //= 10
    d1 = d2
    while y > 0:
        d2 = y % 10
        if dif != d2 - d1:
            return False
        y //= 10
        d1 = d2
    return True

def solve(x):
    n = len(str(x))
    if n <= 7:
        y = x
        while not check(y):
            y += 1
        return y

    elif n >= 11:
        d = int(str(x)[0])
        y = int(str(d)*n)
        while y < x:
            d += 1
            y = int(str(d)*n)
        return y
    
    elif n == 10:
        candidates = []
        d = int(str(x)[0])
        while d <= 9:
            y = int(str(d)*n)
            candidates.append(y)
            d += 1
        candidates.append(9876543210)
        candidates.sort()
        for candidate in candidates:
            if candidate >= x:
                return candidate

    elif n == 9:
        candidates = []
        d = int(str(x)[0])
        while d <= 9:
            y = int(str(d)*n)
            candidates.append(y)
            d += 1
        candidates.append(987654321)
        candidates.append(876543210)
        candidates.append(123456789)
        candidates.sort()
        for candidate in candidates:
            if candidate >= x:
                return candidate
                
    else:
        # n == 8
        candidates = []
        d = int(str(x)[0])
        while d <= 9:
            y = int(str(d)*n)
            candidates.append(y)
            d += 1
        candidates.append(98765432)
        candidates.append(87654321)
        candidates.append(76543210)
        candidates.append(12345678)
        candidates.append(23456789)
        candidates.sort()
        for candidate in candidates:
            if candidate >= x:
                return candidate
                

def printans(ans):
    print(ans)

if __name__=='__main__':
    x=readinput()
    ans=solve(x)
    printans(ans)
