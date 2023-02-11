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
    n = len(s)
    if n == 1:
        return 'Yes'
    elif n == 2:
        if s == 'oo':
            return 'No'
        else:
            return 'Yes'
    else:
        if s[:2] == 'xx':
            s = s[2:]
        elif s[0] == 'x':
            s = s[1:]
        count = 0
        while len(s) > 0:
            if count % 3 == 0:
                if s[0] != 'o':
                    return 'No'
            else:
                if s[0] != 'x':
                    return 'No'
            count += 1
            s = s[1:]
        return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
