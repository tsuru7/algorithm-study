def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    cmat = []
    for i in range(n):
        cmat.append(l_input())
    return n,cmat

def main(n,cmat):
    for i in range(1, n):
        for j in range(1, n):
            if cmat[i][j] - cmat[i][0] == cmat[0][j] - cmat[0][0]:
                continue
            else:
                return 'No', []
    for j in range(1, n):
        for i in range(1, n):
            if cmat[i][j] - cmat[0][j] == cmat[i][0] - cmat[0][0]:
                continue
            else:
                return 'No', []
    b = [cmat[0][j] for j in range(n)]
    a = [cmat[i][0] - cmat[0][0] for i in range(n)]
    mina = min(a)
    minb = min(b)
    if mina < 0:
        for i in range(n):
            a[i] -= mina
            b[i] += mina
    elif minb < 0:
        for i in range(n):
            a[i] += minb
            b[i] -= minb
    return 'Yes', [a, b]
    
def main2(n,cmat):
    cmin = cmat[0][0]
    ij = (0,0)
    for i in range(n):
        for j in range(n):
            if cmin > cmat[i][j]:
                cmin = cmat[i][j]
                ij = (i, j)
    i, j = ij
    b = [cmat[i][j] for j in range(n)]
    a = [cmat[i][j] - b[j] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if cmat[i][j] == a[i] + b[j]:
                continue
            else:
                return 'No', [a, b]
    return 'Yes', [a, b]

def printans(ans, ab):
    if ans == 'No':
        print(ans)
    else:
        print(ans)
        a, b = ab
        print(' '.join(map(str, a)))
        print(' '.join(map(str, b)))

if __name__=='__main__':
    n,cmat=readinput()
    ans, ab=main2(n,cmat)
    printans(ans, ab)
