def readinput():
    b=list(input().split())
    n=int(input())
    a=[]
    for _ in range(n):
        a.append(input())
    return b,n,a

def main(b,n,a):
    xtbl1=[]
    for i in range(1,10):
        xtbl1.append( (chr(ord(b[i])-ord('1')+ord('A')), str(i) ))
    #print(xtbl1)
    xtbl2=sorted(xtbl1,key=lambda x: x[0])
    #print(xtbl2)

    ia=[]
    for i in range(n):
        amod=a[i]
        for j in range(1,10):
            #print('replace {} -> {}'.format(chr(j-1+ord('1')), xtbl[j]))
            amod=amod.replace(chr(j-1+ord('1')), chr(j-1+ord('A')))
        #print('step1: {} -> {}'.format(a[i],amod))

        for j in range(9):
            amod=amod.replace(xtbl2[j][0], xtbl2[j][1])
        #print('step2: -> {}'.format(amod))
        #print(a[i], amod)
        ia.append((int(amod),a[i]))
    ia.sort(key=lambda x:x[0]) 
    for i in range(n):
        print(ia[i][1])

if __name__=='__main__':
    b,n,a=readinput()
    main(b,n,a)
