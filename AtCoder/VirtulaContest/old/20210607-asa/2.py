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
    s = input()
    return s

def main(s):
    n = len(s)
    s = s.lower()
    i = 0
    while i < n and s[i] != 'i':
        i += 1
    else:
        if i == n:
            return 'NO'
    while i < n and s[i] != 'c':
        i += 1
    else:
        if i == n:
            return 'NO'
    while i < n and s[i] != 't':
        i += 1
    else:
        if i == n:
            return 'NO'
    return 'YES'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
