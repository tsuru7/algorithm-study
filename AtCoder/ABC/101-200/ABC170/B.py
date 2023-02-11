def readinput():
    x,y=list(map(int,input().split()))
    return x,y

def main(x,y):
    if(y%2==1):
        return 'No'
    ymin=2*x
    ymax=4*x
    if (ymin<=y) and (y<=ymax):
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    x,y=readinput()
    ans=main(x,y)
    print(ans)
