def readinput():
    n,m=list(map(int,input().split()))
    name=input()
    kit=input()
    return n,m,name,kit

def main(n,m,name,kit):
    nmoji=[0]*26
    kmoji=[0]*26
    for i in range(n):
        c=ord(name[i])-ord('A')
        nmoji[c]+=1
    for i in range(m):
        c=ord(kit[i])-ord('A')
        kmoji[c]+=1

    #print(nmoji)
    #print(kmoji)

    nkit=0
    for i in range(26):
        if nmoji[i]!=0 and kmoji[i]==0:
            return -1
        
        if nmoji[i]==0:
            continue

        if nmoji[i] % kmoji[i] == 0:
            need=nmoji[i]//kmoji[i]
        else:
            need=nmoji[i]//kmoji[i]+1
        #print(i, need, nkit)
        nkit=max(nkit,need)
    return nkit

if __name__=='__main__':
    n,m,name,kit=readinput()
    ans=main(n,m,name,kit)
    print(ans)
