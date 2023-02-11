def readinput():
    n,m=list(map(int,input().split()))
    lmpSw=[]
    for _ in range(m):
        l=list(map(int,input().split()))
        lmpSw.append(l[1:])
    p=list(map(int,input().split()))
    return n,m,lmpSw,p

def main(n,m,lmpSw,p):
    # 電球につながっているスイッチのビット表現を作る
    lmpSwBit=[0]*m
    for i in range(m):
        swBit=0
        for sw in lmpSw[i]:
            swBit+=2**(sw-1)
        lmpSwBit[i]=swBit

    # lmpStat[m][swStat]を準備する
    lmpStat=[]
    for i in range(m):
        stat=[0 for x in range(2**n)]
        lmpStat.append(stat)


    allon=0
    for swStat in range(2**n):
        # スイッチの全状態をスキャン
        count=0
        for lmp in range(m):
            # 全電球についてループ
            swBit=lmpSwBit[lmp]
            b=1
            for sw in range(n):            
                if(swBit&b==b) and (swStat & b)==b:
                    lmpStat[lmp][swStat]+=1
                b=b*2
            lmpStat[lmp][swStat]+=p[lmp]
            if(lmpStat[lmp][swStat]%2==0):
                count+=1
        if(count==m):
            allon+=1
    return allon


if __name__=='__main__':
    n,m,lmpSw,p=readinput()
    ans=main(n,m,lmpSw,p)
    print(ans)
