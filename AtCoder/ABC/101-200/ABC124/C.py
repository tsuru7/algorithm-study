def readinput():
    s=input()
    return s

def main(s):
    count=0
    t=['0','1']
    for i in range(len(s)):
        if s[i]==t[i%2]:
            count+=1
    return min(count,len(s)-count)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
