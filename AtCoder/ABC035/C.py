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
    n,q=m_input()
    lr = []
    for _ in range(q):
        lr.append(l_input())
    return n,q,lr

def main(n,q,lr):
    flips_start = [0]*n
    flips_end = [0]*n
    for l, r in lr:
        l -= 1
        r -= 1
        flips_start[l] += 1
        flips_end[r] += 1
    flip_count = 0
    ans = ''
    for i in range(n):
        flip_count += flips_start[i]
        if flip_count % 2 == 0:
            ans += '0'
        else:
            ans += '1'
        flip_count -= flips_end[i]

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,q,lr=readinput()
    ans=main(n,q,lr)
    printans(ans)
