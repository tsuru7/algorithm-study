a,b,x = list(map(int,input().split()))

if(x<a+b):
    print(0)
    exit()

# 桁数を求める
r=0
s=0
j=0
for i in range(11):
    j+=1         # Nの桁数
    r=10**i      # j桁の最小整数
    s=a*r+b*j
    if(s>x):
        break    # j桁の最小数がxを超えた

# Nはj-1桁
j=j-1

xr = x - b*j
n = xr // a
if (n>10**9):
    n=10**9
elif (n>=10**j):
    n=10**j-1

#print('j: {}'.format(j))

print(n)
