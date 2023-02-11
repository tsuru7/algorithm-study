from collections import deque
def readinput():
    n,m,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    return n,m,k,a,b

def main(n,m,k,a,b):
    qa=deque(a)
    qb=deque(b)
    count=0
    res=k
    while(len(qa)>0 and len(qb)>0):
        if qa[0] < qb[0]:
            res-=qa[0]
            qa.popleft()
        else:
            res-=qb[0]
            qb.popleft()
        if res<0:
            return count
        count+=1
    else:
        if len(qa)==0:
            while(len(qb)>0):
                res-=qb[0]
                qb.popleft()
                if res<0:
                    return count
                count+=1
            return count
        else:
            while(len(qa)>0):
                res-=qa[0]
                qa.popleft()
                if res<0:
                    return count
                count+=1
            return count

import sys
INFTY=sys.maxsize
def find(t,s):
    '''
    単調増加配列sからs[i]がtを超えない最大のiを返す
    '''
    ss=s[:]
    ss.append(INFTY)
    left=0
    right=len(ss)
    while(left<right):
        middle=(left+right)//2
        #print(left,middle,right,t,ss)
        if ss[middle]==t:
            #print(middle, ss)
            return middle
        if t<ss[middle]:
            right=middle
        else:
            left=middle+1
    else:
        return left-1

def main2(n,m,k,a,b):
    sa=[0]
    for i in range(1,n+1):
        sa.append(sa[i-1]+a[i-1])
    sb=[0]
    for i in range(1,m+1):
        sb.append(sb[i-1]+b[i-1])
    maxab=0
    nb=m+1
    for na in range(0,n+1):
        res=k-sa[na]
        if res>=0:
            nb=find(res,sb[:nb+1])
            #print(na,nb,sa,sb)
            maxab=max(maxab,na+nb)
    return maxab

from bisect import bisect_left, bisect_right
def find_le(a, x):
    'Find rightmost index less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i-1
    raise ValueError

def main3(n,m,k,a,b):
    sa=[0]
    for i in range(1,n+1):
        sa.append(sa[i-1]+a[i-1])
    sb=[0]
    for i in range(1,m+1):
        sb.append(sb[i-1]+b[i-1])
    maxab=0
    nb=m+1
    for na in range(0,n+1):
        res=k-sa[na]
        if res>=0:
            nb=find_le(sb,res)
            #print(na,nb,res,sa,sb)
            maxab=max(maxab,na+nb)
    return maxab

def main4(n,m,k,a,b):
    sa=[0]
    for i in range(1,n+1):
        sa.append(sa[i-1]+a[i-1])
    sb=[0]
    for i in range(1,m+1):
        sb.append(sb[i-1]+b[i-1])
    maxab=0
    nb=m
    for na in range(0,n+1):
        res=k-sa[na]
        while res<sb[nb] and nb>=0:
            nb-=1
        else:
            if nb>=0:
                maxab=max(maxab,na+nb)
        #print(na,nb)
    return maxab

def readinput2():
    m=2*10**5
    n=2*10**5
    a=[10**9]*n
    b=[10**9]*m
    k=1
    return n,m,k,a,b

if __name__=='__main__':
    n,m,k,a,b=readinput()
    ans=main3(n,m,k,a,b)
    print(ans)
