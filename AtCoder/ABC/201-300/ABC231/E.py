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
    n,x=m_input()
    a=l_input()
    return n,x,a

def num_change(r, a):
    count = 0
    for ai in a[::-1]:
        if ai > r:
            continue
        count += r // ai
        r = r % ai
    return count

def main(n,x,a):
    # if x > a[n-1]:
    #     m = x // a[n-1] + 1
    #     r = num_change(m*a[n-1]-x, a)
    #     return m+r
    candidates = []
    for ai in a[::-1]:
        if ai >= x:
            m = 1
        else:
            m = x // ai
            if x % ai != 0:
                m += 1
        candidates.append(m+num_change(m*ai-x, a))
    print(f'candidates: {candidates}')
    return min(candidates)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,a=readinput()
    ans=main(n,x,a)
    printans(ans)
