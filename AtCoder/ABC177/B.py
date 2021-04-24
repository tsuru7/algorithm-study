def readinput():
    s=input()
    t=input()
    return s,t

def main(s,t):
    ans=len(t)
    for i in range(len(s)-len(t)+1):
        count=0
        for j in range(len(t)):
            if s[i+j]!=t[j]:
                count+=1
        ans=min(ans,count)
    return ans

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    print(ans)
