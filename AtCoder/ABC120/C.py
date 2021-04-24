def readinput():
    s=list(input())
    return s

def main(s):
    n=len(s)
    count=0
    for i in range(n):
        if s[i]=='1':
            count+=1
    return min(count,n-count)*2

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
