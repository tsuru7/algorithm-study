def readinput():
    a,b,c,d=map(int,input().split())
    return a,b,c,d

def main(a,b,c,d):
    while True:
        c-=b
        if c<=0:
            return 'Yes'
        a-=d
        if a<=0:
            return 'No'


if __name__=='__main__':
    a,b,c,d=readinput()
    ans=main(a,b,c,d)
    print(ans)
