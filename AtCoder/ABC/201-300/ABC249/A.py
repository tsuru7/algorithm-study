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
    a,b,c,d,e,f,x=m_input()
    return a,b,c,d,e,f,x

def solve(a,b,c,d,e,f,x):
    dist_t = ( x // (a+c) ) * a*b
    x_r = x % (a+c)
    if x_r <= a:
        dist_t += x_r*b
    else:
        dist_t += a*b

    dist_a = ( x // (d+f) ) * d*e
    x_r = x % (d+f)
    if x_r <= d:
        dist_a += x_r*e
    else:
        dist_a += d*e

    if dist_t > dist_a:
        return 'Takahashi'
    elif dist_t < dist_a:
        return 'Aoki'
    else:
        return 'Draw'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,d,e,f,x=readinput()
    ans=solve(a,b,c,d,e,f,x)
    printans(ans)
