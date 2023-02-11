def readinput():
    a,b,k = list(map(int,input().split()))
    return a,b,k

def main(a,b,k):
    s = set(range(a,min(a+k,b+1)))
    s|=set(range(max(b-k+1,a),b+1))
    ans=sorted(list(s))
    return ans

if __name__=='__main__':
    a,b,k = readinput()
    ans=main(a,b,k)
    for _ in ans:
        print(_)
