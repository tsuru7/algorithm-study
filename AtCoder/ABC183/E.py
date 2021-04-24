def readinput():
    h, w=map(int,input().split())
    smat = []
    for _ in range(h):
        smat.append(list(map(int,input().split())))
    return h, w, smat

def main(h, w, smat):
    # cmat: カウント用行列
    cmat = []
    for _ in range(h):
        cmat.append([0]*w)
    
    pos = (h-1, w-1)
    
    ans=0
    return ans

if __name__=='__main__':
    h, w, smat=readinput()
    ans=main(h, w, smat)
    print(ans)