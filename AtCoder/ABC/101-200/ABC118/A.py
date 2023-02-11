def readinput():
    a,b=map(int,input().split())
    return a,b

def main(a,b):
    if b % a == 0:
        return a + b
    else:
        return b - a

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    print(ans)
