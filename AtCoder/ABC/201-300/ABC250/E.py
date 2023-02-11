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
    a=l_input()
    b=l_input()
    q=i_input()
    queries = [ l_input() for _ in range(q) ]
    return n,a,b,q,queries

def solve(n,a,b,q,queries):
    cumnum_a = [0]*n
    cumnum_a[0] = 1
    cumnum_b = [0]*n
    cumnum_b[0] = 1
    tmpset_a = { a[0] }
    tmpset_b = { b[0] }
    for i in range(1, n):
        ai = a[i]
        bi = b[i]
        if ai in tmpset_a:
            cumnum_a[i] = cumnum_a[i-1]
        else:
            cumnum_a[i] =cumnum_a[i-1]+1
            tmpset_a.add(ai)
        if bi in tmpset_b:
            cumnum_b[i] = cumnum_b[i-1]
        else:
            cumnum_b[i] = cumnum_b[i-1]+1
            tmpset_b.add(bi)

    i = 0
    j = 0
    tmpset = set()
    kmax = min(cumnum_a[n-1], cumnum_b[n-1])
    difsize = [0]*(kmax+1)
    for k in range(1, kmax+1):
        while cumnum_a[i] < k:
            i += 1
        while cumnum_b[j] < k:
            j += 1
        if a[i] in tmpset:
            tmpset.remove(a[i])
        else:
            tmpset.add(a[i])
        if b[j] in tmpset:
            tmpset.remove(b[j])
        else:
            tmpset.add(b[j])
        difsize[k] = len(tmpset)

    ans=[]
    for x, y in queries:
        x -= 1
        y -= 1
        if cumnum_a[x] == cumnum_b[y]:
            k = cumnum_a[x]
            if difsize[k] == 0:
                ans.append('Yes')
            else:
                ans.append('No')
        else:
            ans.append('No')
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,b,q,queries=readinput()
    ans=solve(n,a,b,q,queries)
    printans(ans)
