def readinput():
    t=int(input())
    qlist=[]
    for _ in range(t):
        n,a,b=map(int,input().split())
        qlist.append((n,a,b))
    return t,qlist

def get_count(n,a,b):

    if a+b>n:
        return 0
    
    MOD=10**9+7

    term1=( (n-a-b+1)*(n-a-b+2) )%MOD
    term2=( 2*(n-a+1)*(n-b+1) )%MOD

    ans = ( term1 * ( term2 - term1) )%MOD

    return ans


def main(t,qlist):
    ans=[]
    for n,a,b in qlist:
        ans.append(get_count(n,a,b))
    return ans

if __name__=='__main__':
    t,qlist=readinput()
    ans=main(t,qlist)
    for a in ans:
        print(a)
