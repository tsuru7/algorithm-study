n = int(input())
s = input()
r = ''
i=0
j=1
while(i<len(s)):
    while(j<len(s) and s[i]==s[j]):
        j+=1
    r += s[j-1]
    #print(r)
    i=j
    j=i+1
print(len(r))
