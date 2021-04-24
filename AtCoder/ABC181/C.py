def readinput():
    n=int(input())
    xy = []
    for _ in range(n):
        x,y=map(int,input().split())
        xy.append((x,y))
    return n,xy

import sys
infty = sys.maxsize

def main(n,xy):


    ans=set()
    for i in range(n-1):
        xi = xy[i][0]
        yi = xy[i][1]
        for j in range(i+1,n):
            xj = xy[j][0]
            yj = xy[j][1]
            if xj == xi:
                a = infty
                b = xi
            else:
                a = (yj - yi)/(xj - xi)
                b = yj - a * xj
            #print(xi,yi, xj,yj, (a,b))
            if (a,b) in ans:
                return 'Yes'
            else:
                ans.add((a,b))
                #print(ans)
    return 'No'

if __name__=='__main__':
    n,xy=readinput()
    ans=main(n,xy)
    print(ans)
