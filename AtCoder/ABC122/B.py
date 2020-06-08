def readinput():
    s=input()
    return s

def main(s):
    
    maxlen=0
    templen=0
    for i in range(len(s)):
        if(s[i]=='A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T'):
            templen+=1
        else:
            maxlen=max(maxlen,templen)
            templen=0
        
    return max(maxlen,templen)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
