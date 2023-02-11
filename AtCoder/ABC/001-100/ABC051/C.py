def readinput():
    sx,sy,tx,ty=list(map(int,input().split()))
    return sx,sy,tx,ty

def main(sx,sy,tx,ty):
    ans=''
    ans=ans+'U'*(ty-sy)
    ans=ans+'R'*(tx-sx+1)
    ans=ans+'D'*(ty-sy+1)
    ans=ans+'L'*(tx-sx+1)
    ans=ans+'U'+'L'
    ans=ans+'U'*(ty-sy+1)
    ans=ans+'R'*(tx-sx+1)
    ans=ans+'D'*(ty-sy+1)
    ans=ans+'L'*(tx-sx)
    return ans

if __name__=='__main__':
    sx,sy,tx,ty=readinput()
    ans=main(sx,sy,tx,ty)
    print(ans)
