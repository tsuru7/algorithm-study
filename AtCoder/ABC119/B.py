def readinput():
    n=int(input())
    dama=[]
    for _ in range(n):
        a,b=input().split()
        dama.append((a,b))
    return n,dama

def main(n,dama):
    sum=0.0
    for x,u in dama:
        if u=='JPY':
            sum+=int(x)
        else:
            sum+=float(x)*380000.0
    return sum

if __name__=='__main__':
    n,dama=readinput()
    ans=main(n,dama)
    print(ans)
