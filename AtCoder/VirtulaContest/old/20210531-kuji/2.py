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
    # kuro shiro
    change = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == '0':
                continue
            else:
                change += 1
        else:
            if s[i] == '1':
                continue
            else:
                change += 1
    ans = change
    # shiro kuro
    change = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == '1':
                continue
            else:
                change += 1
        else:
            if s[i] == '0':
                continue
            else:
                change += 1
    ans=min(ans, change)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
