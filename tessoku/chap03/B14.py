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
    if n <= 20:
        candidates = set()
        ALL = 2**n
        for i in range(ALL):
            tmp = 0
            for j in range(n):
                b = 1<<j
                if i & b > 0:
                    tmp += a[j]
            if tmp == k:
                return 'Yes'
        return 'No'
    else:
        m = n//3
        l = n - m*2
        grp1 = a[:m]
        grp2 = a[m:2*m]
        grp3 = a[2*m:]
        ALLm = 2**m
        ALLl = 2**l
        candi1 = set()
        candi2 = set()
        candi3 = set()
        for i in range(ALLm):
            tmp1 = 0
            tmp2 = 0
            for j in range(m):
                b = 1<<j
                if i & b > 0:
                    tmp1 += grp1[j]
                    tmp2 += grp2[j]
            candi1.add(tmp1)
            candi2.add(tmp2)
        for i in range(ALLl):
            tmp = 0
            for j in range(l):
                b = 1<<j
                if i & b > 0:
                    tmp += grp3[j]
            candi3.add(tmp)
        for i in candi1:
            for j in candi2:
                if k - i - j in candi3:
                    return 'Yes'
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
