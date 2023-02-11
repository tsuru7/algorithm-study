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
    sList = [input() for _ in range(10)]
    return sList

def solve(sList):
    for a in range(1, 11):
        for b in range(a, 11):
            for c in range(1, 11):
                for d in range(c, 11):
                    s = ['' for _ in range(10)]
                    for i in range(1, 11):
                        if a <= i <= b:
                            s[i-1] = '.'*(c-1) + '#'*(d-c+1) + '.'*(10-d)
                        else:
                            s[i-1] = '.'*10
                    # if a == 1 and b == 10 and c == 1 and d == 10:
                    #     print()
                    #     print(*s, sep='\n')
                    match = True
                    for i in range(10):
                        if s[i] != sList[i]:
                            match = False
                            break
                    if match:
                        return [(a, b), (c, d)]

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    sList=readinput()
    ans=solve(sList)
    printans(ans)
