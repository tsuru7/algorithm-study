def readinput():
    n=int(input())
    s=[]
    for _ in range(n):
        s.append(input())
    return n,s

def main(n,s):
    ac=0
    wa=0
    tle=0
    re=0
    for ret in s:
        if ret=='AC':
            ac+=1
        elif ret=='WA':
            wa+=1
        elif ret=='TLE':
            tle+=1
        elif ret=='RE':
            re+=1
    print('AC x {}'.format(ac))
    print('WA x {}'.format(wa))
    print('TLE x {}'.format(tle))
    print('RE x {}'.format(re))

if __name__=='__main__':
    n,s=readinput()
    main(n,s)
