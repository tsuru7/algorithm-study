def readinput():
    n=int(input())
    xy = []
    for _ in range(n):
        x,y=map(int,input().split())
        xy.append((x,y))
    return n,xy

def main(n,xy):
    xy2 = sorted(xy, key=lambda x: x[0])
    count = 0
    for i in range(n-1):
        xi, yi = xy2[i]
        for j in range(i+1, n):
            xj, yj = xy2[j]
            if -(xj - xi) <= yj - yi and yj - yi <= (xj - xi):
                count += 1
    return count

if __name__=='__main__':
    n,xy=readinput()
    ans=main(n,xy)
    print(ans)
