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
    x = input()
    n=i_input()
    slist = []
    for _ in range(n):
        slist.append(input())
    return x,n,slist

def main(x,n,slist):
    newdict = dict()
    newrev = dict()
    for i in range(26):
        newdict[x[i]] = i
        newrev[i] = x[i]
    tlist = []
    for s in slist:
        t = []
        for c in s:
            t.append(newdict[c])
        tlist.append(t)
    tlist.sort()
    ans=[]
    for t in tlist:
        s = ''
        for n in t:
            s += newrev[n]
        ans.append(s)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    x,n,slist=readinput()
    ans=main(x,n,slist)
    printans(ans)
