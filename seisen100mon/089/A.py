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
    l=l_input()
    return n,l

def solve(n,l):
    segment = []
    pre = l[0]
    length = 1
    for i in range(1, n):
        now = l[i]
        if now == pre:
            segment.append(length)
            length = 1
        else:
            length += 1
        pre = now
    else:
        segment.append(length)
    # print(f'segment: {segment}')
    if len(segment) < 3:
        return sum(segment)
    maxlen = 0
    for i in range(1, len(segment)-1):
        maxlen = max(maxlen, segment[i-1]+segment[i]+segment[i+1])
    return maxlen

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l=readinput()
    ans=solve(n,l)
    printans(ans)
