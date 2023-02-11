import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import Counter

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,m=m_input()
    a=l_input()
    return n,m,a

def main(n,m,a):
    arguments = Counter(a[:m])
    # i = 0 のときのmex()の引数に含まれる数
    contained = arguments.keys()
    # print(f'contained: {contained}')
    # contents = set(a[:m])
    others = set(list(range(n+2)))
    others = others - contained
    minvalue = min(list(others))
    # print(others, minvalue)

    # i が [1..n-m] のときの処理
    for i in range(1, n-m+1):
        # a[m+i-1]を対象範囲に入れる
        if a[m+i-1] in arguments:
            arguments[a[m+i-1]] += 1
        else:
            arguments[a[m+i-1]] = 1
            others.discard(a[m+i-1])
            minvalue = min(minvalue, min(list(others)))
        # a[i-1] を対象範囲から外す
        arguments[a[i-1]] -= 1
        if arguments[a[i-1]] == 0:
            del arguments[a[i-1]]
            others.add(a[i-1])
            minvalue = min(minvalue, min(list(others)))
        # print(others, minvalue)
    return minvalue


def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    printans(ans)
