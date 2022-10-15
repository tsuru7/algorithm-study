import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    a=l_input()
    return n,a

def judge(wj, a, n):
    '''
    重複を除いた持っている本のリスト a 
    wj 巻まで読めるか判定する
    '''
    read = bisect_right(a, wj) # 持っている本の中で読む冊数
    sell = n - read # 読まない本は売れる
    if wj - read <= sell//2: # 読みたい本のうち持っていない冊数が買える冊数以下か
        return True
    else:
        return False

def solve(n,a):

    seta = set(a)
    ndup = n - len(seta)
    a = list(seta)
    a.sort()

    ac = 0
    wa = n+1
    while wa - ac > 1:
        wj = (wa+ac)//2
        if judge(wj, a, n):
            ac = wj
        else:
            wa = wj

    return ac

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
