from itertools import combinations

def readinput():
    n=int(input())
    s=input()

    return n,s

def main(n,s):
    count=0
    s1=s[:]
    for i in range(10):
        index1=s1.find(str(i))
        if index1 == -1:
            continue
        s2=s1[index1+1:]
        if(len(s2)<2):
            continue
        #print('s2: {}'.format(s2))
        for j in range(10):
            index2=s2.find(str(j))
            if index2 == -1:
                continue
            s3=s2[index2+1:]
            if(len(s3)<1):
                continue
            #print('s3: {}'.format(s3))
            for k in range(10):
                #print(s[index1+index2+1:])
                index3=s3.find(str(k))
                if index3 == -1:
                    continue
                count+=1
                #print(i,j,k)
    return count

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    print(ans)
     