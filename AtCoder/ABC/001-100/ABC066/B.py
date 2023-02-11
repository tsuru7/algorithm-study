def readinput():
    s=input()
    return s

def main(s):
    i=len(s)-2
    while(i>0):
        lensub=i//2
        sub1=s[:lensub]
        sub2=s[lensub:lensub*2]
        if sub1==sub2:
            return i
        i-=2
    return 0

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
