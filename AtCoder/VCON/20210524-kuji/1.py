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
    if s == 'SUN':
        return 7
    elif s == 'MON':
        return 6
    elif s == 'TUE':
        return 5
    elif s == 'WED':
        return 4
    elif s == 'THU':
        return 3
    elif s == 'FRI':
        return 2
    elif s == 'SAT':
        return 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
