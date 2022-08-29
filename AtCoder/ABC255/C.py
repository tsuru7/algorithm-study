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
    x,a,d,n=m_input()
    return x,a,d,n

def solve(x,a,d,n):
    if d == 0:
        return abs(a-x)
    if d > 0:
        if x <= a:
            return a-x
        elif a+(n-1)*d <= x:
            return x - ( a+(n-1)*d )
        ac = 0
        wa = n
        while wa-ac > 1:
            wj = (ac+wa)//2
            if a+wj*d < x:
                ac = wj
            else:
                wa = wj
        return min(abs(x - (a+ac*d)), abs((a+wa*d)-x))
    if d < 0:
        if x <= a+(n-1)*d:
            return a+(n-1)*d - x
        elif x >= a:
            return x - a
        ac = 0
        wa = n
        while wa-ac > 1:
            wj = (wa+ac)//2
            if a+wj*d > x:
                ac = wj
            else:
                wa = wj
        return min( abs((a+ac*d) - x), abs(x - (a+wa*d)))

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,a,d,n=readinput()
    ans=solve(x,a,d,n)
    printans(ans)
