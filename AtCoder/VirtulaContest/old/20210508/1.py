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
    k=i_input()
    a,b=m_input()
    return k,a,b

def main(k,a,b):
    q, r = divmod(a, k)
    if q >= 1 and r == 0:
        return 'OK'
    q, r = divmod(b, k)
    if q >= 1 and r == 0:
        return 'OK'
    if b//k - a//k > 0:
        return 'OK'
    return 'NG'

def printans(ans):
    print(ans)

if __name__=='__main__':
    k,a,b=readinput()
    ans=main(k,a,b)
    printans(ans)
