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
    n=i_input()
    hlist = []
    for _ in range(n):
        hlist.append(i_input())
    return n,hlist

def main(n,hlist):
    diffs = [0]*(n-1)
    for i in range(1, n):
        if hlist[i-1] < hlist[i]:
            diffs[i-1] = 1
        elif hlist[i-1] > hlist[i]:
            diffs[i-1] = -1
        else:
            diffs[i-1] = 0
    count = 0
    ans = 0
    ascending = False
    decending = False
    for i in range(n-1):
        if diffs[i] == 0:
            ascending = False
            decending = False
            ans = max(ans, count)
        elif not ascending and not decending and diffs[i] > 0:
            ascending = True
            count = 1
        elif not ascending and not decending and diffs[i] < 0:
            decending = True
            count = 1
        elif ascending and diffs[i] > 0:
            count += 1
        elif decending and diffs[i] < 0:
            count += 1
        elif ascending and diffs[i] < 0:
            ascending = False
            decending = True
            count += 1
        elif decending and diffs[i] > 0:
            decending = False
            ascending = True
            ans = max(ans, count)
            count = 1
    ans = max(ans, count)
    return ans + 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,hlist=readinput()
    ans=main(n,hlist)
    printans(ans)
