def readinput():
    s=input()
    t=input()
    return s,t

def main(s,t):
    count=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1
    return count

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    print(ans)
