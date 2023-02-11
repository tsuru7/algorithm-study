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
    n,k=m_input()
    a=l_input()
    return n,k,a

def solve(n,k,a):
    aa = []
    for i in range(n):
        aa.append((a[i], i))
    aa.sort()
    b = [0 for _ in range(n)]
    b[0] = aa[0][0]
    for i in range(1, n):
        b[i] = aa[i][0] - aa[i-1][0]
    i = 0
    tabeta = 0
    while k > b[i]*(n-i):
        k -= b[i]*(n-i)
        tabeta += b[i]
        i += 1


    m = n-i # 空でないかごの数
    tabeta2 = k // m  # 空でないかごから何個減らせるか
    restnum = k % m  # さらに余りの個数

    empty = []
    for aj, j in aa[:i]:
        empty.append([0, j])
    
    rest = aa[i:]
    rest.sort(key=lambda x: x[1])
    nokori = []
    for aj, j in rest:
        nokori.append([aj-tabeta-tabeta2, j])
    for i in range(restnum):
        nokori[i][0] -= 1
    zenbu = empty + nokori
    zenbu.sort(key=lambda x: x[1])
    ans = []
    for i in range(n):
        ans.append(zenbu[i][0])
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
