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
    S = []
    for _ in range(n):
        a,b=m_input()
        S.append(complex(a,b))
    T = []
    for _ in range(n):
        c,d=m_input()
        T.append(complex(c,d))
    return n,S,T

def dist2(p1, p2):
    return (p1.real-p2.real)**2 + (p1.imag-p2.imag)**2

def main(n,S,T):
    if n == 1:
        return 'Yes'
    if n == 2:
        if dist2(S[0], S[1]) == dist2(T[0], T[1]):
            return 'Yes'
        else:
            return 'No'
    
    t0 = T[0]
    for i in range(n):
        T[i] -= t0
    t1 = T[1]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            s0 = S[i]
            S2 = []
            for k in range(n):
                S2.append(S[k] - s0)
            s1 = S2[j]

            if dist2(0, s1) != dist2(0,t1):
                continue
            
            U = set()
            V = set()
            for k in range(n):
                U.add(S2[k]*t1)
                V.add(T[k]*s1)
            if U == V:
                return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,S,T=readinput()
    ans=main(n,S,T)
    printans(ans)
