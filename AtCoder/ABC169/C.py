

def readinput():
    #a,b=list(map(float,input().split()))
    a,b=input().split()
    a=int(a)
    b=float(b+'000000000000000')
    return a,b

def main(a,b):
    #ans=int(a*b*10)//10
    b=int(b*1000)
    ans=a*b//1000
    return ans

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    print(ans)
