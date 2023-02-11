def readinput():
    n,m,t=map(int,input().split())
    ab = []
    for _ in range(m):
        a,b=map(int,input().split())
        ab.append((a,b))
    return n,m,t,ab

def main(n,m,t,ab):
    t0 = 0
    battery = n
    for a,b in ab:
        battery -= (a-t0)
        # print(f'battery(A): {battery}')
        if battery <= 0:
            return 'No'
        battery += (b-a)
        if battery > n:
            battery = n
        # print(f'battery(A): {battery}')
        t0 = b
    battery -= (t-t0)
    # print(f'battery(T): {battery}')
    if battery <= 0:
        return 'No'
    else:
        return 'Yes'

if __name__=='__main__':
    n,m,t,ab=readinput()
    ans=main(n,m,t,ab)
    print(ans)
