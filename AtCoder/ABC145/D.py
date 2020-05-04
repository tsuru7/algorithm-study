from scipy.special import comb

x, y = list(map(int,input().split()))

if ((x+y)%3 != 0):
    print(0)
    exit()
else:
    n1 = (-x+2*y)//3
    n2 = (2*x -y)//3
    if (n1<n2):
        npath = comb(n1+n2, n1, exact=True)
    else:
        npath = comb(n1+n2, n2, exact=True)
    print(npath % (10**9+7))

