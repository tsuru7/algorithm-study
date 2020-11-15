def readinput():
    sx, sy, gx, gy=map(int,input().split())
    return sx, sy, gx, gy

def main(sx, sy, gx, gy):
    ans = sx - sy*(sx-gx)/(sy+gy)
    return ans

if __name__=='__main__':
    sx, sy, gx, gy=readinput()
    ans=main(sx, sy, gx, gy)
    print(ans)
