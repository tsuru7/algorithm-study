n=int(input())
s=input()
if(n%2==1):
    print('No')
else:
    m=n//2
    s1=s[0:m]
    s2=s[m:]
    #print('s1:{} s2:{}'.format(s1,s2))
    if(s1==s2):
        print('Yes')
    else:
        print('No')
