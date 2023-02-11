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
    weak1 = s[0]*4
    now = s[0]
    weak2 = now
    for _ in range(3):
        if now == '9':
            next = '0'
        else:
            next = chr(ord(now)+1)
        weak2 += next
        now = next
    if s == weak1 or s == weak2:
        return 'Weak'
    else:
        return 'Strong'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
