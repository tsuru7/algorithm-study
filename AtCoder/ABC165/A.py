k=int(input())
a,b=list(map(int,input().split()))

if ( a % k == 0 or b % k == 0):
    print('OK')
elif ((b // k) > (a//k)):
    print('OK')
else:
    print('NG')
