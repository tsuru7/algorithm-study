def readinput():
    n=int(input())
    d=[]
    for i in range(n):
        d.append(int(input()))
    return (n,d)

def main(n,d):
    d.sort(reverse=True)
    npre=d[0]
    ndan=1
    for i in range(1,n):
        if(d[i]<npre):
            npre=d[i]
            ndan+=1
    
    return ndan

def main2(n,d):
    # 別解
    set_d = set(d)
    return len(set_d)

if __name__=='__main__':
    n,d=readinput()
    ans=main2(n,d)
    print(ans)
