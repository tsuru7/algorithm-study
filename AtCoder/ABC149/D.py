def readinput():
    n,k=list(map(int,input().split()))
    r,s,p=list(map(int,input().split()))
    t=input()
    return n,k,r,s,p,t

def main(n,k,r,s,p,t):
    rireki=[]
    tokuten=0
    for i in range(n):
        c=t[i]
        if i<k:
            if(c=='r'):
                rireki.append('p')
                tokuten+=p
                #print('パー',tokuten)
            elif(c=='s'):
                rireki.append('r')
                tokuten+=r
                #print('グー',tokuten)
            elif(c=='p'):
                rireki.append('s')
                tokuten+=s
                #print('チョキ',tokuten)
        else:
            #print(rireki[i-k])
            if c=='r':
                if rireki[i-k]=='p':
                    rireki.append('x')
                    #print('パー以外',tokuten)
                else:
                    rireki.append('p')
                    tokuten+=p
                    #print('パー',tokuten)
            elif c=='s':
                if rireki[i-k]=='r':
                    rireki.append('x')
                    #print('グー以外',tokuten)
                else:
                    rireki.append('r')
                    tokuten+=r
                    #print('グー',tokuten)
            elif c=='p':
                if rireki[i-k]=='s':
                    rireki.append('x')
                    #print('チョキ以外',tokuten)
                else:
                    rireki.append('s')
                    tokuten+=s
                    #print('チョキ',tokuten)
        #print(rireki)
    return tokuten

if __name__=='__main__':
    n,k,r,s,p,t=readinput()
    ans=main(n,k,r,s,p,t)
    print(ans)

