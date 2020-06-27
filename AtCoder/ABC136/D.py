def readinput():
    s=input()
    return s

def main(s):
    sList=[]
    i=0
    j=0
    rflg=True
    lflg=False
    while(j<len(s)):
        if s[j]=='L' and rflg==True:
            rflg=False
            lflg=True
        elif s[j]=='R' and lflg==True:
            lflg=False
            rflg=True
            sList.append(s[i:j])
            i=j
        j+=1
    sList.append(s[i:j])
    
    #print(sList)

    ans=[]
    for sub in sList:
        nr=sub.count('R')
        nl=sub.count('L')
        mr=nr//2+nr%2 + nl//2
        ml=nr//2      + nl//2+nl%2
        il=sub.find('L')
        ir=il-1
        #print(ir,il,sub)
        for i in range(nr-1):
            ans.append(0)
        ans.append(mr)
        ans.append(ml)
        for i in range(nl-1):
            ans.append(0)
        #print(ans)
    return ans

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(' '.join(map(str,ans)))
