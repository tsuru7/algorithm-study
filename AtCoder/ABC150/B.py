def readinput():
    n=int(input())
    s=input()
    return n,s

def main(n,s):
    i=0
    count=0
    while(i<n):
        p=s[i:].find('ABC')
        #print(s[i:])
        if(p!=-1):
            i+=p+3
            count+=1
        else:
            break
    return count

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    print(ans)


