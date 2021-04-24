def readinput():
    l,r=map(int,input().split())
    return l,r

def main(l,r):
    ans=2018
    for i in range(l,min(l+2019,r+1)):
        for j in range(i+1,min(l+2019,r+1)):
            ans=min( ((i%2019) * (j%2019))%2019, ans )
    return ans

if __name__=='__main__':
    l,r=readinput()
    ans=main(l,r)
    print(ans)
