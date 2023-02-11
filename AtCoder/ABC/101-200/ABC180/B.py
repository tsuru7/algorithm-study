from math import sqrt
def readinput():
    n=int(input())
    x=list(map(int,input().split()))
    return n,x

def main(n,x):
    dist1 = 0
    for i in range(n):
        dist1 += abs(x[i])
    dist2 = 0
    for i in range(n):
        dist2 += x[i]**2
    dist2 = sqrt(dist2)
    dist3 = 0
    for i in range(n):
        dist3 = max(dist3, abs(x[i]))
    return (dist1, dist2, dist3)

if __name__=='__main__':
    n,x=readinput()
    ans=main(n,x)
    for a in ans:
        print(a)
