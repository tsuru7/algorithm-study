def readinput():
    s=input()
    return s

def main(s):
    
    maxlen=0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub=s[i:j]
            for c in sub:
                if(c == 'A' or c == 'C' or c == 'G' or c == 'T'):
                    pass
                else:
                    break
            else:
                maxlen=max(maxlen,len(sub))
        
    return maxlen

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
