def readinput():
    x,n=list(map(int,input().split()))
    if (n>0):
        p=list(map(int,input().split()))
    else:
        p=[]
    return x,n,p

def main(x,n,p):
    if (len(p)==0):
        return x

    mindist=102
    nearest=0
    for y in range(0,102):
        if y in p:
            continue
        if abs(x-y) < mindist:
            mindist = abs(x-y)
            nearest=y        
    return nearest

if __name__=='__main__':
    x,n,p=readinput()
    ans=main(x,n,p)
    print(ans)
