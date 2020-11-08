def readinput():
    a,b=map(int,input().split())
    return a,b

def main(a,b):
    if 2*a + 100 > b:
        return 2*a + 100 - b
    else:
        return 0
    ans=0
    return ans

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    print(ans)
