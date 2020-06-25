def readinput():
    k,s = list(map(int,input().split()))
    return k,s

def main(k,s):
    count=0
    for x in range(k+1):
        for y in range(k+1):
            z=s-x-y
            #print(x,y,z)
            if 0<=z and z<=k:
                count+=1
    return count

if __name__=='__main__':
    k,s=readinput()
    ans=main(k,s)
    print(ans)

