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
    return n

def judge(s):
    left = 0
    for c in s:
        if c == '(':
            left += 1
        else:
            left -= 1
        if left < 0:
            return False
    if left > 0:
        return False
    else:
        return True

def solve(n):
    ALL = 2**n
    candidates = []
    for x in range(ALL):
        s = ''
        for bit in range(n)[::-1]:
            b = 1<<bit
            if x & b == 0:
                s += '('
            else:
                s += ')'
        if judge(s):
            candidates.append(s)
    # candidates.sort()
    return candidates

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
