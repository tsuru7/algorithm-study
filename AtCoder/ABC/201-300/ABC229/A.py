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
    s1 = input()
    s2 = input()
    return s1, s2

def main(s1, s2):
    if s1[0] == '#':
        if s1[1] == '#' or s2[0] == '#':
            return 'Yes'
        else:
            return 'No'
    elif s1[0] == '.':
        if s1[1] == '#' and s2[1] == '#':
            return 'Yes'
        elif s2[0] == '#' and s2[1] == '#':
            return 'Yes'
        else:
            return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s1, s2=readinput()
    ans=main(s1, s2)
    printans(ans)
