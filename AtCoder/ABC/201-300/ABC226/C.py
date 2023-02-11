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
    tkalist = []
    for _ in range(n):
        l = l_input()
        t = l[0]
        k = l[1]
        a = l[2:]
        tkalist.append([t,k,a])
    return n,tkalist

def main(n,tkalist):
    checked = set()
    unchecked = set()
    for a in tkalist[n-1][2]:
        unchecked.add(a)
    checked.add(n)
    while len(unchecked) > 0:
        # print(f'unchecked: {unchecked}, checked: {checked}')
        unchecked2 = set()
        for e in list(unchecked):
            if e in checked:
                continue
            for a in tkalist[e-1][2]:
                unchecked2.add(a)
            checked.add(e)
        unchecked = unchecked2
    
    ans=0
    for i in list(checked):
        ans += tkalist[i-1][0]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,tkalist=readinput()
    ans=main(n,tkalist)
    printans(ans)
