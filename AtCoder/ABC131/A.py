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
    pre = s[0]
    for i in range(1, 4):
        if s[i] == pre:
            return 'Bad'
        pre = s[i]
    return 'Good'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
