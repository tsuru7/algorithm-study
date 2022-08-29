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
    n,m=m_input()
    switches = [ l_input() for _ in range(m) ]
    p=l_input()
    return n,m,switches,p

def solve(n,m,switches,p):
    swmat = [ [0]*n for _ in range(m) ]
    for lamp, switch in enumerate(switches):
        for sw in switch[1:]:
            swmat[lamp][sw-1] = 1
    # print('swmat:')
    # print(*swmat, sep='\n')

    ans=0
    for bit in range(2**n):
        # print(f'bit: {("0"*n+bin(bit)[2:])[-n:]}')
        oncount = [0]*m
        b = 1
        for sw in range(n):
            if bit & b != b:
                b <<= 1
                continue
            for lamp in range(m):
                if swmat[lamp][sw] == 1:
                    oncount[lamp] += 1
            b <<= 1
        for lamp in range(m):
            if oncount[lamp] % 2 != p[lamp]:
                break
        else:
            ans += 1
        # print(f'oncount: {oncount}, p: {p}, ans: {ans}')
            

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,switches,p=readinput()
    ans=solve(n,m,switches,p)
    printans(ans)
