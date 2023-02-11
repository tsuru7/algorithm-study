def readinput():
    n,k=map(int,input().split())
    s=input()
    return n,k,s

def main(n,k,s):
    ans=s[:k-1]+s[k-1].lower()+s[k:]
    return ans

if __name__=='__main__':
    n,k,s=readinput()
    ans=main(n,k,s)
    print(ans)
