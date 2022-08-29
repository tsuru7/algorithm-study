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
    s = []
    for i in range(4):
        s.append(input())
    return s

def main(s):
    counter = Counter(s)
    if len(counter) == 4:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
