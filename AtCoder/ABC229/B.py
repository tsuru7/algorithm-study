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
    a,b=m_input()
    return a,b

def main(a,b):
    astr = str(a)[::-1]
    bstr = str(b)[::-1]
    for i in range(min(len(astr), len(bstr))):
        ai = int(astr[i])
        bi = int(bstr[i])
        if ai + bi >= 10:
            return 'Hard'
    return 'Easy'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    printans(ans)
