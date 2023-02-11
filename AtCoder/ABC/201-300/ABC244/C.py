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

def solve():
    n = i_input()
    ans_set = set(range(1, 2*n+2))
    takahashi = ans_set.pop()
    print(takahashi)
    while len(ans_set) > 0:
        aoki = i_input()
        ans_set.discard(aoki)
        takahashi = ans_set.pop()
        print(takahashi)
    return 

if __name__=='__main__':
    solve()
