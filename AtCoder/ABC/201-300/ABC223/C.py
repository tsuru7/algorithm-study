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
    ab = []
    for _ in range(n):
        ab.append(l_input())
    return n,ab

def main(n,ab):
    p = 0
    l = 0
    r = n-1
    while r - l > 0:
        al, bl = ab[l]
        ar, br = ab[r]
        tl = al/bl
        tr = ar/br
        if tl == tr:
            t = tl
            l += 1
            r -= 1
        elif tl < tr:
            t = tl
            l += 1
            ab[r] = [ar - br*t, br]
        else:
            t = tr
            r -= 1
            ab[l] = [al - bl*t, bl]
        p += bl*t
    if l == r:
        al, bl = ab[l]
        p += al / 2.0
    return p

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,ab=readinput()
    ans=main(n,ab)
    printans(ans)
