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
    t = input()
    return s,t

def main(s,t):
    si = ord(s[0]) - ord('a')
    ti = ord(t[0]) - ord('a')
    if ti >= si:
        k = ti - si
    else:
        k = ti - si + 26
    for i in range(1, len(s)):
        si = ord(s[i]) - ord('a')
        ti = si + k
        if ti >= 26:
            ti -= 26
        if t[i] != chr(ti + ord('a')):
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    printans(ans)
