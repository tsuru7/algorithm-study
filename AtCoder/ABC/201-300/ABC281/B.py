import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import Counter

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
    s = input()
    return s

def solve(s):
    n = len(s)
    if n != 8:
        return 'No'
    head = s[0]
    between = s[1:-1]
    counter = Counter(between)
    tmp = 0
    for c in '1234567890':
        tmp += counter[c]
    if tmp != 6:
        return 'No'
    tail = s[-1]
    if ord('A') <= ord(head) <= ord('Z') and 100000 <= int(between) <= 999999 and ord('A') <= ord(tail) <= ord('Z'):
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
