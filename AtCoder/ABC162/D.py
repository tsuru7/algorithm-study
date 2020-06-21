def readinput():
    n=int(input())
    s=input()
    s=' '+s
    return n,s

def main(n,s):
    count=0
    all=set(['R','G','B'])
    for i in range(1, n-1):
        l1=s[i]
        for j in range(i+1, n):
            l2=s[j]
            if l1==l2:
                continue
            l3=(all - set([l1,l2])).pop()
            ij=j-i
            sub1=s[j+1:j+ij]
            sub2=s[j+ij+1:]
            count+=sub1.count(l3)
            count+=sub2.count(l3)
    return count

def main2(n,s):
    count=0
    nr=s.count('R')
    ng=s.count('G')
    nb=s.count('B')
    all=set(['R','G','B'])
    for i in range(1, n-1):
        l1=s[i]
        for j in range(i+1, n):
            l2=s[j]
            if l1==l2:
                continue
            ij=j-i
            jk=ij
            k=j+jk
            if(k>n):
                break
            l3=s[k]
            if l3==l1 or l3==l2:
                continue
            count+=1
    return nr*ng*nb-count



if __name__=='__main__':
    n,s=readinput()
    ans=main2(n,s)
    print(ans)
       