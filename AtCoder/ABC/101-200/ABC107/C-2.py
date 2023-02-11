import sys
INFTY = sys.maxsize

def readinput():
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    return n,k,x

def main(n,k,x):

    tmin = INFTY
    for left_i in range(n):
        right_i = left_i + k - 1
        if not (right_i < len(x)):
            break
        tmin = min(tmin, abs(x[left_i]) + abs(x[right_i] - x[left_i]))
        tmin = min(tmin, abs(x[right_i]) + abs(x[right_i] - x[left_i]))

    return tmin

if __name__=='__main__':
    n,k,x=readinput()
    ans=main(n,k,x)
    print(ans)
