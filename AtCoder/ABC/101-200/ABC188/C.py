def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    aa = []
    for i, elem in enumerate(a):
        aa.append((elem, i))
    half=2**(n-1)
    leftmax = max(aa[:half], key=lambda x:x[0])
    rightmax = max(aa[half:], key=lambda x: x[0])
    if leftmax[0] > rightmax[0]:
        return rightmax[1]+1
    else:
        return leftmax[1]+1

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
