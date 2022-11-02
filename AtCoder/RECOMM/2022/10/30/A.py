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

def dfs(formula, rest):
    global candidate

    if len(rest) == 0:
        candidate.append(formula)
        return
    
    if len(formula) != 0 and formula[-1] != '+':
        dfs(formula + '+', rest)
    dfs(formula + rest[0], rest[1:])

    return

def evaluate(formula):
    nums = list(map(int, formula.split('+')))
    return sum(nums)

candidate = []
def solve(s):
    global candidate

    dfs('', s)
    # print(candidate)
    ans=0
    for formula in candidate:
        ans += evaluate(formula)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
