def readinput():
    n=int(input())
    a=[]
    for i in range(1,n+1):
        a.append((int(input()),i))
    return n,a

def main(n,a):
    sa=sorted(a,key=lambda x:x[0], reverse=True)
    for i in range(1,n+1):
        if sa[0][1]!=i:
            print(sa[0][0])
        else:
            print(sa[1][0])            

if __name__=='__main__':
    n,a=readinput()
    main(n,a)
