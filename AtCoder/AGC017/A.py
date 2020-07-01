from itertools import combinations

def readinput():
    n,p=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,p,a


from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main(n,p,a):
    ne=0
    no=0
    for i in range(n):
        if a[i]%2==0:
            ne+=1
        else:
            no+=1
    #print('ne: {}, no: {}'.format(ne,no))

    alle=2**ne
    #print('alle: {}'.format(alle))

    allo=0
    if p==0:
        mo=0
    else:
        mo=1
    while mo<=no:
        allo+=cmb(no,mo)
        mo+=2
    #print('allo: {}'.format(allo))
    
    return alle*allo

if __name__=='__main__':
    n,p,a=readinput()
    ans=main(n,p,a)
    print(ans)
