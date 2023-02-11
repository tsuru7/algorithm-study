def readinput():
    s=input()
    return s

def findToken(s):
    tokens=[]
    i=0
    count=0
    while(i+1<len(s)):
        if s[i]=='2' and s[i+1]=='5':
            count+=1
            i+=2
        else:
            if count>0:
                tokens.append(count)
                count=0
            i+=1
    else:
        if count>0:
            tokens.append(count)
    return tokens

def main(s):
    tokens=findToken(s)
    sum=0
    for token in tokens:
        sum+=token*(token+1)//2
    #print(tokens)
    return sum

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
