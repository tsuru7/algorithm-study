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
    slist = []
    for _ in range(n):
        slist.append(input())
    return n,slist

def main(n,slist):
    counts = dict()
    max_count = 0
    max_s = ''
    for s in slist:
        if s not in counts:
            counts[s] = 1
        else:
            counts[s] += 1
        if max_count < counts[s]:
            max_count = counts[s]
            max_s = s
    
    ans=max_s
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,slist=readinput()
    ans=main(n,slist)
    printans(ans)
