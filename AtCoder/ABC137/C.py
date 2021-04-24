def readinput():
    n=int(input())
    s=[]
    for _ in range(n):
        s.append(input())
    return n,s

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main(n,s):
    count={}
    for word in s:
        sword=''.join(sorted(word))
        if sword in count:
            count[sword]+=1
        else:
            count[sword]=1
    ans=0
    for k,v in count.items():
        if v>1:
            ans+=cmb(v,2)        

    return ans

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    print(ans)
