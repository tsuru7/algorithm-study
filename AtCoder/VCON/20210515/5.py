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
    k=i_input()
    return s,k

def main(s,k):

    if k <= len(s):
        if s[:k] == '1'*k:
            return '1'
    
    i = 0
    while i < len(s) and s[i] == '1':
        i += 1
    return s[i]

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,k=readinput()
    ans=main(s,k)
    printans(ans)
