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
    n=i_input()
    return n

def judge_row(ac, wj):
    print(f'? {ac} {wj} 1 {n}')
    t = i_input()
    if wj - ac + 1 == t:
        return False
    else:
        return True

def judge_col(ac, wj):
    print(f'? 1 {n} {ac} {wj}')
    t = i_input()
    if wj - ac + 1 == t:
        return False
    else:
        return True

def solve(n):
    # ルークのいない行を特定する
    ac = 1
    wa = n
    while wa - ac > 0:
        wj = (ac+wa)//2
        if judge_row(ac, wj):
            # ac, wj間に答えがある
            wa = wj
        else:
            ac = wj+1
    row = ac
    ac = 1
    wa = n
    while wa - ac > 0:
        wj = (ac+wa)//2
        if judge_col(ac, wj):
            wa = wj
        else:
            ac = wj+1
    col = ac
    return (row, col)

def printans(ans):
    print(f'! {ans[0]} {ans[1]}')

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
