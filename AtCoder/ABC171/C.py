def readinput():
    n=int(input())
    return n

def main(n):
    name=subname(n)
    return name

def subname(n):
    alph='abcdefghijklmnopqrstuvwxyz'
    if n <=26:
        return alph[n-1]
    else:
        r=n%26
        if r==0:
            addch='z'
            n=n-26
        else:
            addch=alph[r-1]
        q=n//26
        return subname(q)+addch


if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
