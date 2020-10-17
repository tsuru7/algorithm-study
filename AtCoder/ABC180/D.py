def readinput():
    x,y,a,b=map(int,input().split())
    return x,y,a,b

def main(x,y,a,b):
    m=0
    k=0
    while a*x <= x+b and a*x < y:
        x *= a
        m += 1
    k = (y-1 - x)//b
    return m+k

if __name__=='__main__':
    x,y,a,b=readinput()
    ans=main(x,y,a,b)
    print(ans)
