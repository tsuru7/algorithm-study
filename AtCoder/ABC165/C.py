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
    n,m,q=m_input()
    queries = []
    for _ in range(q):
        a,b,c,d = m_input()
        queries.append((a,b,c,d))
    return n,m,queries

def gen_a(l,n,m,aList):
    # print(f'[before] level: {l}, aList: {aList}')

    if l > n:
        return aList
    
    if l == 0:
        for i in range(1, m+1):
            aList.append([i])

    tempList = []
    for a in aList:
        lowest = a[-1]
        for i in range(lowest, m+1):
            tempList.append(a + [i])
    aList = gen_a(l+1, n, m, tempList)

    # print(f'[after] level: {l}, aList: {aList}')
    return aList

def calc_point(l, queries):
    point = 0
    for a,b,c,d in queries:
        a -= 1
        b -= 1
        if l[b] - l[a] == c:
            point += d
    return point

def main(n,m,queries):
    aList = []
    aList = gen_a(0, n, m, aList)
    # print(aList)
    ans=0
    for a in aList:
        point = calc_point(a, queries)
        ans = max(ans, point)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,queries=readinput()
    ans=main(n,m,queries)
    printans(ans)
