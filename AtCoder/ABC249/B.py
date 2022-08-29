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
    low =  'abcdefghijklmnopqrstuvwxyz'
    high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counter = Counter(s)
    found_low = False
    found_high = False
    found_double = False
    for k,v in counter.items():
        if k in low:
            found_low = True
        elif k in high:
            found_high = True
        if v > 1:
            found_double = True
    # print(f'found_low: {found_low}, found_high: {found_high}, found_double: {found_double}')
    if found_low and found_high and not found_double:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
