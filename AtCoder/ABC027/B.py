def readinput():
    n=int(input())
    aList=list(map(int,input().split()))
    return n,aList

def main(n,aList):
    sum=0
    for a in aList:
        sum+=a
    if sum%n != 0:
        return -1
    
    avg = sum//n
    #print('avg: {}'.format(avg))
    residue=0
    count=0
    for i in range(n-1):
        residue+=(aList[i]-avg)
        if residue!=0:
            count+=1
        #print('residue: {}'.format(residue))
    residue+=(aList[n-1]-avg)
    #print('residue: {}'.format(residue))
    if residue==0:
        return count
    else:
        return -1

if __name__=='__main__':
    n,aList=readinput()
    ans=main(n,aList)
    print(ans)
