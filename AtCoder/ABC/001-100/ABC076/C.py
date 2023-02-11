def readinput():
    s=input()
    t=input()
    return s,t

def main(s,t):
    found=False
    it=0
    for i in range(len(s)-len(t),-1,-1):
        for j in range(len(t)):
            #print(s[i+j],t[j])
            if s[i+j]=='?':
                continue
            if s[i+j]!=t[j]:
                break
        else:
            found=True
            it=i
            break
    if found==False:
        return 'UNRESTORABLE'

    ans=s[:it]+t+s[it+len(t):]
    ans=ans.replace('?','a')

    return ans

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    print(ans)
