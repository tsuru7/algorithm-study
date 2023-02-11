def readinput():
    h,w=map(int,input().split())
    mat=[]
    for _ in range(h):
        l=list(map(int,input().split()))
        mat.append(l)
    return h,w,mat

def main(h,w,mat):
    mina=101
    for i in range(h):
        for j in range(w):
            mina=min(mina,mat[i][j])
    count=0
    for i in range(h):
        for j in range(w):
            count += (mat[i][j]-mina)
    return count

if __name__=='__main__':
    h,w,mat=readinput()
    ans=main(h,w,mat)
    print(ans)
