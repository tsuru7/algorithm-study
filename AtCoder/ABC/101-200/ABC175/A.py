def readinput():
    s=input()
    return s

def main(s):
    ans=0
    cont=0
    for c in s:
        if c=='S':
            cont=0
        else:
            cont+=1
            ans=max(cont,ans)
    return ans

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
