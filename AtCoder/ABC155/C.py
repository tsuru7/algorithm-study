def readinput():
    n=int(input())
    sList=[]
    for _ in range(n):
        sList.append(input())
    return n,sList

def main(n,sList):
    hist={}
    for s in sList:
        if s in hist.keys():
            hist[s]+=1
        else:
            hist[s]=1
    hList=sorted(list(hist.items()), key=lambda x:x[1], reverse=True)
    #print(hList)
    hvalue=hList[0][1]
    ss=[]
    i=0
    while(i<len(hList) and hList[i][1]==hvalue):
        ss.append(hList[i][0])
        i+=1
    ss.sort()
    for s in ss:
        print(s)    

if __name__=='__main__':
    n,sList=readinput()
    main(n,sList)
