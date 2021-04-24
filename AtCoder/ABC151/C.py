def readinput():
    n,m=map(int,input().split())
    tries=[]
    for _ in range(m):
        p,s=input().split()
        p=int(p)
        tries.append((p,s))
    return n,m,tries

def main(n,m,tries):
    point=[[0,0] for i in range(n+1)]
    for i in range(m):
        p,s=tries[i]
        if s=='WA':
            if point[p][0]>0:
                continue
            else:
                point[p][1]+=1
        else:
            point[p][0]+=1
    ac=0
    wa=0
    for i in range(1,n+1):
        if point[i][0]>0:
            ac+=1
            wa+=point[i][1]
    
    return ac,wa

if __name__=='__main__':
    n,m,tries=readinput()
    ans=main(n,m,tries)
    print(' '.join(map(str,ans)))

