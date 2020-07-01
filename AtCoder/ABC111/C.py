def readinput():
    n=int(input())
    v=list(map(int,input().split()))
    return n,v

def main(n,v):

    hist=[0]*(10**5+1)
    maxhist=0
    maxvalue=0
    for i in range(n):
        hist[v[i]]+=1
        if (maxhist<hist[v[i]]):
            maxhist=hist[v[i]]
            maxvalue=v[i]
    print('maxvalue: {}, maxhist: {}'.format(maxvalue, maxhist))

    secondhist=0
    for i in range(1,10**5+1):
        if i == maxvalue:
            continue
        secondhist=max(secondhist,hist[i])
    print('secondhist: {}'.format(secondhist))

    nsame=n//2
    nchange=0
    if maxhist>nsame:
        nchange+=maxhist-nsame
    elif maxhist<nsame:
        nchange+=nsame-maxhist
    nchange+=nsame-secondhist
    return nchange

def main2(n,v):
    eList=[]
    oList=[]
    for i in range(n):
        if i%2==0:
            eList.append(v[i])
        else:
            oList.append(v[i])

    #print(eList)
    #print(oList)

    ehist=[0]*(10**5+1)
    for i in eList:
        ehist[i]+=1
    emaxh=0
    emaxv=0
    for i in range(1,10**5+1):
        if emaxh<ehist[i]:
            emaxh=ehist[i]
            emaxv=i
    esech=0
    esecv=0
    for i in range(1,10**5+1):
        if i==emaxv:
            continue
        if esech<ehist[i]:
            esech=ehist[i]
            esecv=i
    
    ohist=[0]*(10**5+1)
    for i in oList:
        ohist[i]+=1
    omaxh=0
    omaxv=0
    for i in range(1,10**5+1):
        if omaxh<ohist[i]:
            omaxh=ohist[i]
            omaxv=i
    osech=0
    osecv=0
    for i in range(1,10**5+1):
        if i == omaxv:
            continue
        if osech<ohist[i]:
            osech=ohist[i]
            osecv=i

    if omaxv==emaxv:
        if omaxh==emaxh:
            if osech>esech:
                omaxv=osecv
            else:
                emaxv=esecv
        elif omaxh>emaxh:
            emaxv=esecv
        else:
            omaxv=osecv
    
    #print('emaxv: {}, omaxv: {}'.format(emaxv,omaxv))

    nchange=0
    for i in range(n//2):
        if eList[i]!=emaxv:
            nchange+=1
        if oList[i]!=omaxv:
            nchange+=1
    return nchange


if __name__=='__main__':
    n,v=readinput()
    ans=main2(n,v)
    print(ans)
