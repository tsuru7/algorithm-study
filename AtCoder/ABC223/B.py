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
    s = input()
    return s

def main(s):
    head = s
    tail = s
    for i in range(len(s)):
        if head > s:
            head = s
        if tail < s:
            tail = s
        s = s[1:]+s[0]
    return head, tail

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
