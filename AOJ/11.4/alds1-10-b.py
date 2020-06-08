n=int(input())
sum=0
k,l=list(map(int,input().split()))
n-=1
while(n>0):
    l,m=list(map(int,input().split()))
    n-=1
    sum+=k*l*m
print(sum) 
   