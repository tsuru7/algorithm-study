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
    s1 = s[:2]
    s2 = s[2:]
    i1 = int(s1)
    i2 = int(s2)
    if 1 <= i1 <= 12 and 1 <= i2 <= 12:
        return 'AMBIGUOUS'
    elif 1 <= i1 <= 12:
        return 'MMYY'
    elif 1 <= i2 <= 12:
        return 'YYMM'
    else:
        return 'NA'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
