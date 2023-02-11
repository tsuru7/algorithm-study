def readinput():
    r1,c1=map(int,input().split())
    r2,c2=map(int,input().split())
    return r1,c1,r2,c2

def main(r1,c1,r2,c2):
    if r1==r2 and c1==c2:
        return 0
        
    parity1 = (r1+c1)%2
    parity2 = (r2+c2)%2
    if parity1 == parity2:
        if (r1+c1 == r2+c2) or (r1-c1 == r2-c2):
            return 1
        elif abs(r1-r2)+abs(c1-c2) <= 3:
            return 1
        else:
            return 2
    else:
        if abs(r1-r2)+abs(c1-c2) <= 3:
            return 1
        elif (r1+c1==r2+c2+1) or (r1+c1==r2+c2-1) or (r1+c1==r2+c2+3) or (r1+c1==r2+c2-3) \
            or (r1-c1==r2-c2+1) or (r1-c1==r2-c2-1) or (r1-c1==r2-c2+3) or (r1-c1==r2-c2-3):
            return 2
        else:
            return 3

if __name__=='__main__':
    r1,c1,r2,c2=readinput()
    ans=main(r1,c1,r2,c2)
    print(ans)
