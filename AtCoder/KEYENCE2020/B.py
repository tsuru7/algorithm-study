def readinput():
    n=int(input())
    arms=[]
    for _ in range(n):
        x,l=list(map(int,input().split()))
        arms.append([x,l])
    return n,arms

def main(n,arms):
    count=0
    i=0
    j=i+1
    while(j<n):
        l=arms[i][0]+arms[i][1]
        r=arms[j][0]-arms[j][1]
        if l<=r:
            i=j
            j=i+1
        else:
            if arms[i][1]<=arms[j][1]:
                j=j+1
                count+=1
                print('{}, {}: remove {}'.format(i,j,j))
            else:
                i=j
                j=i+1
                count+=1
                print('{}, {}: remove {}'.format(i,j,i))
    return n-count

def main2(n,arms):
    for arm in arms:
        l=arm[0]-arm[1]
        r=arm[0]+arm[1]
        arm.append(l)
        arm.append(r)
    arms.sort(key=lambda x:x[3])
    count=1
    llim=arms[0][3]
    for i in range(1,n):
        if llim<=arms[i][2]:
            count+=1
            llim=arms[i][3]
    return count

if __name__=='__main__':
    n,arms=readinput()
    ans=main2(n,arms)
    print(ans)
