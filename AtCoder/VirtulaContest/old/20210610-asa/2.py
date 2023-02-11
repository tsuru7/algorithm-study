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
    s = input().split()
    return s

def main(s):
    ans=[]
    for word in s:
        if word == 'Left':
            ans.append('<')
        elif word == 'Right':
            ans.append('>')
        else:
            ans.append('A')  
    return ans

def printans(ans):
    print(' '.join(ans))

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
