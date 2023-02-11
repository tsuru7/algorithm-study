n=int(input())
s=input()
ss=''
for c in s:
    cc=ord(c)+n
    if (cc > ord('Z')):
        cc-=26
    ss+=chr(cc)
print(ss)
