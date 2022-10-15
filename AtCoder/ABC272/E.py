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
    n,m=m_input()
    a=l_input()
    return n,m,a

def solve(n,m,a):
    count = dict()
    for i in range(n):
        ai = a[i]
        if ai >= 0:
            continue
        tmp = ((-ai)-1)//(i+1) + 1
        if tmp in count:
            count[tmp].add(ai)
        else:
            count[tmp] = {ai}
    
    ans=[]
    for i in range(1, m+1):
        if i not in count:
            ans.append(0)
        else:
            tmpset = set(range(len(count[i])+1))
            tmpset = tmpset - count[i]
            tmplist = list(tmpset)
            tmplist.sort()
            ans.append(tmplist[0])

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,a=readinput()
    ans=solve(n,m,a)
    printans(ans)
