def readinput():
    k=int(input())
    s=input()
    return k,s

def main(k,s):
    if(len(s)<=k):
        return s
    else:
        return s[0:k]+'...'

if __name__=='__main__':
    k,s=readinput()
    ans=main(k,s)
    print(ans)
