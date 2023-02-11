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
    l=l_input()
    return l

def solve(l):
    cards = [0 for _ in range(13)]
    for num in l:
        cards[num-1] += 1
    pair = False
    triple = False
    for i in range(13):
        if cards[i] == 2:
            pair = True
        elif cards[i] == 3:
            triple = True
    if pair and triple:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    l=readinput()
    ans=solve(l)
    printans(ans)
