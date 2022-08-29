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

def solve(s):
    n = len(s)
    t = s[::-1]
    if s == t:
        return 'Yes'
    
    tail_a = 0
    for i in range(n):
        if t[i] == 'a':
            tail_a += 1
        else:
            break
    head_a = 0
    for i in range(n):
        if s[i] == 'a':
            head_a += 1
        else:
            break
    if head_a >= tail_a:
        return 'No'
    
    add_a = 'a'*(tail_a - head_a)
    s = add_a + s
    t = t + add_a
    if s == t:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
