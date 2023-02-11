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
    n,x=m_input()
    s = input()
    return n,x,s

def solve(n,x,s):
    x_bin = list(bin(x)[2:])
    for c in s:
        if c == 'U':
            x_bin.pop()
        elif c == 'L':
            x_bin.append('0')
        elif c == 'R':
            x_bin.append('1')
    return int('0b'+''.join(x_bin), base=2)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,s=readinput()
    ans=solve(n,x,s)
    printans(ans)
