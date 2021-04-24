def readinput():
    a,b=map(int,input().split())
    return a,b

def main(a,b):
    astr = str(a)
    bstr = str(b)
    aval = 0
    for c in astr:
        aval += int(c)
    bval = 0
    for c in bstr:
        bval += int(c)
    if aval >= bval:
        return aval
    else:
        return bval

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    print(ans)
