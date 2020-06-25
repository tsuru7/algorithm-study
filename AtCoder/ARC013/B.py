def readinput():
    c=int(input())
    nimotsu=[]
    for _ in range(c):
        n,m,l=list(map(int,input().split()))
        nimotsu.append((n,m,l))
    return c,nimotsu

def main(c,nimotsu):
    l1=0
    l2=0
    l3=0
    for l in nimotsu:
        s=sorted(l)
        l1=max(l1,s[0])
        l2=max(l2,s[1])
        l3=max(l3,s[2])
    return l1*l2*l3

if __name__=='__main__':
    c,nimotsu=readinput()
    ans=main(c,nimotsu)
    print(ans)
