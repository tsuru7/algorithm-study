import sys
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    ab = []
    for _ in range(n):
        a,b=m_input()
        ab.append((a, b))
    return n,ab

def main(n,ab):
    a = []
    b = []
    for aa, bb in ab:
        a.append(aa)
        b.append(bb)
    # print(a, b)
    tmin = INFTY
    for i in range(n):
        for j in range(n):
            if i == j:
                tmin = min(tmin, a[i]+b[j])
            else:
                tmin = min(tmin, max(a[i], b[j]))
            # print(i,j,a[i], b[j], tmin)
    return tmin

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,ab=readinput()
    ans=main(n,ab)
    printans(ans)
