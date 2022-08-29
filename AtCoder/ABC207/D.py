import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
import cmath
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

def main(n,S,T):
    if n == 1:
        return 'Yes'
    elif n == 2:
        Tdist = (T[0].real-T[1].real)**2 + (T[0].imag-T[1].imag)**2
        Sdist = (S[0].real-S[1].real)**2 + (S[0].imag-S[1].imag)**2
        if Sdist == Tdist:
            return 'Yes'
        else:
            return 'No'

    # n >= 3

    GT = complex(0,0)
    for i in range(n):
        GT += T[i]
    GT = GT/n
    for i in range(n):
        T[i] -= GT
    Tpolar = []
    for i in range(n):
        radius2 = (T[i].real)**2 + (T[i].imag)**2 
        Tpolar.append((radius2, cmath.phase(T[i])))
    Tpolar.sort()
    
    GS = complex(0,0)
    for i in range(n):
        GS += S[i]
    GS = GS/n
    for i in range(n):
        S[i] -= GS
    Spolar = []
    for i in range(n):
        radius2 = (S[i].real)**2 + (S[i].imag)**2 
        Spolar.append((radius2, cmath.phase(S[i])))
    Spolar.sort()

    for i in range(n):
        if abs(Spolar[i][0] - Tpolar[i][0]) > 0.0001:
            return 'No'
    
    rdist = {}
    for i in range(n):
        radius = Spolar[i][0]
        if radius not in rdist.keys():
            rdist[radius] = 1
        else:
            rdist[radius] += 1
    
    for k, v in rdist.items():
        


    ans=0
    return ans

def isEquivalent(c, d):
    if abs(c.real-d.real) < 0.0001 and abs(c.imag-d.imag) < 0.0001:
        return True
    else:
        return False


def printans(ans):
    print(ans)

if __name__=='__main__':
    n,S,T=readinput()
    ans=main(n,S,T)
    printans(ans)
