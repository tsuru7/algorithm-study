import sys
sys.setrecursionlimit(10**5)
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

def main(s):
    counter = Counter(s)
    if 'S' not in counter.keys() and 'N' in counter.keys():
        return 'No'
    if 'N' not in counter.keys() and 'S' in counter.keys():
        return 'No'
    if 'E' not in counter.keys() and 'W' in counter.keys():
        return 'No'
    if 'W' not in counter.keys() and 'E' in counter.keys():
        return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
