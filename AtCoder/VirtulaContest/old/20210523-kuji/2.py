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
    mid = (n-1)//2
    s1 = s[:mid]
    s2 = s[mid+1:]
    r1 = s1[::-1]
    r2 = s2[::-1]
    r = s[::-1]
    if s1 == r1 and s2 == r2 and s == r:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
