def readinput():
    s=input()
    return s

def main(s):
    ans=''
    prevch=''
    count=0
    for c in s:
        if prevch==c:
            count+=1
        else:
            if count>0:
                ans+=prevch+str(count)
                count=0
            prevch=c
            count+=1
    else:
        if count>0:
            ans+=prevch+str(count)
    return ans                  

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
