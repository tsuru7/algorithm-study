n = int(input())
d=[]
d[:]=map(int,input().split())
sum=0
for i in range(0,n):
    for j in range(i+1,n):
        sum+=d[i]*d[j]
        #print(i,j,d[i]*d[j])
print(sum)
